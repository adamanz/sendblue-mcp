# Integrating Sendblue MCP Server with Claude Clients

This document provides instructions on how to integrate the Sendblue MCP server with Claude Desktop and Cursor.

## Claude Desktop Integration

Claude Desktop allows you to configure MCP servers that can be used in conversations with Claude. Here's how to set up the Sendblue MCP server:

### Prerequisites

1. Make sure you have [Claude Desktop](https://claude.ai/download) installed and up to date
2. Set up your Sendblue MCP server locally or have it running in a container

### Configuration Steps

1. Locate the Claude Desktop configuration file at:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%AppData%\Claude\claude_desktop_config.json`

2. Create or edit the configuration file with a text editor:
   ```bash
   # macOS
   mkdir -p ~/Library/Application\ Support/Claude/
   touch ~/Library/Application\ Support/Claude/claude_desktop_config.json
   
   # Or with VS Code
   code ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

3. Add the Sendblue MCP server configuration:
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

   Replace `/absolute/path/to/sendblue-mcp` with the absolute path to your Sendblue MCP server directory.

4. Save the file and restart Claude Desktop.

5. After restarting, you should see MCP tools available in the Claude interface when you click on the hammer icon.

### Troubleshooting Claude Desktop Integration

If the MCP server doesn't appear in Claude Desktop:

1. Check Claude's logs:
   ```bash
   # View most recent MCP-related logs
   tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
   ```

2. Make sure your `.env` file is properly configured with Sendblue API credentials
3. Verify the path in the config file is absolute and correct
4. Try restarting Claude Desktop completely

## Cursor Integration

[Cursor](https://cursor.sh/) is an AI-powered code editor that can integrate with MCP servers for enhanced functionality:

### Prerequisites

1. Install [Cursor](https://cursor.sh/download)
2. Have your Sendblue MCP server running

### Configuration Steps

1. Open Cursor and go to Settings:
   - Click on the gear icon in the lower left corner or use the keyboard shortcut `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux)

2. Navigate to "Extensions" > "AI" > "MCP Servers"

3. Click "Add Server" and enter the following details:
   - **Server Name**: `sendblue`
   - **Command**: `python -m src.main`
   - **Working Directory**: `/absolute/path/to/sendblue-mcp`

4. Save the configuration and restart Cursor.

5. When using Cursor's AI features, you can now choose to invoke the Sendblue MCP Server's tools.

### Using with Cursor

1. Use the Cursor AI panel to interact with Claude
2. Access Sendblue tools by typing commands like:
   - "Send a message to +19998887777 saying 'Hello from Cursor!'"
   - "Show me my recent message history"

3. The AI will utilize the MCP tools to perform the requested actions, prompting you for any required Sendblue API credentials if they're not already configured.

## Environment Variables

For both Claude Desktop and Cursor integrations, you need to ensure the environment variables for Sendblue API credentials are properly set:

1. Create a `.env` file in the root of your Sendblue MCP server directory:
   ```
   SENDBLUE_API_KEY_ID=your_api_key_id
   SENDBLUE_API_SECRET_KEY=your_api_secret_key
   ```

2. Alternatively, set these environment variables in your system profile.

## Docker Integration

If you're running your Sendblue MCP server in a Docker container, you can configure Claude Desktop and Cursor to connect to it. Update the configuration to use the Docker command:

```json
{
   "mcpServers": {
      "sendblue": {
         "command": "docker",
         "args": [
            "run",
            "--rm",
            "-p", "5000:5000",
            "--env-file", "/path/to/your/.env",
            "sendblue-mcp"
         ]
      }
   }
}
```

## Common Issues

1. **MCP Tools Not Showing Up**:
   - Verify the server is properly configured
   - Check Claude logs for errors
   - Ensure the MCP server is running with the correct transport mode

2. **Authentication Errors**:
   - Make sure your Sendblue API credentials are correctly set in the `.env` file
   - Verify the credentials have the correct permissions in your Sendblue account

3. **Connection Issues**:
   - For HTTP transport, ensure the port specified is available
   - For STDIO transport, ensure the command path is correct

4. **MCP Response Timeouts**:
   - Increase the timeout value in the MCP server configuration if available
   - Check for network connectivity issues to the Sendblue API