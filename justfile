fmt:
    uv run ruff format --exit-non-zero-on-format .

lint:
    uv run ruff check . --fix

static_check:
    uv run mypy .

check: fmt lint static_check
