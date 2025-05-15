"""
Unit tests for the Sendblue MCP server tools.
"""
import unittest
import asyncio
from unittest.mock import patch, MagicMock, AsyncMock
import httpx

from src.tools import (
    send_message,
    send_group_message,
    lookup_number_service,
    send_typing_indicator,
    get_message_history,
    add_recipient_to_group,
    upload_media_for_sending
)

from tests.test_config import (
    TEST_PHONE_NUMBER, 
    TEST_GROUP_ID, 
    TEST_GROUP_MEMBERS,
    TEST_MESSAGE_CONTENT, 
    TEST_MEDIA_URL, 
    TEST_CALLBACK_URL,
    MOCK_SEND_MESSAGE_RESPONSE,
    MOCK_SEND_GROUP_MESSAGE_RESPONSE,
    MOCK_LOOKUP_NUMBER_RESPONSE,
    MOCK_TYPING_INDICATOR_RESPONSE,
    MOCK_GET_MESSAGES_RESPONSE,
    MOCK_ADD_RECIPIENT_RESPONSE,
    MOCK_UPLOAD_MEDIA_RESPONSE,
    MOCK_HTTP_ERROR_RESPONSE
)

from tests.mock_helper import configure_client_mock_success, configure_client_mock_error


class TestSendMessageTool(unittest.TestCase):
    """Test cases for the send_message tool."""
    
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    def tearDown(self):
        self.loop.close()
    
    def test_send_message_success(self):
        """Test successful send_message request."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_SEND_MESSAGE_RESPONSE):
                result = self.loop.run_until_complete(
                    send_message(
                        to_number=TEST_PHONE_NUMBER,
                        content=TEST_MESSAGE_CONTENT
                    )
                )
                
                # Verify the response matches our expected mock data
                self.assertEqual(result["status"], "QUEUED")
                self.assertEqual(result["content"], TEST_MESSAGE_CONTENT)
                self.assertEqual(result["to_number"], TEST_PHONE_NUMBER)
    
    def test_send_message_with_optional_params(self):
        """Test send_message with all optional parameters."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_SEND_MESSAGE_RESPONSE):
                result = self.loop.run_until_complete(
                    send_message(
                        to_number=TEST_PHONE_NUMBER,
                        content=TEST_MESSAGE_CONTENT,
                        from_number="+16468528190",
                        media_url=TEST_MEDIA_URL,
                        send_style="invisible",
                        status_callback=TEST_CALLBACK_URL
                    )
                )
                
                # Verify the response matches our expected mock data
                self.assertEqual(result["status"], "QUEUED")
    
    def test_send_message_error(self):
        """Test error handling in send_message."""
        with configure_client_mock_error():
            # Patch the make_sendblue_api_request function to raise an HTTPError
            with patch('src.tools.make_sendblue_api_request', side_effect=httpx.HTTPError("Mock HTTP Error")):
                result = self.loop.run_until_complete(
                    send_message(
                        to_number=TEST_PHONE_NUMBER,
                        content=TEST_MESSAGE_CONTENT
                    )
                )
                
                # Verify error response
                self.assertEqual(result["status"], "ERROR")
                self.assertTrue("error_message" in result)


