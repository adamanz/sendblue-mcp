FROM python:3.10-slim

WORKDIR /app

# Install dependencies first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV MCP_TRANSPORT=stdio

# The server will be started by Smithery using the commandFunction from smithery.yaml
CMD ["python", "-m", "src.main"]