install:
	uv sync

build:
	uv build

uninstall:
	uv tool uninstall report-from-csv

run:
	uv run report-from-csv -- help

test:
	uv run pytest

lint:
	uv run ruff check

check: test lint
