"""
Blaxel MCP Server entrypoint for Sendblue.
This file serves as the main entrypoint for the Blaxel deployment.
"""
import os
import logging
from mcp.server.fastmcp import FastMCP
from blaxel.runtime import blaxel_handler

from src.config import check_credentials
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

@blaxel_handler
async def handler(request):
    """
    Blaxel handler for MCP server requests.
    This handler processes incoming MCP protocol requests over HTTP/WebSocket.
    """
    try:
        # Check that API credentials are configured
        check_credentials()

        # Process the MCP request
        logger.info("Processing MCP request via Blaxel")

        # The mcp.run() method will handle the request
        # For Blaxel, we need to use HTTP transport
        return await mcp.handle_request(request)
    except ValueError as e:
        logger.error(f"Configuration error: {str(e)}")
        return {"error": f"Configuration error: {str(e)}"}, 500
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {"error": f"Internal server error"}, 500

# Export the handler for Blaxel
__all__ = ['handler']