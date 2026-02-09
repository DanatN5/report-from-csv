install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall:
	uv tool install --force dist/*.whl
	
uninstall:
	uv tool uninstall report-from-csv

run:
	uv run report-from-csv -- help

test:
	uv run pytest

lint:
	uv run ruff check

check: test lint
