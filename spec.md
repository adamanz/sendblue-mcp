**MCP Server Specification: Sendblue API Integration**


**1. Overview**

This document outlines the specifications for an MCP server that acts as an interface to the Sendblue API. The server will expose Sendblue's functionalities as a set of tools that an LLM can utilize to send messages, manage groups, and perform other communication-related tasks via iMessage and SMS.

**2. Target Audience**

This specification is intended for an LLM or a development team responsible for implementing the MCP server.

**3. General Requirements**

*   The server MUST interact with the Sendblue API endpoints as documented.
*   All API requests to Sendblue MUST be authenticated using `sb-api-key-id` and `sb-api-secret-key`. These credentials should be securely managed by the MCP server and NOT be parameters of the MCP tools.
*   The server MUST handle potential errors from the Sendblue API gracefully and return informative error messages to the MCP client (the LLM).
*   Phone numbers MUST be handled in E.164 format where specified by the Sendblue API.
*   All POST request bodies to Sendblue should use `Content-Type: application/json`.

**4. Authentication with Sendblue API**

The MCP server will need to be configured with:
*   `SB_API_KEY_ID`: Your Sendblue API Key ID.
*   `SB_API_SECRET_KEY`: Your Sendblue API Secret Key.

These credentials must be included in the headers of every request to the Sendblue API:
*   `sb-api-key-id: YOUR_SB_API_KEY_ID`
*   `sb-api-secret-key: YOUR_SB_API_SECRET_KEY`

**5. MCP Tool Specifications**

The following tools should be implemented:

---

**5.1 Tool: `send_message`**

*   **Description:** Sends a message (iMessage or SMS) to a single recipient. Can include text, media (image or Apple voice note), and expressive send styles.
*   **Sendblue API Endpoint:** `POST https://api.sendblue.co/api/send-message`
*   **Parameters (for the MCP tool, to be translated into the Sendblue JSON body):**
    | Parameter Name      | Type                  | Required? | Default | Description                                                                                                |
    | :------------------ | :-------------------- | :-------- | :------ | :--------------------------------------------------------------------------------------------------------- |
    | `to_number`         | `str`                 | Yes       |         | The E.164 formatted phone number of the recipient.                                                         |
    | `content`           | `str`                 | Yes (if no `media_url`) |         | The text content of the message.                                                                           |
    | `from_number`       | `Optional[str]`       | No        | `None`  | The E.164 formatted Sendblue number to send the message from. (Sendblue may assign one if not provided).     |
    | `media_url`         | `Optional[str]`       | No        | `None`  | Publicly accessible URL of an image or a `.caf` voice note file. Max file size 5MB. Not for signed URLs.      |
    | `send_style`        | `Optional[str]`       | No        | `None`  | Expressive style for iMessage (e.g., "invisible", "fireworks", "slam"). See Sendblue docs for full list. |
    | `status_callback`   | `Optional[str]`       | No        | `None`  | Webhook URL for message status updates (queued, failed, sent, delivered, read).                            |
*   **Returns:** `dict`
    *   A dictionary representing the Sendblue API response, typically including:
        *   `status: str` (e.g., "QUEUED")
        *   `message_handle: str` (Unique Sendblue message identifier)
        *   `from_number: str`
        *   `to_number: str`
        *   `content: str`
        *   `error_message: Optional[str]` (If an error occurred)
        *   Other fields as returned by Sendblue.

---

**5.2 Tool: `send_group_message`**

*   **Description:** Sends a message to a group of recipients. If the group does not exist (based on the list of numbers), it will be created. Can also message an existing group using its `group_id`. Supports text, media, and expressive styles.
*   **Sendblue API Endpoint:** `POST https://api.sendblue.co/api/send-group-message`
*   **Parameters (for the MCP tool, to be translated into the Sendblue JSON body):**
    | Parameter Name      | Type                  | Required? | Default | Description                                                                                                |
    | :------------------ | :-------------------- | :-------- | :------ | :--------------------------------------------------------------------------------------------------------- |
    | `to_numbers`        | `Optional[list[str]]` | Conditional | `None`  | Array of E.164 formatted phone numbers for group recipients (max 25). Required if `group_id` is not provided. |
    | `group_id`          | `Optional[str]`       | Conditional | `None`  | UUID of an existing group. Required if `to_numbers` is not provided.                                       |
    | `content`           | `str`                 | Yes (if no `media_url`) |         | The text content of the message.                                                                           |
    | `from_number`       | `Optional[str]`       | No        | `None`  | The E.164 formatted Sendblue number to send the message from.                                                |
    | `media_url`         | `Optional[str]`       | No        | `None`  | Publicly accessible URL to media.                                                                          |
    | `send_style`        | `Optional[str]`       | No        | `None`  | Expressive style for iMessage.                                                                             |
    | `status_callback`   | `Optional[str]`       | No        | `None`  | Webhook URL for message status updates.                                                                      |
