#!/usr/bin/env python3
"""
Launcher script for Sendblue MCP server.
"""
import os
import sys
import logging

# Set up basic logging to stderr
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger("sendblue-launcher")

# Ensure we're in the correct directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
logger.info(f"Changed working directory to: {script_dir}")

# Add the current directory to the Python path
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)
    logger.info(f"Added {script_dir} to Python path")

# Import and run the server
try:
    logger.info("Importing src.main module...")
    from src.main import main
    logger.info("Starting Sendblue MCP server...")
    main()
except Exception as e:
    logger.error(f"Error running Sendblue MCP server: {str(e)}")
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)