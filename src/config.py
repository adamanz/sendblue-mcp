"""
Configuration module for Sendblue MCP server.
Handles loading of API credentials and server settings.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Sendblue API credentials
SENDBLUE_API_KEY_ID = os.environ.get("SENDBLUE_API_KEY_ID")
SENDBLUE_API_SECRET_KEY = os.environ.get("SENDBLUE_API_SECRET_KEY")

# Sendblue API constants
SENDBLUE_API_BASE_URL = "https://api.sendblue.co/api"
SENDBLUE_ACCOUNTS_BASE_URL = "https://api.sendblue.co/accounts"

# Dictionary of valid send styles for expressive messages
VALID_SEND_STYLES = {
    "celebration",
    "shooting_star",
    "fireworks", 
    "lasers", 
    "love", 
    "confetti", 
    "balloons", 
    "spotlight", 
    "echo", 
    "invisible", 
    "gentle", 
    "loud", 
    "slam"
}

def check_credentials():
    """Verify that required API credentials are set."""
    if not SENDBLUE_API_KEY_ID:
        raise ValueError("SENDBLUE_API_KEY_ID is not set")
    if not SENDBLUE_API_SECRET_KEY:
        raise ValueError("SENDBLUE_API_SECRET_KEY is not set")
    return True