"""
Mock helpers for testing the Sendblue MCP server.
"""
from unittest.mock import patch, AsyncMock
import httpx

from tests.test_config import (
    MOCK_SEND_MESSAGE_RESPONSE,
    MOCK_SEND_GROUP_MESSAGE_RESPONSE,
    MOCK_LOOKUP_NUMBER_RESPONSE,
    MOCK_TYPING_INDICATOR_RESPONSE,
    MOCK_GET_MESSAGES_RESPONSE,
    MOCK_ADD_RECIPIENT_RESPONSE,
    MOCK_UPLOAD_MEDIA_RESPONSE,
    MOCK_HTTP_ERROR_RESPONSE,
    MockResponse
)

def mock_httpx_client():
    """Return a mock httpx AsyncClient that returns predefined responses."""
    mock_client = AsyncMock()
    
    # Configure the get method to return different responses based on URL
    async def mock_get(url, **kwargs):
        if "evaluate-service" in url:
            return MockResponse(200, MOCK_LOOKUP_NUMBER_RESPONSE)
        elif "accounts/messages" in url:
            return MockResponse(200, MOCK_GET_MESSAGES_RESPONSE)
        else:
            # Default response for unknown GET endpoints
            return MockResponse(404, {"error": "Not found"})
    
    # Configure the post method to return different responses based on URL
    async def mock_post(url, **kwargs):
        if "send-message" in url:
            return MockResponse(200, MOCK_SEND_MESSAGE_RESPONSE)
        elif "send-group-message" in url:
            return MockResponse(200, MOCK_SEND_GROUP_MESSAGE_RESPONSE)
        elif "modify-group" in url:
            return MockResponse(200, MOCK_ADD_RECIPIENT_RESPONSE)
        elif "send-typing-indicator" in url:
            return MockResponse(200, MOCK_TYPING_INDICATOR_RESPONSE)
        elif "upload-media-object" in url:
            return MockResponse(200, MOCK_UPLOAD_MEDIA_RESPONSE)
        else:
            # Default response for unknown POST endpoints
            return MockResponse(404, {"error": "Not found"})
    
    mock_client.get = mock_get
    mock_client.post = mock_post
    
    return mock_client

def configure_client_mock_success():
    """Configure a mock httpx client that returns successful responses."""
    mock_client = mock_httpx_client()
    return patch("httpx.AsyncClient", return_value=mock_client)

def configure_client_mock_error():
    """Configure a mock httpx client that returns error responses."""
    mock_client = AsyncMock()
    
    async def mock_error(*args, **kwargs):
        raise httpx.HTTPError("Mock HTTP Error")
    
    mock_client.get = mock_error
    mock_client.post = mock_error
    
    return patch("httpx.AsyncClient", return_value=mock_client)