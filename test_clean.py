import clean
def test_name():
    assert clean.fix_name("  o'brien  van der berg") == "O'Brien van der Berg"
    assert clean.fix_name("ana-sofia MCDONALD") == "Ana-Sofia McDonald"
def test_email(): assert clean.fix_email(" John.Smith @ Example,com ") == ("john.smith@example.com", True)
def test_phone():
    assert clean.fix_phone("+1 4785550001")[0] == "(478) 555-0001"
    assert clean.fix_phone("n/a") == ("", False)
def test_date():
    for s in ["3/4/2025", "2025-03-04", "04-Mar-2025", "March 4, 2025"]: assert clean.fix_date(s)[0] == "2025-03-04"
def test_dedupe():
    r = {"Full Name": "a b", "Email": "X@example.com", "Phone": "", "Signup Date": ""}
    out, st, _ = clean.clean([r, {**r, "Email": "x@example.com "}, dict.fromkeys(r, "")])
    assert len(out) == 1 and st["duplicates_removed"] == 1 and st["blank_rows"] == 1
