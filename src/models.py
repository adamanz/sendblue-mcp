"""
Pydantic models for validating tool parameters and Sendblue API responses.
"""
from typing import List, Optional, Union
from pydantic import BaseModel, Field, validator, HttpUrl
import re

from src.config import VALID_SEND_STYLES

# Regular expression for E.164 phone number format
E164_PATTERN = r"^\+[1-9]\d{1,14}$"

class SendMessageParams(BaseModel):
    """Parameters for the send_message tool."""
    to_number: str = Field(..., description="The E.164 formatted phone number of the recipient")
    content: Optional[str] = Field(None, description="The text content of the message")
    from_number: Optional[str] = Field(None, description="The E.164 formatted Sendblue number to send from")
    media_url: Optional[str] = Field(None, description="Publicly accessible URL of an image or .caf voice note file")
    send_style: Optional[str] = Field(None, description="Expressive style for iMessage")
    status_callback: Optional[str] = Field(None, description="Webhook URL for message status updates")
    
    @validator('to_number', 'from_number')
    def validate_phone_number(cls, v):
        """Validate that phone numbers are in E.164 format."""
        if v and not re.match(E164_PATTERN, v):
            raise ValueError(f"Phone number must be in E.164 format (e.g., +19998887777)")
        return v
    
    @validator('send_style')
    def validate_send_style(cls, v):
        """Validate that send style is one of the allowed values."""
        if v and v not in VALID_SEND_STYLES:
            raise ValueError(f"Invalid send style. Must be one of: {', '.join(VALID_SEND_STYLES)}")
        return v
    
    @validator('content', 'media_url')
    def validate_content_or_media(cls, v, values):
        """Validate that either content or media_url is provided."""
        if 'content' in values and not values['content'] and 'media_url' in values and not values['media_url']:
            raise ValueError("Either content or media_url must be provided")
        return v


class SendGroupMessageParams(BaseModel):
    """Parameters for the send_group_message tool."""
    to_numbers: Optional[List[str]] = Field(None, description="Array of E.164 formatted phone numbers for group recipients (max 25)")
    group_id: Optional[str] = Field(None, description="UUID of an existing group")
    content: Optional[str] = Field(None, description="The text content of the message")
    from_number: Optional[str] = Field(None, description="The E.164 formatted Sendblue number to send from")
    media_url: Optional[str] = Field(None, description="Publicly accessible URL to media")
    send_style: Optional[str] = Field(None, description="Expressive style for iMessage")
    status_callback: Optional[str] = Field(None, description="Webhook URL for message status updates")
    
    @validator('to_numbers')
    def validate_to_numbers(cls, v):
        """Validate that to_numbers contains valid E.164 phone numbers and has at most 25 numbers."""
        if v:
            if len(v) > 25:
                raise ValueError("Group chats can have at most 25 participants")
            for number in v:
                if not re.match(E164_PATTERN, number):
                    raise ValueError(f"Phone number {number} must be in E.164 format (e.g., +19998887777)")
        return v
    
    @validator('from_number')
    def validate_phone_number(cls, v):
        """Validate that phone numbers are in E.164 format."""
        if v and not re.match(E164_PATTERN, v):
            raise ValueError(f"Phone number must be in E.164 format (e.g., +19998887777)")
        return v
    
    @validator('send_style')
    def validate_send_style(cls, v):
        """Validate that send style is one of the allowed values."""
        if v and v not in VALID_SEND_STYLES:
            raise ValueError(f"Invalid send style. Must be one of: {', '.join(VALID_SEND_STYLES)}")
        return v
    
    @validator('group_id', 'to_numbers')
    def validate_group_id_or_to_numbers(cls, v, values, **kwargs):
        """Validate that either group_id or to_numbers is provided."""
        field_name = kwargs.get('field_name')
        other_field = 'to_numbers' if field_name == 'group_id' else 'group_id'
        
        if field_name == 'to_numbers' and not v and not values.get(other_field):
            raise ValueError("Either to_numbers or group_id must be provided")
            
        return v
    
    @validator('content', 'media_url')
    def validate_content_or_media(cls, v, values):
        """Validate that either content or media_url is provided."""
        if 'content' in values and not values['content'] and 'media_url' in values and not values['media_url']:
            raise ValueError("Either content or media_url must be provided")
        return v


class LookupNumberServiceParams(BaseModel):
    """Parameters for the lookup_number_service tool."""
    phone_number: str = Field(..., description="The E.164 formatted phone number to evaluate")
    
    @validator('phone_number')
    def validate_phone_number(cls, v):
        """Validate that phone numbers are in E.164 format."""
        if not re.match(E164_PATTERN, v):
            raise ValueError(f"Phone number must be in E.164 format (e.g., +19998887777)")
        return v


class SendTypingIndicatorParams(BaseModel):
    """Parameters for the send_typing_indicator tool."""
    to_number: str = Field(..., description="The E.164 formatted phone number to send the typing indicator to")
    
    @validator('to_number')
    def validate_phone_number(cls, v):
        """Validate that phone numbers are in E.164 format."""
        if not re.match(E164_PATTERN, v):
            raise ValueError(f"Phone number must be in E.164 format (e.g., +19998887777)")
        return v


class GetMessageHistoryParams(BaseModel):
    """Parameters for the get_message_history tool."""
    contact_phone_number: Optional[str] = Field(None, description="Filter by sender/recipient E.164 phone number")
    conversation_id: Optional[str] = Field(None, description="Filter by conversation ID (contact ID)")
    limit: Optional[int] = Field(50, description="Maximum number of messages per request")
    offset: Optional[int] = Field(0, description="Offset for paginating through messages")
    from_date: Optional[str] = Field(None, description="Filter messages sent after this date/time (e.g., '2023-06-15 12:00:00')")
    
    @validator('contact_phone_number')
    def validate_phone_number(cls, v):
        """Validate that phone numbers are in E.164 format."""
        if v and not re.match(E164_PATTERN, v):
            raise ValueError(f"Phone number must be in E.164 format (e.g., +19998887777)")
        return v
    
    @validator('limit')
    def validate_limit(cls, v):
        """Validate that limit is a positive integer."""
        if v and (v < 1 or v > 1000):
            raise ValueError("Limit must be between 1 and 1000")
        return v
    
    @validator('offset')
    def validate_offset(cls, v):
        """Validate that offset is a non-negative integer."""
        if v and v < 0:
            raise ValueError("Offset cannot be negative")
        return v


class AddRecipientToGroupParams(BaseModel):
    """Parameters for the add_recipient_to_group tool."""
    group_id: str = Field(..., description="The ID (uuid) of the group to which the recipient will be added")
    recipient_number: str = Field(..., description="The E.164 formatted phone number of the recipient to add to the group")
    
    @validator('recipient_number')
    def validate_phone_number(cls, v):
        """Validate that phone numbers are in E.164 format."""
        if not re.match(E164_PATTERN, v):
            raise ValueError(f"Phone number must be in E.164 format (e.g., +19998887777)")
        return v


class UploadMediaParams(BaseModel):
    """Parameters for the upload_media_for_sending tool."""
    media_file_url: str = Field(..., description="The publicly accessible URL of the media file")