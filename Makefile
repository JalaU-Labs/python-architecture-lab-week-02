.DEFAULT_GOAL := help

UV         ?= uv
SRC_DIR    := src
TEST_DIR   := tests
IMAGE_NAME := math-toolkit-jala
IMAGE_TAG  := latest
ARGS       ?=

docs-serve: ## Serve the documentation locally with live reload
	$(UV) run mkdocs serve

docs-build: ## Build the documentation site
	$(UV) run mkdocs build --strict

.PHONY: help install test lint format typecheck check run clean build docker-build docker-run docs-serve docs-build

help: ## Display this help message
	@awk 'BEGIN {FS = ":.*?## "; printf "Usage: make <target>\n\n"} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install runtime and development dependencies
	$(UV) sync

test: ## Run the test suite with coverage
	$(UV) run pytest

lint: ## Run ruff in check mode
	$(UV) run ruff check $(SRC_DIR) $(TEST_DIR)

format: ## Auto-format the codebase with ruff
	$(UV) run ruff format $(SRC_DIR) $(TEST_DIR)
	$(UV) run ruff check --fix $(SRC_DIR) $(TEST_DIR)

typecheck: ## Run mypy against sources and tests
	$(UV) run mypy $(SRC_DIR) $(TEST_DIR)

check: lint typecheck test ## Run lint, typecheck and tests in sequence

run: ## Run the CLI (usage: make run ARGS="factorial 5")
	$(UV) run math-toolkit-jala $(ARGS)

clean: ## Remove build, test and cache artifacts
	rm -rf build dist htmlcov .coverage .coverage.* .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name '*.egg-info' -prune -exec rm -rf {} +

build: ## Build distribution artifacts (sdist and wheel)
	$(UV) build

docker-build: ## Build the Docker image
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

docker-run: ## Run the CLI inside Docker (usage: make docker-run ARGS="factorial 5")
	docker compose run --rm math-toolkit-jala $(ARGS)
