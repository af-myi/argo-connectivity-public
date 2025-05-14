FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app.py .

# Expose Flask port
EXPOSE 5000

# Start with Gunicorn (production-grade WSGI server)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]