# eligibility-checker Skill

This skill checks a citizen's eligibility for specific government schemes based on provided personal data.

## Activation

The skill can be invoked manually or integrated into a workflow after intent classification (e.g., when the intent is `ELIGIBILITY_CHECK`).

## Command-line interface

```
python check_eligibility.py --scheme <SCHEME_NAME> --age <AGE> --income <INCOME> --land <LAND_AREA> --state <STATE>
```

- `--scheme` – Name of the government scheme (e.g., "PM-KISAN", "PMJAY", "MGNREGA", "PM Awas Yojana").
- `--age` – Citizen's age in years (integer).
- `--income` – Annual income in Indian rupees (numeric, e.g., 450000 for ₹4.5 Lakh).
- `--land` – Land ownership indicator (boolean: `yes`/`no` or numeric area in acres). For simplicity, any non‑zero value is treated as owning land.
- `--state` – Indian state name (used for potential state‑specific extensions; currently not used in hard‑coded rules).

## Hard‑coded eligibility rules

| Scheme | Eligibility conditions |
|--------|--------------------------|
| **PM‑KISAN** | Must be a farmer who **owns land** (land > 0) and is **not an income‑tax payer** (income ≤ 0). |
| **PMJAY** (Pradhan Mantri Jan Arogya Yojana) | Annual income **below ₹5 lakhs** and **not covered by other insurance** (income‑tax payer flag not considered here). |
| **MGNREGA** (Mahila Gram Nyayik Rojgar Abhiyan) | Must belong to a **rural household** (state may be used to infer rural/urban later) and have at least one **adult member** (age ≥ 18). |
| **PM Awas Yojana** | Does **not own a pucca house** (land flag used as proxy) and annual income **below ₹6 lakhs**. |

If a scheme name is not recognized, the script will report that it cannot evaluate the request.

## Output format

- Prints `[ELIGIBLE]` or `[NOT_ELIGIBLE]` with a brief reason.
- Prints `[ACTION: eligibility check run for <scheme>]`.
- Writes a plain‑text report file to:
  `~/.openclaw/workspaces/default/reports/<scheme>_report.txt`
  containing the same information.

## Example usage

```
python check_eligibility.py --scheme PMJAY --age 30 --income 450000 --land 0 --state Rajasthan
```

Outputs:
```
[ELIGIBLE] Eligible for PMJAY: income below 5 Lakhs.
[ACTION: eligibility check run for PMJAY]
```
and writes the same to the report file.

---

**Note**: This skill only contains the contract and documentation. The actual implementation lives in `check_eligibility.py`.