*   **Note:** Either `to_numbers` or `group_id` MUST be provided.
*   **Returns:** `dict`
    *   A dictionary representing the Sendblue API response, typically including:
        *   `group_id: str` (UUID of the group, crucial for correlation)
        *   `status: str` (e.g., "QUEUED")
        *   `message_handle: str`
        *   Other fields as returned by Sendblue.

---

**5.3 Tool: `lookup_number_service`**

*   **Description:** Determines if a phone number supports iMessage or SMS. Useful for checking if a number is an iPhone or if it's a real number before sending a message. (Available on Sapphire plan and above).
*   **Sendblue API Endpoint:** `GET https://api.sendblue.co/api/evaluate-service`
*   **Parameters (for the MCP tool):**
    | Parameter Name      | Type  | Required? | Default | Description                                                                |
    | :------------------ | :---- | :-------- | :------ | :------------------------------------------------------------------------- |
    | `phone_number`      | `str` | Yes       |         | The E.164 formatted phone number to evaluate. (Maps to `?number=` query param) |
*   **Returns:** `dict`
    *   Example: `{"number": "+19999999999", "service": "iMessage"}` or `{"service": "SMS"}`

---

**5.4 Tool: `send_typing_indicator`**

*   **Description:** Sends a typing indicator (animated dots) to a recipient. This requires an existing chat where messages have been exchanged recently. Not supported in group chats.
*   **Sendblue API Endpoint:** `POST https://api.sendblue.co/api/send-typing-indicator`
*   **Parameters (for the MCP tool, to be translated into the Sendblue JSON body):**
    | Parameter Name      | Type  | Required? | Default | Description                                                              |
    | :------------------ | :---- | :-------- | :------ | :----------------------------------------------------------------------- |
    | `to_number`         | `str` | Yes       |         | The E.164 formatted phone number to send the typing indicator to.        |
*   **Returns:** `dict`
    *   Example: `{"number": "+19998887777", "status": "SENT" or "ERROR", "error_message": Optional[str]}`

---

**5.5 Tool: `get_message_history`**

*   **Description:** Retrieves message history for the account. Can be filtered by contact (phone number or conversation ID), date, and paginated.
*   **Sendblue API Endpoint:** `GET https://api.sendblue.co/accounts/messages`
*   **Parameters (for the MCP tool, to be translated into Sendblue query parameters):**
    | Parameter Name         | Type            | Required? | Default | Description                                                                 |
    | :--------------------- | :-------------- | :-------- | :------ | :-------------------------------------------------------------------------- |
    | `contact_phone_number` | `Optional[str]` | No        | `None`  | Filter by sender/recipient E.164 phone number. (Maps to `?number=`)         |
    | `conversation_id`      | `Optional[str]` | No        | `None`  | Filter by conversation ID (contact ID). (Maps to `?cid=`)                    |
    | `limit`                | `Optional[int]` | No        | `50`    | Maximum number of messages per request. (Maps to `?limit=`)                   |
    | `offset`               | `Optional[int]` | No        | `0`     | Offset for paginating through messages. (Maps to `?offset=`)                  |
    | `from_date`            | `Optional[str]` | No        | `None`  | Filter messages sent after this date/time (e.g., "2023-06-15 12:00:00"). (Maps to `?from_date=`) |
*   **Returns:** `list[dict]`
    *   A list of message objects. Each message object is a dictionary containing fields like:
        *   `content: Optional[str]`
        *   `media_url: Optional[str]`
        *   `is_outbound: bool`
        *   `status: str`
        *   `date_sent: str` (ISO 8601)
        *   `from_number: str`
        *   `to_number: str`
        *   Other fields as returned by Sendblue.

---

**5.6 Tool: `add_recipient_to_group`**

*   **Description:** Adds a new recipient to an existing group chat.
*   **Sendblue API Endpoint:** `POST https://api.sendblue.co/api/modify-group`
*   **Parameters (for the MCP tool, to be translated into the Sendblue JSON body):**
    | Parameter Name      | Type  | Required? | Default | Description                                                            |
    | :------------------ | :---- | :-------- | :------ | :--------------------------------------------------------------------- |
    | `group_id`          | `str` | Yes       |         | The ID (uuid) of the group to which the recipient will be added.       |
    | `recipient_number`  | `str` | Yes       |         | The E.164 formatted phone number of the recipient to add to the group. |
