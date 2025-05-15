"""
HTTP client module for making requests to the Sendblue API.
Provides a configured client with auth headers and error handling.
"""
import httpx
from typing import Dict, Any, Optional

from src.config import SENDBLUE_API_KEY_ID, SENDBLUE_API_SECRET_KEY
from src.config import SENDBLUE_API_BASE_URL, SENDBLUE_ACCOUNTS_BASE_URL

async def make_sendblue_api_request(
    endpoint: str, 
    method: str = "GET", 
    data: Optional[Dict[str, Any]] = None,
    params: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Make a request to the Sendblue API with proper error handling.
    
    Args:
        endpoint (str): The API endpoint (without the base URL)
        method (str): HTTP method (GET or POST)
        data (Optional[Dict[str, Any]]): JSON payload for POST requests
        params (Optional[Dict[str, Any]]): Query parameters for GET requests
        
    Returns:
        Dict[str, Any]: The JSON response from the API
        
    Raises:
        httpx.HTTPError: If the request fails
    """
    # Determine if this is an accounts endpoint or regular API endpoint
    if endpoint.startswith("/accounts"):
        url = f"{SENDBLUE_ACCOUNTS_BASE_URL}{endpoint[9:]}"  # Remove /accounts prefix
    else:
        url = f"{SENDBLUE_API_BASE_URL}{endpoint}"
    
    headers = {
        "sb-api-key-id": SENDBLUE_API_KEY_ID,
        "sb-api-secret-key": SENDBLUE_API_SECRET_KEY,
        "Content-Type": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers, params=params, timeout=30.0)
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers, json=data, timeout=30.0)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            # Try to extract error information from the response if possible
            error_detail = {}
            try:
                error_detail = e.response.json()
            except:
                error_detail = {"error": str(e)}
            
            error_message = (
                f"Sendblue API error: {e.response.status_code} - "
                f"{error_detail.get('error_message', str(e))}"
            )
            
            # Re-raise with more information
            raise httpx.HTTPError(error_message) from e
        except Exception as e:
            raise httpx.HTTPError(f"Error communicating with Sendblue API: {str(e)}")