# Ticket Validator

Reads AMC/service tickets from a CSV, validates each row with Pydantic, and reports valid and invalid rows.

## Setup

uv sync

## Run tests

uv run pytest -v

## Structure

- src/tickets/models.py: Pydantic Ticket model
- src/tickets/validator.py: row validation and logging
- src/tickets/loader.py: CSV reading
- tests/test_tickets.py: 5 tests
- reports/test-report.txt: pytest -v output
