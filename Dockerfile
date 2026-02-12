# Endlessh Game - Multi-Stage Dockerfile

# Stage 1: Build Dependencies
FROM python:3.14-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/production.txt requirements/production.txt
COPY requirements/base.txt requirements/base.txt
RUN pip install --no-cache-dir --user -r requirements/production.txt

# Stage 2: Production Image
FROM python:3.14-slim AS production

WORKDIR /app

RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN addgroup --gid 1001 appuser && \
    adduser --disabled-password --gecos "" --uid 1001 --gid 1001 appuser

# Copy Python packages from builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

# Copy application code
COPY --chown=appuser:appuser . .

# Create directories
RUN mkdir -p /app/static-collected /app/logs && \
    chown -R appuser:appuser /app

USER appuser

# Collect static files
RUN DJANGO_SETTINGS_MODULE=config.settings.production \
    SECRET_KEY=build-only-key \
    POSTGRES_HOST=localhost \
    python manage.py collectstatic --noinput 2>/dev/null || true

# Cleanup
RUN find /app -name "*.pyc" -delete && \
    find /app -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/api/v1/health/ || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "2", \
     "--worker-class", "gthread", "--worker-tmp-dir", "/dev/shm", \
     "--log-file", "-", "--access-logfile", "-", "--error-logfile", "-", \
     "config.wsgi:application"]

# Stage 3: Development Image
FROM production AS development

USER root
RUN pip install --no-cache-dir django-debug-toolbar ipython
USER appuser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
