[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/adamanz-sendblue-mcp-badge.png)](https://mseep.ai/app/adamanz-sendblue-mcp)

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

## Quick Start

### Fastest Way to Get Started

#### For Claude Desktop
```sh
# Clone the repository
git clone https://github.com/your-username/sendblue-mcp.git
cd sendblue-mcp

# Install dependencies
pip install -r requirements.txt

# Set up credentials
cp sample.env .env
# Edit .env and add your API credentials

# Add to Claude Desktop config (macOS)
echo '{
  "mcpServers": {
    "sendblue": {
      "command": "python",
      "args": ["-m", "src.main"],
      "cwd": "'$(pwd)'"
    }
  }
}' > ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Restart Claude Desktop
```

#### For Local Testing
```sh
# After cloning and installing dependencies
python start_sendblue.py
```

## Setup

### Prerequisites

- Python 3.10 or higher
- Sendblue API credentials (API Key ID and Secret Key)

### Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/sendblue-mcp.git
   cd sendblue-mcp
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure your Sendblue API credentials:
   ```sh
   cp sample.env .env
   # Edit .env to add your API credentials
   ```

   Open `.env` and add:
   ```
   SENDBLUE_API_KEY_ID=your_api_key_id_here
   SENDBLUE_API_SECRET_KEY=your_api_secret_key_here
   ```

### Running Locally

1. Ensure you're in the project directory:
   ```sh
   cd /path/to/sendblue-mcp
   ```

2. Run the server:
   ```sh
   python -m src.main
   ```

   Or use the convenience script:
   ```sh
   python start_sendblue.py
   ```

   The server will start using the configuration from your `.env` file.

## Client Integration

### Claude Desktop Integration

Claude Desktop allows you to use the Sendblue MCP server directly from the Claude interface:

1. Locate the Claude Desktop configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%AppData%\Claude\claude_desktop_config.json`

2. Create or edit the file and add the following configuration:
   ```json
   {
      "mcpServers": {
         "sendblue": {
            "command": "python",
            "args": [
               "-m",
               "src.main",
               "--directory",
               "/absolute/path/to/sendblue-mcp"
            ]
         }
      }
   }
   ```

3. Replace `/absolute/path/to/sendblue-mcp` with the actual path to your Sendblue MCP server directory
4. Save the file and restart Claude Desktop
5. The Sendblue tools will appear in the Claude interface when you click on the hammer icon

### Cursor Integration

To add the Sendblue MCP server to Cursor:

1. Open Cursor Settings:
   - **macOS**: Press `Cmd + ,`
   - **Windows/Linux**: Press `Ctrl + ,`

2. Navigate to the MCP settings:
   - Go to "Features" > "MCP Servers"

3. Click "Add Server" and configure:
   - **Server Name**: `sendblue`
   - **Command**: `python`
   - **Args**: `["-m", "src.main"]`
   - **Working Directory**: `/absolute/path/to/sendblue-mcp`
   - **Environment Variables**:
     ```json
     {
       "SENDBLUE_API_KEY_ID": "your_api_key_id",
       "SENDBLUE_API_SECRET_KEY": "your_api_secret_key"
     }
     ```

4. Save and restart Cursor

5. Verify the server is connected:
   - Open the AI chat
   - You should see Sendblue tools available when you click the tools icon
   - Try running `@sendblue send test message` to confirm it's working

### Troubleshooting Integration

If the MCP server doesn't appear in Claude Desktop:

1. Check Claude's logs (macOS): `tail -n 20 -f ~/Library/Logs/Claude/mcp*.log`
2. Verify your `.env` file has valid Sendblue API credentials
3. Make sure the path in the config file is absolute and correct
4. Try restarting the client application completely

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

### Obtaining Sendblue API Keys

1. Sign up for a Sendblue account at [https://sendblue.co/](https://sendblue.co/)
2. Once logged in, navigate to the API dashboard
3. Generate your API Key ID and API Secret Key
4. Store these credentials securely as they will be needed to authenticate with the Sendblue API

### Setting Up Credentials

The server requires two main API credentials:

- **SENDBLUE_API_KEY_ID**: Your Sendblue API Key ID
- **SENDBLUE_API_SECRET_KEY**: Your Sendblue API Secret Key

These can be provided in any of the following ways:

#### 1. Using a .env File (Local Development)

Create a `.env` file in the root directory with your credentials:

```
SENDBLUE_API_KEY_ID=your_api_key_id_here
SENDBLUE_API_SECRET_KEY=your_api_secret_key_here
MCP_TRANSPORT=stdio  # or http for web transport
```

#### 2. For Claude Desktop Integration

When using with Claude Desktop, you can also set these environment variables in your system profile or pass them directly in the Claude Desktop configuration file:

```json
{
   "mcpServers": {
      "sendblue": {
         "command": "python",
         "args": [
            "-m",
            "src.main"
         ],
         "env": {
            "SENDBLUE_API_KEY_ID": "your_api_key_id_here",
            "SENDBLUE_API_SECRET_KEY": "your_api_secret_key_here"
         }
      }
   }
}
```

#### 3. For Smithery Deployment

When deploying to Smithery, you'll be prompted to input these environment variables through the Smithery interface. The deployment will securely store these values and provide them to your server at runtime.

## Configuration

Additional configuration is managed through environment variables:

- `MCP_TRANSPORT`: Transport method (`stdio` or `http`); defaults to `stdio`
- `MCP_HTTP_PORT`: Port number for HTTP transport; defaults to `5000`

## Testing

The project includes a comprehensive test suite:

```sh
python -m unittest discover -s tests
```

## Documentation

- [API Documentation](./api-docs/README.md) - Generated documentation for the Sendblue API
- [Sendblue Documentation](./sendblue-docs/README.md) - Original Sendblue API documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.