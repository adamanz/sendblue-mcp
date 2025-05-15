#!/usr/bin/env python3
"""
Comprehensive test script to verify the Sendblue MCP server.
"""
import os
import sys
import json
import unittest
import asyncio
import subprocess

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=== Sendblue MCP Server Comprehensive Test ===")

# Test 1: Check imports
print("\n1. Testing imports...")
try:
    from src.config import check_credentials
    from src.main import main, mcp
    from src.tools import (
        send_message,
        send_group_message,
        lookup_number_service,
        send_typing_indicator,
        get_message_history,
        add_recipient_to_group,
        upload_media_for_sending
    )
    print("✓ All imports successful")
except Exception as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

# Test 2: Check environment configuration
print("\n2. Testing environment configuration...")
try:
    check_credentials()
    print("✓ API credentials are set")
except ValueError as e:
    print(f"⚠ Warning: {e}")
    print("  (This is expected if running without actual API keys)")

# Test 3: Verify tool registration
print("\n3. Testing tool registration...")
try:
    # Access the FastMCP server's tool registry
    tools = mcp._tools if hasattr(mcp, '_tools') else {}
    expected_tools = [
        'send_message',
        'send_group_message',
        'lookup_number_service',
        'send_typing_indicator',
        'get_message_history',
        'add_recipient_to_group',
        'upload_media_for_sending'
    ]
    
    registered_tools = list(tools.keys())
    print(f"Registered tools: {registered_tools}")
    
    for tool in expected_tools:
        if tool in registered_tools:
            print(f"✓ {tool} is registered")
        else:
            print(f"✗ {tool} is NOT registered")
    
    if len(registered_tools) == len(expected_tools):
        print(f"✓ All {len(expected_tools)} tools are registered")
    else:
        print(f"⚠ Expected {len(expected_tools)} tools, found {len(registered_tools)}")
except Exception as e:
    print(f"✗ Error checking tools: {e}")

# Test 4: Run unit tests
print("\n4. Running unit tests...")
try:
    # Run the unit tests and capture output
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✓ All unit tests pass")
    else:
        print(f"✗ Unit tests failed:")
        print(result.stdout)
        print(result.stderr)
except Exception as e:
    print(f"✗ Error running unit tests: {e}")

# Test 5: Test server startup
print("\n5. Testing server startup...")
try:
    # Test with stdio transport
    os.environ["MCP_TRANSPORT"] = "stdio"
    print("Testing stdio transport...")
    
    # Start the server in a subprocess (will timeout as expected)
    proc = subprocess.Popen(
        [sys.executable, "-m", "src.main"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Let it run for a moment
    import time
    time.sleep(1)
    
    # Check if it's still running (should be)
    if proc.poll() is None:
        print("✓ Server started successfully with stdio transport")
        proc.terminate()
    else:
        stderr = proc.stderr.read()
        print(f"✗ Server exited unexpectedly: {stderr}")
        
except Exception as e:
    print(f"✗ Error testing server startup: {e}")

print("\n=== Test Summary ===")
print("All critical tests have been run.")
print("To test with actual API calls, ensure your SENDBLUE_API_KEY_ID")
print("and SENDBLUE_API_SECRET_KEY are set in the .env file.")
print("\nFor Docker testing, run:")
print("  docker build -t sendblue-mcp .")
print("  docker run -p 5000:5000 --env-file .env sendblue-mcp")