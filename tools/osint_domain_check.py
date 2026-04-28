#!/usr/bin/env python3
"""
Passive DNS helper for OSINT lab work.

The script only performs DNS lookups. It does not scan ports, crawl pages,
submit forms, or interact with web applications.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from typing import Dict, List

import dns.exception
import dns.resolver

try:
    from rich.console import Console
    from rich.table import Table

    RICH_AVAILABLE = True
except ImportError:
    Console = None
    Table = None
    RICH_AVAILABLE = False


RECORD_TYPES = ("A", "MX", "TXT", "NS")


@dataclass
class DomainResult:
    domain: str
    records: Dict[str, List[str]] = field(default_factory=dict)
    errors: Dict[str, str] = field(default_factory=dict)
    spf_present: bool = False
    dmarc_present: bool = False
    risk_score: int = 0
    risk_notes: List[str] = field(default_factory=list)


def clean_domain(domain: str) -> str:
    """Normalize common user input mistakes without doing URL parsing."""
    domain = domain.strip().lower()
    domain = domain.removeprefix("https://").removeprefix("http://")
    return domain.strip("/")


def query_records(name: str, record_type: str, resolver: dns.resolver.Resolver) -> List[str]:
    answers = resolver.resolve(name, record_type)
    return [answer.to_text() for answer in answers]


def collect_domain_data(domain: str) -> DomainResult:
    resolver = dns.resolver.Resolver()
    resolver.lifetime = 5
    resolver.timeout = 3

    result = DomainResult(domain=domain)

    for record_type in RECORD_TYPES:
        try:
            result.records[record_type] = query_records(domain, record_type, resolver)
        except dns.resolver.NoAnswer:
            result.records[record_type] = []
        except dns.resolver.NXDOMAIN:
            result.errors[record_type] = "NXDOMAIN"
        except dns.exception.Timeout:
            result.errors[record_type] = "DNS query timed out"
        except dns.exception.DNSException as exc:
            result.errors[record_type] = f"DNS error: {exc.__class__.__name__}"

    txt_records = result.records.get("TXT", [])
    result.spf_present = any("v=spf1" in record.lower() for record in txt_records)

    dmarc_name = f"_dmarc.{domain}"
    try:
        dmarc_records = query_records(dmarc_name, "TXT", resolver)
        result.records["DMARC"] = dmarc_records
        result.dmarc_present = any("v=dmarc1" in record.lower() for record in dmarc_records)
    except dns.resolver.NoAnswer:
        result.records["DMARC"] = []
    except dns.resolver.NXDOMAIN:
        result.records["DMARC"] = []
    except dns.exception.Timeout:
        result.errors["DMARC"] = "DNS query timed out"
    except dns.exception.DNSException as exc:
        result.errors["DMARC"] = f"DNS error: {exc.__class__.__name__}"

    score_result(result)
    return result


def score_result(result: DomainResult) -> None:
    if result.errors:
        result.risk_score += 2
        result.risk_notes.append("DNS errors were observed")

    if not result.records.get("MX"):
        result.risk_score += 1
        result.risk_notes.append("MX record is missing")

    if not result.spf_present:
        result.risk_score += 1
        result.risk_notes.append("SPF record was not found")

    if not result.dmarc_present:
        result.risk_score += 1
        result.risk_notes.append("DMARC record was not found")


def risk_label(score: int) -> str:
    if score >= 4:
        return "High"
    if score >= 2:
        return "Medium"
    return "Low"


def print_plain(result: DomainResult) -> None:
    print(f"Domain: {result.domain}")
    print(f"Risk score: {result.risk_score} ({risk_label(result.risk_score)})")
    print()

    for record_type in (*RECORD_TYPES, "DMARC"):
        print(f"{record_type} records:")
        values = result.records.get(record_type, [])
        if values:
            for value in values:
                print(f"  - {value}")
        else:
            print("  - none found")

        if record_type in result.errors:
            print(f"  error: {result.errors[record_type]}")
        print()

    print(f"SPF present: {'yes' if result.spf_present else 'no'}")
    print(f"DMARC present: {'yes' if result.dmarc_present else 'no'}")

    if result.risk_notes:
        print("\nRisk notes:")
        for note in result.risk_notes:
            print(f"  - {note}")


def print_rich(result: DomainResult) -> None:
    console = Console()
    console.print(f"[bold]Domain:[/bold] {result.domain}")
    console.print(
        f"[bold]Risk score:[/bold] {result.risk_score} "
        f"([bold]{risk_label(result.risk_score)}[/bold])"
    )

    table = Table(title="DNS Records")
    table.add_column("Type", style="cyan")
    table.add_column("Value")
    table.add_column("Error", style="red")

    for record_type in (*RECORD_TYPES, "DMARC"):
        values = result.records.get(record_type, [])
        error = result.errors.get(record_type, "")
        if values:
            for value in values:
                table.add_row(record_type, value, error)
        else:
            table.add_row(record_type, "none found", error)

    console.print(table)
    console.print(f"[bold]SPF present:[/bold] {'yes' if result.spf_present else 'no'}")
    console.print(f"[bold]DMARC present:[/bold] {'yes' if result.dmarc_present else 'no'}")

    if result.risk_notes:
        console.print("\n[bold]Risk notes:[/bold]")
        for note in result.risk_notes:
            console.print(f"- {note}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Passive DNS and email-security check for a domain."
    )
    parser.add_argument("domain", help="Domain to check, for example example.com")
    parser.add_argument(
        "--plain",
        action="store_true",
        help="Use plain text output even if rich is installed.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    domain = clean_domain(args.domain)

    if not domain or "." not in domain:
        print("Please provide a valid domain, for example example.com")
        return 2

    result = collect_domain_data(domain)

    if RICH_AVAILABLE and not args.plain:
        print_rich(result)
    else:
        print_plain(result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
