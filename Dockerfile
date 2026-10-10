# syntax=docker/dockerfile:1.7

# -----------------------------------------------------------------------------
# Stage 1: builder
# Installs uv, resolves dependencies from the lock file, and builds the
# project into an isolated virtual environment.
# -----------------------------------------------------------------------------
FROM python:3.14-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:0.13.0 /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PROJECT_ENVIRONMENT=/app/.venv

WORKDIR /app

# Install only the runtime dependencies first (cache-friendly layer).
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

# Copy project metadata and sources, then install the package itself.
COPY pyproject.toml uv.lock README.md LICENSE ./
COPY src ./src

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-editable

# -----------------------------------------------------------------------------
# Stage 2: runtime
# Minimal image containing only the virtual environment and a non-root user.
# -----------------------------------------------------------------------------
FROM python:3.14-slim AS runtime

RUN groupadd --system --gid 1000 app \
    && useradd --system --uid 1000 --gid app --create-home app

COPY --from=builder --chown=app:app /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
USER app

ENTRYPOINT ["math-utils"]
CMD ["--help"]
