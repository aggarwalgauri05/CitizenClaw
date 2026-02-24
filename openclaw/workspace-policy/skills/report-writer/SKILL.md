# report-writer Skill

This skill generates a personalized benefits report for a citizen based on their profile information.

## Activation

The skill can be invoked manually (e.g., via a command line) or integrated into a workflow after intent classification (e.g., when the user asks for a summary of applicable schemes).

## Command‑line interface

```bash
python write_report.py \
    --citizen-name <NAME> \
    --age <AGE> \
    --income <INCOME> \
    --occupation <OCCUPATION> \
    --state <STATE>
```

### Arguments
- `--citizen-name` – Name of the citizen (used for the filename and report header).
- `--age` – Age in years (integer).
- `--income` – Annual income in Indian rupees (numeric, e.g., `450000` for ₹4.5 Lakh).
- `--occupation` – Occupation string (e.g., `daily‑wage worker`).
- `--state` – Indian state name (used for any state‑specific scheme logic).

## Behaviour
1. **Determine matching schemes** – Uses a hard‑coded set of central/state schemes with simple eligibility rules (based on age, income, land ownership, occupation, etc.).
2. **Create a formatted text report** containing:
   - Citizen profile summary
   - List of qualifying schemes with a brief description of the benefit
   - Step‑by‑step next actions for each scheme (e.g., collect documents, visit portal)
   - Official portal URL for each scheme
3. **Save the report** to `~/.openclaw/workspaces/default/reports/<citizen_name>_benefits_report.txt` (creates the folder if needed).
4. **Print an action log** – `[ACTION: report written to <filepath>]`.

## Example usage
```
python write_report.py --citizen-name "Anita" --age 28 --income 120000 --occupation "daily‑wage worker" --state Rajasthan
```
Will generate `~/.../reports/Anita_benefits_report.txt` and print the action line.

---

**Note**: The script contains placeholder eligibility logic that can be expanded later with real scheme data.
