FROM python:3.10-slim

WORKDIR /app

# Set environment variables for MCP
ENV SMITHERY_DEPLOYMENT=true
ENV MCP_TRANSPORT=stdio
ENV PYTHONUNBUFFERED=1

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port that Smithery expects
EXPOSE 5000

# Default command
CMD ["python", "-m", "src.main"]