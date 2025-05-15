[Skip to main content](https://docs.sendblue.com/docs/typing-indicator/#__docusaurus_skipToContent_fallback)

On this page

The Sendblue API allows you to call an endpoint to send an indication that you are typing. This shows up on the end users device as the three dots that animate, which is useful for different kinds of applications:

- For chatbots: Indicate that the bot is thinking/processing information
- For customer support: Indicate that a support agent is typing
- For any other use-case where you want to indicate that the user should expect an answer soon, increasing the likelihood that they will remain in the chat

## Usage [​](https://docs.sendblue.com/docs/typing-indicator/\#usage "Direct link to Usage")

The typing indicator api is only available when a chat already exists with a user, and only when messages have been exchanged recently. Furthermore, typing indicators are not supported in group chats at this time.

The endpoint for this API is a POST request to the following URL:

`https://api.sendblue.co/api/send-typing-indicator?number=+19999999999`

This endpoint is authenticated, so you must pass in your [credentials](https://docs.sendblue.com/docs/credentials/).

Here is an example using cURL:

```codeBlockLines_e6Vv
curl --location --request POST 'https://api.sendblue.co/api/send-typing-indicator' \
--header 'sb-api-key-id: YOUR_SB_API_KEY_ID' \
--header 'sb-api-secret-key: YOUR_SB_API_SECRET_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "number": "+19998887777"
}'

```

### Request Parameters [​](https://docs.sendblue.com/docs/typing-indicator/\#request-parameters "Direct link to Request Parameters")

| parameter | type | description |
| --- | --- | --- |
| number | string | The number you want to send a typing indicator to |

### Response [​](https://docs.sendblue.com/docs/typing-indicator/\#response "Direct link to Response")

The response comes back as JSON with the following fields:

| field | type | description |
| --- | --- | --- |
| number | string | The number you evaluated in E.164 format |
| status | string | The status of the typing indicator you tried to send (this will either be SENT or ERROR) |
| error\_message | string | The error message if the status is ERROR |

The typing indicator is sent on a "best effort" basis. Sometimes, a typing indicator is unable to be sent due to the last message having been too long ago, or the recipient number being iMessage. In these cases you will still se a 'SENT' status, but the typing indicator will not be delivered.

- [Usage](https://docs.sendblue.com/docs/typing-indicator/#usage)
  - [Request Parameters](https://docs.sendblue.com/docs/typing-indicator/#request-parameters)
  - [Response](https://docs.sendblue.com/docs/typing-indicator/#response)