#!/usr/bin/env python3
"""
Test script to verify the Sendblue MCP server runs correctly with stdio transport.
"""
import os
import sys
import json

# Set environment variables for stdio transport
os.environ["MCP_TRANSPORT"] = "stdio"

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("Starting Sendblue MCP server test with stdio transport...", file=sys.stderr)
print(f"MCP_TRANSPORT: {os.environ.get('MCP_TRANSPORT')}", file=sys.stderr)

try:
    # Import and run the main function
    from src.main import main
    main()
except Exception as e:
    print(f"Error running server: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)