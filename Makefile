PYTHON_VERSIONS := 3.10 3.11 3.12 3.13 3.14
TEST_PY_TARGETS := $(addprefix test-py,$(PYTHON_VERSIONS))

.PHONY: sync test lint format clean test-all

sync:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check

format:
	uv run ruff format

clean:
	rm -rf .venv .venv-* dist *.egg-info .pytest_cache

test-all: $(TEST_PY_TARGETS)

test-py%:
	UV_PROJECT_ENVIRONMENT=.venv-$* uv run --python $* pytest
