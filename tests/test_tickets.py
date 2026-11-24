from pathlib import Path

from tickets.loader import load_tickets

HEADER = "ticket_id,customer_name,priority,status,created_date\n"


def make_csv(tmp_path: Path, text: str) -> Path:
    p = tmp_path / "tickets.csv"
    p.write_text(text, encoding="utf-8")
    return p


def test_valid_row(tmp_path):
    p = make_csv(tmp_path, HEADER + "1,Ravi,high,open,2026-11-20\n")
    valid, invalid = load_tickets(p)
    assert len(valid) == 1
    assert invalid == []


def test_missing_field(tmp_path):
    p = make_csv(tmp_path, "ticket_id,customer_name,priority,status\n1,Ravi,high,open\n")
    valid, invalid = load_tickets(p)
    assert valid == []
    assert len(invalid) == 1


def test_invalid_date(tmp_path):
    p = make_csv(tmp_path, HEADER + "1,Ravi,high,open,2026-13-45\n")
    valid, invalid = load_tickets(p)
    assert valid == []
    assert len(invalid) == 1


def test_invalid_enum(tmp_path):
    p = make_csv(tmp_path, HEADER + "1,Ravi,urgent,open,2026-11-20\n")
    valid, invalid = load_tickets(p)
    assert valid == []
    assert len(invalid) == 1


def test_empty_csv(tmp_path):
    p = make_csv(tmp_path, "")
    valid, invalid = load_tickets(p)
    assert valid == []
    assert invalid == []