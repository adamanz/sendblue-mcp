#!/usr/bin/env python3
"""
Test script to verify the Sendblue MCP server runs correctly.
"""
import os
import sys
import asyncio
import signal

# Set environment variables for HTTP transport
os.environ["MCP_TRANSPORT"] = "http"
os.environ["MCP_HTTP_PORT"] = "5000"

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the main server function
from src.main import main

print("Starting Sendblue MCP server test with HTTP transport...")
print(f"MCP_TRANSPORT: {os.environ.get('MCP_TRANSPORT')}")
print(f"MCP_HTTP_PORT: {os.environ.get('MCP_HTTP_PORT')}")

# Set up signal handling for graceful shutdown
def signal_handler(sig, frame):
    print("\nShutting down server...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Run the server
try:
    main()
except Exception as e:
    print(f"Error running server: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)