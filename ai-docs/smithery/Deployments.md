Deployments
Smithery Deployments allow you to host your MCP server on Smithery served over streamable HTTP connection.
Overview
Deploying on Smithery is straightforward:

Add your server to Smithery (or claim it if it's already listed)
Click Deploy on Smithery Deployments tab on your server page (only authenticated server owners can see this tab)

That's it! Your MCP server will be built and deployed according to your project configuration.
Supported Transports
We are able to host MCP servers that use the streamable HTTP and the stdio transport based on the type defined in your project configuration.
HTTP
This is the native and recommended way to deploy your server on Smithery.
We provide an SDK in TypeScript to help you create a Smithery-compatible HTTP server.
If you prefer to implement the server yourself without using our SDK, you should follow the streamable HTTP specification and use MCP's official language-specific SDK.
There are a few Smithery-specified details you should be aware of:

The /mcp endpoint MUST be available and will be used to process GET, POST and DELETE requests as part of the streamable HTTP specification.
If your server requires configuration, we MUST pass the configuration object to your server as a query parameter: /mcp?config={...} in base64 encoding.

STDIO
This is deprecated.
We highly recommend using HTTP servers over STDIO servers for better performance and future proofing for OAuth support. If you deploy a STDIO server, we will wrap your server and proxy it over HTTP for you.
Serverless Hosting
We serve your hosted MCP servers on Smithery over streamable HTTP in a serverless environment. Connections to stateful servers will timeout after 2 minutes of inactivity.
You will need to handle reconnection at the client if needed.
You should design your server with ephemeral storage in mind.
Persistent data should be stored in an external database.
Tool Lists
Smithery can only display tool lists for servers that don't require authentication to list tools. Server developers must ensure that the list tools functionality is not dependent on any API keys or configurations that users have to provide.
As a server developer, you can implement this by supporting "lazy loading" - only authenticating using your required configuration/API keys upon tool call, rather than upon initialization or tool listing.