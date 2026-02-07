.PHONY: lint fix typecheck test

lint:
	uv run ruff check .

fix:
	uv run ruff check . --fix
	uv run ruff format .

typecheck:
	uv run mypy src

test:
	uv run pytest -q
