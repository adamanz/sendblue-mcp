"""
Blaxel MCP Server entrypoint for Sendblue.
This file serves as the main entrypoint for the Blaxel deployment.
"""
import os
import logging
from mcp.server.fastmcp import FastMCP

from src.tools import (
    send_message,
    send_group_message,
    lookup_number_service,
    send_typing_indicator,
    get_message_history,
    add_recipient_to_group,
    upload_media_for_sending
)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("sendblue-mcp-blaxel")

# Initialize FastMCP server
mcp = FastMCP("sendblue-mcp-blaxel")

# Register tools with FastMCP
mcp.tool()(send_message)
mcp.tool()(send_group_message)
mcp.tool()(lookup_number_service)
mcp.tool()(send_typing_indicator)
mcp.tool()(get_message_history)
mcp.tool()(add_recipient_to_group)
mcp.tool()(upload_media_for_sending)

def main():
    """Main entry point for Blaxel deployment."""
    # Check if we have credentials available (for logging purposes only)
    api_key = os.environ.get("SENDBLUE_API_KEY_ID")
    api_secret = os.environ.get("SENDBLUE_API_SECRET_KEY")

    if not api_key or not api_secret:
        logger.warning("Sendblue API credentials not found in environment. They must be set as secrets in Blaxel.")
    else:
        logger.info("Sendblue API credentials detected")

    # Run the MCP server with HTTP transport for Blaxel
    logger.info("Starting Sendblue MCP server on Blaxel")
    mcp.run(transport="http", port=8080)

if __name__ == "__main__":
    main()