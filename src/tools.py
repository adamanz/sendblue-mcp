"""
MCP tools for the Sendblue API.
Implements all the tools specified in the MCP Server Specification.
"""
from typing import Dict, Any, List, Optional, Union
import httpx

from src.client import make_sendblue_api_request
from src.models import (
    SendMessageParams,
    SendGroupMessageParams,
    LookupNumberServiceParams,
    SendTypingIndicatorParams,
    GetMessageHistoryParams,
    AddRecipientToGroupParams,
    UploadMediaParams
)

async def send_message(
    to_number: str,
    content: Optional[str] = None,
    from_number: Optional[str] = None,
    media_url: Optional[str] = None,
    send_style: Optional[str] = None,
    status_callback: Optional[str] = None
) -> Dict[str, Any]:
    """
    Sends a message (iMessage or SMS) to a single recipient.
    
    Args:
        to_number: The E.164 formatted phone number of the recipient.
        content: The text content of the message.
        from_number: The E.164 formatted Sendblue number to send the message from.
        media_url: Publicly accessible URL of an image or .caf voice note file.
        send_style: Expressive style for iMessage (e.g., "invisible", "fireworks", "slam").
        status_callback: Webhook URL for message status updates.
    
    Returns:
        Dict containing the Sendblue API response with message status and details.
    """
    # Validate parameters
    params = SendMessageParams(
        to_number=to_number,
        content=content,
        from_number=from_number,
        media_url=media_url,
        send_style=send_style,
        status_callback=status_callback
    )
    
    # Prepare API request
    request_data = {
        "number": params.to_number,
        "content": params.content
    }
    
    # Add optional parameters if provided
    if params.from_number:
        request_data["from_number"] = params.from_number
    
    if params.media_url:
        request_data["media_url"] = params.media_url
    
    if params.send_style:
        request_data["send_style"] = params.send_style
    
    if params.status_callback:
        request_data["status_callback"] = params.status_callback
    
    try:
        # Make API request
        response = await make_sendblue_api_request(
            endpoint="/send-message",
            method="POST",
            data=request_data
        )
        return response
    except httpx.HTTPError as e:
        return {
            "status": "ERROR",
            "error_message": str(e)
        }


async def send_group_message(
    to_numbers: Optional[List[str]] = None,
    group_id: Optional[str] = None,
    content: Optional[str] = None,
    from_number: Optional[str] = None,
    media_url: Optional[str] = None,
    send_style: Optional[str] = None,
    status_callback: Optional[str] = None
) -> Dict[str, Any]:
    """
    Sends a message to a group of recipients. If the group does not exist, it will be created.
    
    Args:
        to_numbers: Array of E.164 formatted phone numbers for group recipients (max 25).
        group_id: UUID of an existing group.
        content: The text content of the message.
        from_number: The E.164 formatted Sendblue number to send the message from.
        media_url: Publicly accessible URL to media.
        send_style: Expressive style for iMessage.
        status_callback: Webhook URL for message status updates.
    
    Returns:
        Dict containing the Sendblue API response including group_id and message status.
    """
    # Validate parameters
    params = SendGroupMessageParams(
        to_numbers=to_numbers,
        group_id=group_id,
        content=content,
        from_number=from_number,
        media_url=media_url,
        send_style=send_style,
        status_callback=status_callback
    )
    
    # Prepare API request
    request_data = {}
    
    # Add either numbers or group_id (required)
    if params.to_numbers:
        request_data["numbers"] = params.to_numbers
    elif params.group_id:
        request_data["group_id"] = params.group_id
    
    # Add content if provided
    if params.content:
        request_data["content"] = params.content
    
    # Add optional parameters if provided
    if params.from_number:
        request_data["from_number"] = params.from_number
    
    if params.media_url:
        request_data["media_url"] = params.media_url
    
    if params.send_style:
        request_data["send_style"] = params.send_style
    
    if params.status_callback:
        request_data["status_callback"] = params.status_callback
    
    try:
        # Make API request
        response = await make_sendblue_api_request(
            endpoint="/send-group-message",
            method="POST",
            data=request_data
        )
        return response
    except httpx.HTTPError as e:
        return {
            "status": "ERROR",
            "error_message": str(e)
        }


