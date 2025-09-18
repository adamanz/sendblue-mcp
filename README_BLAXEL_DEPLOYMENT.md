# Blaxel Deployment Guide for Sendblue MCP Server

## Overview
This guide explains how to deploy the Sendblue MCP server to Blaxel's serverless infrastructure.

## Prerequisites
1. Blaxel CLI installed (`bl` command)
2. Logged into your Blaxel workspace
3. Sendblue API credentials

## Configuration Files

### blaxel.toml
The main configuration file for Blaxel deployment. Already configured with:
- Function name: `sendblue-mcp-blaxel`
- Workspace: `simple`
- HTTP trigger at `/functions/sendblue-mcp`
- Private authentication (requires API keys)

### server.py
The main entrypoint for the Blaxel deployment that:
- Initializes the MCP server
- Registers all Sendblue tools
- Runs on HTTP transport for serverless

## Setting Up API Credentials

### Option 1: Using Environment File (Recommended for deployment)

1. Copy the example environment file:
```bash
cp .env.blaxel .env
```

2. Edit `.env` and add your actual Sendblue credentials:
```
SENDBLUE_API_KEY_ID=your_actual_api_key_id
SENDBLUE_API_SECRET_KEY=your_actual_api_secret_key
```

3. Deploy with the environment file:
```bash
bl deploy -e .env
```

### Option 2: Using Secrets During Deploy

Deploy with secrets directly:
```bash
bl deploy -s SENDBLUE_API_KEY_ID=your_key_id -s SENDBLUE_API_SECRET_KEY=your_secret_key
```

### Option 3: Create a Deployment Manifest

Create a file `deployment.yaml`:
```yaml
apiVersion: blaxel.ai/v1alpha1
kind: Function
metadata:
  name: sendblue-mcp-blaxel
  workspace: simple
spec:
  env:
    SENDBLUE_API_KEY_ID: "your_key_id"
    SENDBLUE_API_SECRET_KEY: "your_secret_key"
```

Then apply:
```bash
bl apply -f deployment.yaml
```

## Deployment Steps

1. **Initial Deployment** (already done):
```bash
bl deploy
```

2. **Update with Credentials**:
```bash
# After setting up your .env file
bl deploy -e .env
```

3. **Check Deployment Status**:
```bash
bl get function sendblue-mcp-blaxel
```

4. **View Logs**:
```bash
bl logs function sendblue-mcp-blaxel
```

## Endpoint Information

Once deployed, your MCP server will be available at:
- **URL**: https://app.blaxel.ai/simple/global-agentic-network/function/sendblue-mcp-blaxel
- **Protocol**: HTTP/WebSocket for MCP
- **Authentication**: Private (requires proper authentication headers)

## Testing the Deployment

You can test the deployed MCP server by:
1. Using an MCP client that supports HTTP transport
2. Connecting via WebSocket to the deployed endpoint
3. Providing proper authentication

## Troubleshooting

### Missing Credentials Error
If you see "SENDBLUE_API_KEY_ID is not set" in logs:
1. Ensure you've set the environment variables correctly
2. Redeploy with the `-e .env` flag
3. Check that the .env file contains valid credentials

### Connection Issues
1. Verify the function is running: `bl get function sendblue-mcp-blaxel`
2. Check logs for errors: `bl logs function sendblue-mcp-blaxel`
3. Ensure authentication is properly configured

## Updating the Deployment

To update the deployment with new code:
1. Make your code changes
2. Commit to git
3. Run `bl deploy` or `bl deploy -e .env` (if updating with credentials)

## Support

For Blaxel-specific issues, refer to the Blaxel documentation or support.
For Sendblue MCP server issues, check the main README.md file.