class TestSendGroupMessageTool(unittest.TestCase):
    """Test cases for the send_group_message tool."""
    
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    def tearDown(self):
        self.loop.close()
    
    def test_send_group_message_with_numbers_success(self):
        """Test successful send_group_message request with to_numbers."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_SEND_GROUP_MESSAGE_RESPONSE):
                result = self.loop.run_until_complete(
                    send_group_message(
                        to_numbers=TEST_GROUP_MEMBERS,
                        content=TEST_MESSAGE_CONTENT
                    )
                )
                
                # Verify the response matches our expected mock data
                self.assertEqual(result["status"], "QUEUED")
                self.assertEqual(result["content"], TEST_MESSAGE_CONTENT)
                self.assertEqual(result["group_id"], TEST_GROUP_ID)
    
    def test_send_group_message_with_group_id_success(self):
        """Test successful send_group_message request with group_id."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_SEND_GROUP_MESSAGE_RESPONSE):
                result = self.loop.run_until_complete(
                    send_group_message(
                        group_id=TEST_GROUP_ID,
                        content=TEST_MESSAGE_CONTENT
                    )
                )
                
                # Verify the response matches our expected mock data
                self.assertEqual(result["status"], "QUEUED")
                self.assertEqual(result["content"], TEST_MESSAGE_CONTENT)
                self.assertEqual(result["group_id"], TEST_GROUP_ID)
    
    def test_send_group_message_error(self):
        """Test error handling in send_group_message."""
        with configure_client_mock_error():
            # Patch the make_sendblue_api_request function to raise an HTTPError
            with patch('src.tools.make_sendblue_api_request', side_effect=httpx.HTTPError("Mock HTTP Error")):
                result = self.loop.run_until_complete(
                    send_group_message(
                        to_numbers=TEST_GROUP_MEMBERS,
                        content=TEST_MESSAGE_CONTENT
                    )
                )
                
                # Verify error response
                self.assertEqual(result["status"], "ERROR")
                self.assertTrue("error_message" in result)


class TestLookupNumberServiceTool(unittest.TestCase):
    """Test cases for the lookup_number_service tool."""
    
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    def tearDown(self):
        self.loop.close()
    
    def test_lookup_number_service_success(self):
        """Test successful lookup_number_service request."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_LOOKUP_NUMBER_RESPONSE):
                result = self.loop.run_until_complete(
                    lookup_number_service(phone_number=TEST_PHONE_NUMBER)
                )
                
                # Verify the response matches our expected mock data
                self.assertEqual(result["number"], TEST_PHONE_NUMBER)
                self.assertEqual(result["service"], "iMessage")
    
    def test_lookup_number_service_error(self):
        """Test error handling in lookup_number_service."""
        with configure_client_mock_error():
            # Patch the make_sendblue_api_request function to raise an HTTPError
            with patch('src.tools.make_sendblue_api_request', side_effect=httpx.HTTPError("Mock HTTP Error")):
                result = self.loop.run_until_complete(
                    lookup_number_service(phone_number=TEST_PHONE_NUMBER)
                )
                
                # Verify error response
                self.assertEqual(result["status"], "ERROR")
                self.assertTrue("error_message" in result)


class TestSendTypingIndicatorTool(unittest.TestCase):
    """Test cases for the send_typing_indicator tool."""
    
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    def tearDown(self):
        self.loop.close()
    
    def test_send_typing_indicator_success(self):
        """Test successful send_typing_indicator request."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_TYPING_INDICATOR_RESPONSE):
                result = self.loop.run_until_complete(
                    send_typing_indicator(to_number=TEST_PHONE_NUMBER)
                )
                
                # Verify the response matches our expected mock data
                self.assertEqual(result["number"], TEST_PHONE_NUMBER)
                self.assertEqual(result["status"], "SENT")
    
    def test_send_typing_indicator_error(self):
        """Test error handling in send_typing_indicator."""
        with configure_client_mock_error():
            # Patch the make_sendblue_api_request function to raise an HTTPError
            with patch('src.tools.make_sendblue_api_request', side_effect=httpx.HTTPError("Mock HTTP Error")):
                result = self.loop.run_until_complete(
                    send_typing_indicator(to_number=TEST_PHONE_NUMBER)
                )
                
                # Verify error response
                self.assertEqual(result["status"], "ERROR")
                self.assertTrue("error_message" in result)