async def lookup_number_service(phone_number: str) -> Dict[str, Any]:
    """
    Determines if a phone number supports iMessage or SMS.
    
    Args:
        phone_number: The E.164 formatted phone number to evaluate.
    
    Returns:
        Dict containing the number and service type (iMessage or SMS).
    """
    # Validate parameters
    params = LookupNumberServiceParams(phone_number=phone_number)
    
    try:
        # Make API request 
        response = await make_sendblue_api_request(
            endpoint="/evaluate-service",
            method="GET",
            params={"number": params.phone_number}
        )
        return response
    except httpx.HTTPError as e:
        return {
            "status": "ERROR",
            "error_message": str(e)
        }


async def send_typing_indicator(to_number: str) -> Dict[str, Any]:
    """
    Sends a typing indicator (animated dots) to a recipient.
    
    Args:
        to_number: The E.164 formatted phone number to send the typing indicator to.
    
    Returns:
        Dict containing the status of the typing indicator request.
    """
    # Validate parameters
    params = SendTypingIndicatorParams(to_number=to_number)
    
    # Prepare API request
    request_data = {
        "number": params.to_number
    }
    
    try:
        # Make API request
        response = await make_sendblue_api_request(
            endpoint="/send-typing-indicator",
            method="POST",
            data=request_data
        )
        return response
    except httpx.HTTPError as e:
        return {
            "status": "ERROR",
            "error_message": str(e)
        }


async def get_message_history(
    contact_phone_number: Optional[str] = None,
    conversation_id: Optional[str] = None,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0,
    from_date: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Retrieves message history for the account.
    
    Args:
        contact_phone_number: Filter by sender/recipient E.164 phone number.
        conversation_id: Filter by conversation ID (contact ID).
        limit: Maximum number of messages per request.
        offset: Offset for paginating through messages.
        from_date: Filter messages sent after this date/time (e.g., "2023-06-15 12:00:00").
    
    Returns:
        List of message objects.
    """
    # Validate parameters
    params = GetMessageHistoryParams(
        contact_phone_number=contact_phone_number,
        conversation_id=conversation_id,
        limit=limit,
        offset=offset,
        from_date=from_date
    )
    
    # Prepare query parameters
    query_params = {}
    
    if params.contact_phone_number:
        query_params["number"] = params.contact_phone_number
    
    if params.conversation_id:
        query_params["cid"] = params.conversation_id
    
    if params.limit:
        query_params["limit"] = params.limit
    
    if params.offset:
        query_params["offset"] = params.offset
    
    if params.from_date:
        query_params["from_date"] = params.from_date
    
    try:
        # Make API request
        response = await make_sendblue_api_request(
            endpoint="/accounts/messages",
            method="GET",
            params=query_params
        )
        # Return the messages array from the response
        return response.get("messages", [])
    except httpx.HTTPError as e:
        return [{
            "status": "ERROR",
            "error_message": str(e)
        }]


async def add_recipient_to_group(
    group_id: str,
    recipient_number: str
) -> Dict[str, Any]:
    """
    Adds a new recipient to an existing group chat.
    
    Args:
        group_id: The ID (uuid) of the group to which the recipient will be added.
        recipient_number: The E.164 formatted phone number of the recipient to add to the group.
    
    Returns:
        Dict indicating success or failure.
    """
    # Validate parameters
    params = AddRecipientToGroupParams(
        group_id=group_id,
        recipient_number=recipient_number
    )
    
    # Prepare API request
    request_data = {
        "group_id": params.group_id,
        "modify_type": "add_recipient",  # Hardcoded to add_recipient as per spec
        "number": params.recipient_number
    }
    
    try:
        # Make API request
        response = await make_sendblue_api_request(
            endpoint="/modify-group",
            method="POST",
            data=request_data
        )
        return response
    except httpx.HTTPError as e:
        return {
            "status": "ERROR",
            "error_message": str(e)
        }


async def upload_media_for_sending(media_file_url: str) -> Dict[str, Any]:
    """
    Uploads a media file from a publicly accessible URL to Sendblue's servers.
    
    Args:
        media_file_url: The publicly accessible URL of the media file.
    
    Returns:
        Dict containing upload status and mediaObjectId if successful.
    """
    # Validate parameters
    params = UploadMediaParams(media_file_url=media_file_url)
    
    # Prepare API request
    request_data = {
        "media_url": params.media_file_url
    }
    
    try:
        # Make API request
        response = await make_sendblue_api_request(
            endpoint="/upload-media-object",
            method="POST",
            data=request_data
        )
        return response
    except httpx.HTTPError as e:
        return {
            "status": "ERROR",
            "error_message": str(e)
        }