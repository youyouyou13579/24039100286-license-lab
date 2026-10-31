#!/usr/bin/env python3
"""Generate cryptographically secure random passwords."""

import argparse
import secrets
import string

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"


def build_alphabet(upper=True, lower=True, digits=True, symbols=True):
    """Return one string per enabled character group."""
    groups = []
    if upper:
        groups.append(string.ascii_uppercase)
    if lower:
        groups.append(string.ascii_lowercase)
    if digits:
        groups.append(string.digits)
    if symbols:
        groups.append(SYMBOLS)
    return groups


def generate_password(length, groups):
    """Generate a password containing at least one char from each group."""
    if not groups:
        raise ValueError("at least one character group must be enabled")
    if length < len(groups):
        raise ValueError("length must be at least the number of enabled groups")

    alphabet = "".join(groups)
    chars = [secrets.choice(group) for group in groups]
    chars.extend(secrets.choice(alphabet) for _ in range(length - len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate cryptographically secure random passwords."
    )
    parser.add_argument("--length", type=int, default=16, help="password length")
    parser.add_argument("--count", type=int, default=1, help="number of passwords")
    parser.add_argument("--no-upper", action="store_true", help="exclude uppercase")
    parser.add_argument("--no-lower", action="store_true", help="exclude lowercase")
    parser.add_argument("--no-digits", action="store_true", help="exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="exclude symbols")
    return parser


def main():
    args = build_parser().parse_args()
    if args.length < 1:
        raise SystemExit("error: --length must be at least 1")
    groups = build_alphabet(
        upper=not args.no_upper,
        lower=not args.no_lower,
        digits=not args.no_digits,
        symbols=not args.no_symbols,
    )
    for _ in range(args.count):
        try:
            print(generate_password(args.length, groups))
        except ValueError as exc:
            raise SystemExit(f"error: {exc}")


if __name__ == "__main__":
    main()