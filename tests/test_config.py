"""
Test configuration and mock data for Sendblue MCP server tests.
"""
import os
from unittest.mock import patch
import json

# Mock API credentials for testing
os.environ["SENDBLUE_API_KEY_ID"] = "test_api_key_id"
os.environ["SENDBLUE_API_SECRET_KEY"] = "test_api_secret_key"

# Test data for messages
TEST_PHONE_NUMBER = "+19998887777"
TEST_GROUP_ID = "66e3b90d-4447-43c6-9439-15a69408ac2"
TEST_GROUP_MEMBERS = ["+19998887777", "+17778889999"]
TEST_MESSAGE_CONTENT = "Hello from Sendblue test!"
TEST_MEDIA_URL = "https://example.com/test-image.jpg"
TEST_CALLBACK_URL = "https://example.com/callback"

# Mock response data
MOCK_SEND_MESSAGE_RESPONSE = {
    "accountEmail": "test@example.com",
    "content": TEST_MESSAGE_CONTENT,
    "is_outbound": True,
    "status": "QUEUED",
    "error_code": None,
    "error_message": None,
    "message_handle": "dfd747ba-5600-4a8a-804a-a614a0fbc1c5",
    "date_sent": "2023-09-27T16:35:32.287Z",
    "date_updated": "2023-09-27T16:35:32.703Z",
    "from_number": "+16468528190",
    "number": TEST_PHONE_NUMBER,
    "to_number": TEST_PHONE_NUMBER,
    "was_downgraded": None,
    "plan": "dedicated",
    "media_url": None,
    "message_type": "message",
    "group_id": "",
    "participants": [],
    "send_style": None,
    "opted_out": False,
    "error_detail": None
}

MOCK_SEND_GROUP_MESSAGE_RESPONSE = {
    "accountEmail": "test@example.com",
    "content": TEST_MESSAGE_CONTENT,
    "is_outbound": True,
    "status": "QUEUED",
    "error_code": None,
    "error_message": None,
    "message_handle": "073c1408-a6d9-48e2-ae8c-01f06443833",
    "date_sent": "2021-05-19T23:07:23.371Z",
    "date_updated": "2021-05-19T23:07:23.371Z",
    "from_number": "+16468528190",
    "number": TEST_GROUP_MEMBERS,
    "to_number": TEST_GROUP_MEMBERS,
    "was_downgraded": None,
    "plan": "blue",
    "media_url": None,
    "message_type": "group",
    "group_id": TEST_GROUP_ID
}

MOCK_LOOKUP_NUMBER_RESPONSE = {
    "number": TEST_PHONE_NUMBER,
    "service": "iMessage"
}

MOCK_TYPING_INDICATOR_RESPONSE = {
    "number": TEST_PHONE_NUMBER,
    "status": "SENT",
    "error_message": None
}

MOCK_GET_MESSAGES_RESPONSE = {
    "messages": [
        {
            "date": "2023-08-15T16:04:38.866Z",
            "allowSMS": None,
            "sendStyle": "",
            "type": "message",
            "uuid": "e8942f7a-c1d2-49e1-b35f-68958754635d",
            "media_url": "",
            "content": "Test message 1",
            "number": TEST_PHONE_NUMBER,
            "is_outbound": True,
            "accountEmail": "test@example.com",
            "was_downgraded": False,
            "callbackURL": "",
            "row_id": None,
            "status": "DELIVERED"
        },
        {
            "date": "2023-08-15T16:05:38.866Z",
            "allowSMS": None,
            "sendStyle": "",
            "type": "message",
            "uuid": "f9942f7a-c1d2-49e1-b35f-68958754636e",
            "media_url": "",
            "content": "Test message 2",
            "number": TEST_PHONE_NUMBER,
            "is_outbound": False,
            "accountEmail": "test@example.com",
            "was_downgraded": False,
            "callbackURL": "",
            "row_id": None,
            "status": "RECEIVED"
        }
    ]
}

MOCK_ADD_RECIPIENT_RESPONSE = {
    "status": "SUCCESS",
    "message": f"Recipient {TEST_PHONE_NUMBER} added successfully to group {TEST_GROUP_ID}"
}

MOCK_UPLOAD_MEDIA_RESPONSE = {
    "status": "OK",
    "message": "File uploaded successfully",
    "mediaObjectId": "MO_asdasdasdasdasd.jpg"
}

# Mock HTTP error responses
MOCK_HTTP_ERROR_RESPONSE = {
    "status": "ERROR",
    "error_message": "Sendblue API error: 400 - Invalid request"
}

# Helper function to create a mock httpx response
class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json_data = json_data
    
    def json(self):
        return self._json_data
    
    def raise_for_status(self):
        if self.status_code >= 400:
            from httpx import HTTPStatusError
            raise HTTPStatusError("Mock HTTP Error", request=None, response=self)