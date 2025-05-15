"""
Main entry point for the Sendblue MCP server.
Registers all tools with FastMCP and starts the server.
"""
import logging
import os
from mcp.server.fastmcp import FastMCP

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
logger = logging.getLogger("sendblue-mcp")

# Initialize FastMCP server
mcp = FastMCP("sendblue")

# Register tools with FastMCP
mcp.tool()(send_message)
mcp.tool()(send_group_message)
mcp.tool()(lookup_number_service)
mcp.tool()(send_typing_indicator)
mcp.tool()(get_message_history)
mcp.tool()(add_recipient_to_group)
mcp.tool()(upload_media_for_sending)

def main():
    """Main entry point for the server."""
    try:
        # Check that API credentials are configured
        check_credentials()
        
        # Determine transport method from config
        from src.config import MCP_TRANSPORT, MCP_HTTP_PORT
        
        if MCP_TRANSPORT not in ["stdio", "http"]:
            logger.warning(f"Invalid transport '{MCP_TRANSPORT}'. Defaulting to 'stdio'.")
            transport = "stdio"
        else:
            transport = MCP_TRANSPORT
        
        # Log that we're starting
        logger.info(f"Starting Sendblue MCP server with {transport} transport")
        if transport == "http":
            logger.info(f"HTTP server will listen on port {MCP_HTTP_PORT}")
        
        # Initialize and run the server
        if transport == "http":
            mcp.run(transport=transport, port=MCP_HTTP_PORT)
        else:
            mcp.run(transport=transport)
    except ValueError as e:
        logger.error(f"Configuration error: {str(e)}")
        exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()