FROM python:3.11.14-alpine3.23

# Set working directory
WORKDIR /app

# Install system dependencies (optional but often needed)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY budget_tracker ./budget_tracker

# Expose FastAPI default port
EXPOSE 9000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "budget_tracker.main:app", "--host", "0.0.0.0", "--port", "9000"]
