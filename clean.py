"""Clean a messy contacts CSV: names, emails, phones, dates, dedupe -> clean CSV + Markdown report."""
import argparse, csv, re
from datetime import datetime
from pathlib import Path

DATE_FMTS = ["%m/%d/%Y", "%Y-%m-%d", "%d-%b-%Y", "%B %d, %Y", "%m-%d-%Y", "%m/%d/%y"]
PARTICLES = {"van", "der", "de", "la", "von"}

def fix_name(s):
    def word(w):
        if w.lower() in PARTICLES: return w.lower()
        w = "-".join(p.capitalize() for p in w.lower().split("-"))
        w = re.sub(r"^(O')(\w)", lambda m: m[1] + m[2].upper(), w)
        return re.sub(r"^(Mc|Mac)(\w)(?=\w{2,})", lambda m: m[1] + m[2].upper(), w)
    return " ".join(word(w) for w in s.split())

def fix_email(s):
    e = re.sub(r"\s+", "", s).lower().replace(",", ".")
    return (e, True) if re.fullmatch(r"[\w.+'-]+@[\w-]+(\.[\w-]+)+", e) else (e, False)

def fix_phone(s):
    d = re.sub(r"\D", "", s)
    if len(d) == 11 and d[0] == "1": d = d[1:]
    return (f"({d[:3]}) {d[3:6]}-{d[6:]}", True) if len(d) == 10 else ("", False)

def fix_date(s):
    s = s.strip()
    for f in DATE_FMTS:
        try: return datetime.strptime(s, f).date().isoformat(), True
        except ValueError: pass
    return "", False

def clean(rows):
    stats = {"input_rows": len(rows), "blank_rows": 0, "names_changed": 0, "emails_fixed": 0, "emails_invalid": 0,
             "phones_normalized": 0, "phones_missing": 0, "dates_normalized": 0, "dates_missing": 0, "duplicates_removed": 0}
    out, seen, changes = [], set(), []
    for r in rows:
        if not any(v.strip() for v in r.values()): stats["blank_rows"] += 1; continue
        name = fix_name(r["Full Name"]); email, ok_e = fix_email(r["Email"])
        phone, ok_p = fix_phone(r["Phone"]); d, ok_d = fix_date(r["Signup Date"])
        stats["names_changed"] += name != r["Full Name"]; stats["emails_fixed"] += ok_e and email != r["Email"]
        stats["emails_invalid"] += not ok_e; stats["phones_normalized"] += ok_p and phone != r["Phone"]
        stats["phones_missing"] += not ok_p; stats["dates_normalized"] += ok_d and d != r["Signup Date"]; stats["dates_missing"] += not ok_d
        key = email or (name.lower(), phone)
        if key in seen: stats["duplicates_removed"] += 1; continue
        seen.add(key); new = {"Full Name": name, "Email": email, "Phone": phone, "Signup Date": d}
        out.append(new); changes.append((r, new))
    stats["output_rows"] = len(out)
    return out, stats, changes

def report(stats, changes, path):
    L = ["# Data cleanup report", "", "| Metric | Count |", "|---|---|"] + [f"| {k.replace('_',' ')} | {v} |" for k, v in stats.items()]
    L += ["", "## Before / after (first 10 rows)", "", "| Before | After |", "|---|---|"]
    for b, a in changes[:10]: L.append(f"| {' / '.join(b.values())} | {' / '.join(a.values())} |")
    Path(path).write_text("\n".join(L) + "\n")

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input"); ap.add_argument("--out", default="output/clean_contacts.csv"); ap.add_argument("--report", default="output/report.md")
    a = ap.parse_args(argv)
    with open(a.input, newline="") as f: rows = list(csv.DictReader(f))
    out, stats, changes = clean(rows); Path(a.out).parent.mkdir(exist_ok=True, parents=True)
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)
    report(stats, changes, a.report)
    for k, v in stats.items(): print(f"{k.replace('_',' '):20} {v}")
    return out, stats

if __name__ == "__main__": main()
