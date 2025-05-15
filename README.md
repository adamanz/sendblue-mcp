# Sendblue MCP Server

An MCP (Model Context Protocol) server that exposes Sendblue's iMessage and SMS capabilities as tools for LLMs.

## Overview

This MCP server acts as an interface to the Sendblue API, enabling LLMs to send messages, manage groups, and perform other communication-related tasks via iMessage and SMS. It follows the MCP specification and provides a standardized way for LLMs to interact with the Sendblue platform.

## Features

The server provides the following tools:

- `send_message`: Send individual messages (iMessage/SMS) with support for text, media, and expressive styles
- `send_group_message`: Send messages to group chats
- `lookup_number_service`: Check if a number supports iMessage or SMS
- `send_typing_indicator`: Send typing indicators to recipients
- `get_message_history`: Retrieve message history
- `add_recipient_to_group`: Add new recipients to existing group chats
- `upload_media_for_sending`: Upload media from URLs to Sendblue servers

## Setup

### Prerequisites

- Python 3.10 or higher
- Sendblue API credentials (API Key ID and Secret Key)

### Installation

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `sample.env` to `.env` and configure your Sendblue API credentials

```sh
cp sample.env .env
nano .env  # Edit with your API credentials
```

### Running Locally

```sh
python -m src.main
```

## Deployment

### Using Docker

Build and run the Docker container:

```sh
docker build -t sendblue-mcp .
docker run -p 5000:5000 --env-file .env sendblue-mcp
```

### Using Smithery

This server is compatible with Smithery hosting. Deploy using:

```sh
smithery deploy
```

## API Credentials

You need to obtain API credentials from Sendblue by signing up at [https://sendblue.co/](https://sendblue.co/).

## Configuration

Configuration is managed through environment variables, which can be set in a `.env` file:

- `SENDBLUE_API_KEY_ID`: Your Sendblue API Key ID
- `SENDBLUE_API_SECRET_KEY`: Your Sendblue API Secret Key
- `MCP_TRANSPORT`: Transport method (`stdio` or `http`); defaults to `stdio`

## License

This project is licensed under the MIT License - see the LICENSE file for details.