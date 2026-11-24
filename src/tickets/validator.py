import logging
from collections.abc import Iterable
from typing import Any

from pydantic import ValidationError

from tickets.models import Ticket

logger = logging.getLogger(__name__)


def validate_rows(
    rows: Iterable[dict[str, Any]],
) -> tuple[list[Ticket], list[tuple[int, str]]]:
    """Validate each row. Returns (valid tickets, invalid rows as (line, error))."""
    valid: list[Ticket] = []
    invalid: list[tuple[int, str]] = []

    for line_no, row in enumerate(rows, start=2):  # line 1 is the header
        try:
            valid.append(Ticket(**row))
            logger.info("Row %d valid", line_no)
        except ValidationError as e:
            invalid.append((line_no, str(e)))
            logger.warning("Row %d invalid: %d error(s)", line_no, e.error_count())

    logger.info("Done: %d valid, %d invalid", len(valid), len(invalid))
    return valid, invalid