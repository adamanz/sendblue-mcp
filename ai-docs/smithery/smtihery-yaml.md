smithery.yaml Reference
The smithery.yaml file provides configuration for your Model Context Protocol (MCP) server on Smithery. This file must be placed in your repository root.
Configuration Options
startCommand
Type: Object (Required)
Defines how to start your MCP server. The structure varies based on the server type you're using.
Smithery supports two types of MCP servers: HTTP and STDIO. Choose the appropriate configuration based on your server implementation.
HTTP Server Configuration
yamlCopystartCommand:
  type: http
  configSchema: object
PropertyTypeDescriptiontypestringMust be set to "http" for HTTP-based MCP serversconfigSchemaobjectJSON Schema defining the configuration options for your server. Smithery uses this to validate user configurations before starting your server.
With HTTP servers, Smithery will start your application and route MCP traffic to the /mcp endpoint under the provided PORT environment variable. Your server needs to implement the Streamable HTTP protocol and handle configuration objects passed via the query parameter.
Example HTTP Configuration:
yamlCopystartCommand:
  type: http
  configSchema:
    type: object
    required: ["apiKey"]
    properties:
      apiKey:
        type: string
        title: "API Key"
        description: "Your API key"
      temperature:
        type: number
        default: 0.7
        minimum: 0
        maximum: 1
We recommend using our TypeScript SDK to create HTTP-based MCP servers.
STDIO Server Configuration
yamlCopystartCommand:
  type: stdio
  configSchema: object
  commandFunction: string
PropertyTypeDescriptiontypestringMust be set to "stdio" for standard I/O based MCP serversconfigSchemaobjectJSON Schema defining the configuration options for your server. Smithery uses this to validate user configurations before starting your server.commandFunctionstringA JavaScript function that returns the command, arguments and environment variables required to start your server. See details below.
commandFunction Details
This JavaScript function receives a validated config object and must return an object with the following properties:
jsCopy(config) => ({
  command: string, // The command to execute
  args: string[],  // Array of command arguments
  env: object      // Environment variables as key-value pairs
})
You can trust that the config parameter conforms to your defined configSchema.
build (Optional)
Type: Object
Contains build configuration options for your server.
yamlCopybuild:
  dockerfile: string
  dockerBuildPath: string
PropertyTypeDescriptiondockerfilestringPath to Dockerfile, relative to the smithery.yaml filedockerBuildPathstringPath to docker build context, relative to the smithery.yaml file
Examples
Next Steps

Configure your Dockerfile
Deploy your server
Monitor your server
