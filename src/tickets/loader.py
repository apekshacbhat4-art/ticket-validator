import csv
from pathlib import Path

from tickets.models import Ticket
from tickets.validator import validate_rows


def read_rows(path: Path) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_tickets(path: Path) -> tuple[list[Ticket], list[tuple[int, str]]]:
    return validate_rows(read_rows(Path(path)))