#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path

REPORT_DIR = Path.home() / '.openclaw' / 'workspaces' / 'default' / 'reports'
REPORT_DIR.mkdir(parents=True, exist_ok=True)

RULES = {
    'PM-KISAN': lambda age, income, land, state: (land != 0) and (income <= 0),
    'PMJAY': lambda age, income, land, state: (income < 500000),
    'MGNREGA': lambda age, income, land, state: (age >= 18) and (state is not None),
    'PM Awas Yojana': lambda age, income, land, state: (land == 0) and (income < 600000),
}

def parse_bool(val):
    return str(val).lower() in ['yes', 'true', '1']

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scheme', required=True)
    ap.add_argument('--age', type=int, required=True)
    ap.add_argument('--income', type=int, required=True)
    ap.add_argument('--land', required=True)
    ap.add_argument('--state', required=True)
    args = ap.parse_args()

    scheme = args.scheme
    age = args.age
    income = args.income
    land = parse_bool(args.land) and 1 or int(args.land) if args.land.isdigit() else (1 if args.land.lower() in ['yes','true'] else 0)
    state = args.state

    result = None
    reason = ''
    if scheme in RULES:
        eligibility = RULES[scheme](age, income, land, state)
        if eligibility:
            result = 'ELIGIBLE'
            reason = 'Meets basic internal criteria.'
        else:
            result = 'NOT_ELIGIBLE'
            reason = 'Does not meet internal criteria.'
    else:
        print(f"[NOT_ELIGIBLE] Unknown scheme: {scheme}")
        reason = 'Unknown scheme'
        result = 'NOT_ELIGIBLE'

    output = f"[{result}] {scheme}: {reason}"
    print(output)
    print(f"[ACTION: eligibility check run for {scheme}]")

    report_file = REPORT_DIR / f"{scheme}_report.txt"
    with report_file.open('w') as f:
        f.write(output + "\n")
        f.write(f"[ACTION: eligibility check run for {scheme}]\n")

if __name__ == '__main__':
    main()