class TestGetMessageHistoryTool(unittest.TestCase):
    """Test cases for the get_message_history tool."""
    
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    def tearDown(self):
        self.loop.close()
    
    def test_get_message_history_success(self):
        """Test successful get_message_history request."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_GET_MESSAGES_RESPONSE):
                result = self.loop.run_until_complete(
                    get_message_history(contact_phone_number=TEST_PHONE_NUMBER)
                )
                
                # Verify the response matches our expected mock data (list of messages)
                self.assertTrue(isinstance(result, list))
                self.assertEqual(len(result), 2)
                self.assertEqual(result[0]["number"], TEST_PHONE_NUMBER)
                self.assertEqual(result[0]["content"], "Test message 1")
    
    def test_get_message_history_with_params(self):
        """Test get_message_history with additional parameters."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_GET_MESSAGES_RESPONSE):
                result = self.loop.run_until_complete(
                    get_message_history(
                        contact_phone_number=TEST_PHONE_NUMBER,
                        limit=10,
                        offset=5,
                        from_date="2023-06-15 12:00:00"
                    )
                )
                
                # Verify the response matches our expected mock data
                self.assertTrue(isinstance(result, list))
                self.assertEqual(len(result), 2)
    
    def test_get_message_history_error(self):
        """Test error handling in get_message_history."""
        with configure_client_mock_error():
            # Patch the make_sendblue_api_request function to raise an HTTPError
            with patch('src.tools.make_sendblue_api_request', side_effect=httpx.HTTPError("Mock HTTP Error")):
                result = self.loop.run_until_complete(
                    get_message_history(contact_phone_number=TEST_PHONE_NUMBER)
                )
                
                # Verify error response (should be a list with one error item)
                self.assertTrue(isinstance(result, list))
                self.assertEqual(len(result), 1)
                self.assertEqual(result[0]["status"], "ERROR")


class TestAddRecipientToGroupTool(unittest.TestCase):
    """Test cases for the add_recipient_to_group tool."""
    
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    def tearDown(self):
        self.loop.close()
    
    def test_add_recipient_to_group_success(self):
        """Test successful add_recipient_to_group request."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_ADD_RECIPIENT_RESPONSE):
                result = self.loop.run_until_complete(
                    add_recipient_to_group(
                        group_id=TEST_GROUP_ID,
                        recipient_number=TEST_PHONE_NUMBER
                    )
                )
                
                # Verify the response matches our expected mock data
                self.assertEqual(result["status"], "SUCCESS")
                self.assertTrue(TEST_PHONE_NUMBER in result["message"])
                self.assertTrue(TEST_GROUP_ID in result["message"])
    
    def test_add_recipient_to_group_error(self):
        """Test error handling in add_recipient_to_group."""
        with configure_client_mock_error():
            # Patch the make_sendblue_api_request function to raise an HTTPError
            with patch('src.tools.make_sendblue_api_request', side_effect=httpx.HTTPError("Mock HTTP Error")):
                result = self.loop.run_until_complete(
                    add_recipient_to_group(
                        group_id=TEST_GROUP_ID,
                        recipient_number=TEST_PHONE_NUMBER
                    )
                )
                
                # Verify error response
                self.assertEqual(result["status"], "ERROR")
                self.assertTrue("error_message" in result)


class TestUploadMediaForSendingTool(unittest.TestCase):
    """Test cases for the upload_media_for_sending tool."""
    
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    def tearDown(self):
        self.loop.close()
    
    def test_upload_media_for_sending_success(self):
        """Test successful upload_media_for_sending request."""
        with configure_client_mock_success():
            # Patch the make_sendblue_api_request function
            with patch('src.tools.make_sendblue_api_request', return_value=MOCK_UPLOAD_MEDIA_RESPONSE):
                result = self.loop.run_until_complete(
                    upload_media_for_sending(media_file_url=TEST_MEDIA_URL)
                )
                
                # Verify the response matches our expected mock data
                self.assertEqual(result["status"], "OK")
                self.assertEqual(result["message"], "File uploaded successfully")
                self.assertTrue("mediaObjectId" in result)
    
    def test_upload_media_for_sending_error(self):
        """Test error handling in upload_media_for_sending."""
        with configure_client_mock_error():
            # Patch the make_sendblue_api_request function to raise an HTTPError
            with patch('src.tools.make_sendblue_api_request', side_effect=httpx.HTTPError("Mock HTTP Error")):
                result = self.loop.run_until_complete(
                    upload_media_for_sending(media_file_url=TEST_MEDIA_URL)
                )
                
                # Verify error response
                self.assertEqual(result["status"], "ERROR")
                self.assertTrue("error_message" in result)


if __name__ == "__main__":
    unittest.main()