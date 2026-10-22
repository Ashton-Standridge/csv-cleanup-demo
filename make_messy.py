"""Generate a messy fake contacts CSV (all names/emails/phones are fictional)."""
import csv, random
from pathlib import Path
random.seed(7)
FIRST = ["john", "MARIA", "  li ", "o'brien", "ana-sofia", "DeShawn", "mcdonald", "priya"]
LAST = ["smith", "GARCIA", "nguyen ", "o'neil", "van der berg", "JOHNSON", "macleod", "patel"]
def phone(i):
    d = f"478555{i:04d}"[-10:]
    return random.choice([f"({d[:3]}) {d[3:6]}-{d[6:]}", f"{d[:3]}.{d[3:6]}.{d[6:]}", f"+1 {d}", f"1-{d[:3]}-{d[3:6]}-{d[6:]}", d, "n/a"])
def dt(i):
    m, d, y = 1 + i % 12, 1 + i % 27, 2024 + i % 2
    return random.choice([f"{m}/{d}/{y}", f"{y}-{m:02d}-{d:02d}", f"{d:02d}-{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][m-1]}-{y}", f"{['January','March','June'][i%3]} {d}, {y}", ""])
def main(path=Path(__file__).parent / "samples/messy_contacts.csv"):
    path.parent.mkdir(exist_ok=True); rows = []
    for i in range(40):
        f, l = random.choice(FIRST), random.choice(LAST)
        email = f"{f.strip().lower().replace(chr(39),'')}.{l.strip().lower().replace(' ','')}{i}@example.com"
        email = random.choice([email, email.upper(), f" {email} ", email.replace("@", " @ "), email.replace(".com", ",com")])
        rows.append([f"{f} {l}", email, phone(i), dt(i)])
    rows += [rows[3][:], [rows[5][0].upper(), rows[5][1].upper(), rows[5][2], rows[5][3]], rows[10][:], ["", "", "", ""]]
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["Full Name", "Email", "Phone", "Signup Date"]); w.writerows(rows)
    print(f"wrote {len(rows)} messy rows -> {path}")
if __name__ == "__main__": main()
