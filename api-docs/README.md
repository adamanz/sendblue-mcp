# Sendblue API Documentation

This directory contains documentation for the Sendblue API, which allows you to send and receive iMessages and SMS programmatically.

## Contents

1. [Outbound Messages](./01-outbound-messages.md) - How to send messages to individuals
2. [Inbound Messages](./02-inbound-messages.md) - How to receive messages via webhooks
3. [Group Messaging](./03-group-messaging.md) - How to send and manage group messages
4. [Message Retrieval](./04-message-retrieval.md) - How to retrieve sent or received messages
5. [Media Uploads](./05-media-uploads.md) - How to upload media objects for messages
6. [Expressive Messages](./06-expressive-messages.md) - How to send messages with special effects
7. [Number Lookup](./07-number-lookup.md) - How to check if a number supports iMessage
8. [Voice Notes](./08-voice-notes.md) - How to send voice notes via iMessage
9. [Typing Indicators](./09-typing-indicators.md) - How to send typing indicators
10. [Python Client](./10-python-client.txt) - Details of the Python client library

## API Authentication

All Sendblue API endpoints require authentication with your API Key and API Secret, which must be included in the request headers:

```
sb-api-key-id: YOUR_SB_API_KEY_ID
sb-api-secret-key: YOUR_SB_API_SECRET_KEY
```

## Base URL

All API requests should be made to the following base URL:

```
https://api.sendblue.co/api
```