*   **Note:** The `modify_type` field in the Sendblue API request body for this tool will be hardcoded to `"add_recipient"`.
*   **Returns:** `dict`
    *   A dictionary indicating success or failure. Example: `{"status": "SUCCESS", "message": "Recipient added successfully to group [group_id]"}` or `{"status": "ERROR", "message": "Error details"}`. (The Sendblue docs do not specify the exact response format for this endpoint).

---

**5.7 Tool: `upload_media_for_sending`**

*   **Description:** Uploads a media file from a publicly accessible URL to Sendblue's servers. This is primarily useful for scenarios where the media URL might be temporary (e.g., signed URLs) or to get a Sendblue-hosted media object ID before sending.
*   **Sendblue API Endpoint:** `POST https://api.sendblue.co/api/upload-media-object`
*   **Parameters (for the MCP tool, to be translated into the Sendblue JSON body):**
    | Parameter Name   | Type  | Required? | Default | Description                                   |
    | :--------------- | :---- | :-------- | :------ | :-------------------------------------------- |
    | `media_file_url` | `str` | Yes       |         | The publicly accessible URL of the media file. |
*   **Returns:** `dict`
    *   Example: `{"status": "OK", "message": "File uploaded successfully", "mediaObjectId": "MO_asdasdasdasdasd.jpg"}` or `{"status": "ERROR", "message": "Invalid media URL"}`.

---

**6. General Implementation Notes**

*   **Error Handling:** The MCP server should catch exceptions from the `httpx` library (or whatever HTTP client is used) and Sendblue API error responses. These should be translated into meaningful MCP error responses.
*   **Logging:** Implement logging within the MCP server for requests made to Sendblue and responses received, to aid in debugging.
*   **Media Handling:** For `send_message` and `send_group_message`, if `media_url` points to a `.caf` file, it will be sent as an Apple voice note. Otherwise, it's treated as an image/MMS.
*   **Send Styles:** The `send_style` parameter is only applicable to iMessage. The Sendblue documentation lists possible values: `"celebration"`, `"shooting_star"`, `"fireworks"`, `"lasers"`, `"love"`, `"confetti"`, `"balloons"`, `"spotlight"`, `"echo"`, `"invisible"`, `"gentle"`, `"loud"`, `"slam"`. These should be documented for the LLM.

**7. Future Considerations / Sendblue Roadmap**

The Sendblue API documentation indicates the following group management features are "Scheduled" or "In progress":
*   Removing people from groups (`modify_type: "remove_recipient"`)
*   Changing group names (`modify_type: "rename"`)
*   Leaving groups (`modify_type: "leave"`)

Once these features are fully supported by Sendblue, corresponding MCP tools should be created (e.g., `remove_recipient_from_group`, `rename_group_chat`, `leave_group_chat`).

**8. Todo List for Implementation**

1.  **Set up MCP Server Base:** Initialize a FastMCP server project.
2.  **Secure Credential Management:** Implement a secure way to load and store `SB_API_KEY_ID` and `SB_API_SECRET_KEY`.
3.  **HTTP Client:** Choose and configure an HTTP client library (e.g., `httpx`) for making requests to Sendblue.
4.  **Implement Tool `send_message`:**
    *   Map MCP parameters to Sendblue JSON body.
    *   Handle API call and response.
5.  **Implement Tool `send_group_message`:**
    *   Handle conditional logic for `to_numbers` vs `group_id`.
    *   Map MCP parameters to Sendblue JSON body.
    *   Handle API call and response.
6.  **Implement Tool `lookup_number_service`:**
    *   Map MCP parameter to Sendblue GET query parameter.
    *   Handle API call and response.
7.  **Implement Tool `send_typing_indicator`:**
    *   Map MCP parameter to Sendblue JSON body.
    *   Handle API call and response.
8.  **Implement Tool `get_message_history`:**
    *   Map MCP parameters to Sendblue GET query parameters.
    *   Handle API call and response, ensuring proper list[dict] structure.
9.  **Implement Tool `add_recipient_to_group`:**
    *   Map MCP parameters to Sendblue JSON body, hardcoding `modify_type`.
    *   Handle API call and response.
10. **Implement Tool `upload_media_for_sending`:**
    *   Map MCP parameter to Sendblue JSON body.
    *   Handle API call and response.
11. **Comprehensive Error Handling:** For each tool, implement logic to catch common Sendblue API errors and HTTP errors, returning structured error messages.
12. **Input Validation:** Add Pydantic models or other validation for tool inputs (e.g., E.164 format, URL validity).
13. **Unit Tests:** Write unit tests for each tool, mocking Sendblue API responses (both success and error cases).
14. **Documentation:** Document the MCP server's tools for LLM consumption, including descriptions, parameters, and example return values.

---