# Sendblue API Documentation

This directory contains documentation for the Sendblue API, which allows for programmatic sending and receiving of iMessages and SMS.

## Contents

- [Outbound Messages](./outbound_messages.md) - How to send SMS and iMessages to individual recipients
- [Inbound Messages](./inbound_messages.md) - How to receive messages via webhooks
- [Group Messaging](./group_messaging.md) - How to send and manage group messages
- [Retrieve Messages](./retrieve_messages.md) - How to retrieve message history
- [Media Objects](./media_objects.md) - How to upload media files for sending
- [Expressive Messages](./expressive_messages.md) - How to send messages with special visual effects
- [Number Lookup](./number_lookup.md) - How to check if a number supports iMessage
- [Voice Notes](./voice_notes.md) - How to send Apple voice notes
- [Typing Indicators](./typing_indicators.md) - How to send typing indicators
- [Python Client Library](./python_client_library.txt) - Documentation for the Sendblue Python client

## Authentication

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

For account-related endpoints:

```
https://api.sendblue.co/accounts
```