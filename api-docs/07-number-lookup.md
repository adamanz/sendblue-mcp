[Skip to main content](https://docs.sendblue.com/docs/lookup-api/#__docusaurus_skipToContent_fallback)

On this page

The Sendblue API allows you to call an endpoint to figure out if a number supports iMessage. This is pretty useful to determine:

- Whether a certain phone number is an iPhone or not
- If a number is real before sending a message
- Whether to use Sendblue or another provider to send a message

## Usage [​](https://docs.sendblue.com/docs/lookup-api/\#usage "Direct link to Usage")

The lookup-api (formerly called evaluate-service) endpoint is a GET request to the following URL:

`https://api.sendblue.co/api/evaluate-service?number=+19999999999`

This endpoint is authenticated, so you must pass in your [credentials](https://docs.sendblue.com/docs/credentials/). It is available on the Sapphire plan and above.

### Request Parameters [​](https://docs.sendblue.com/docs/lookup-api/\#request-parameters "Direct link to Request Parameters")

| parameter | type | description |
| --- | --- | --- |
| number | string | The number you want to evaluate in E.164 format |

### Response [​](https://docs.sendblue.com/docs/lookup-api/\#response "Direct link to Response")

The response comes back as JSON with the following fields:

| field | type | description |
| --- | --- | --- |
| number | string | The number you evaluated in E.164 format |
| service | string | The service the number supports. Can be `iMessage` or `SMS` |

\`

- [Usage](https://docs.sendblue.com/docs/lookup-api/#usage)
  - [Request Parameters](https://docs.sendblue.com/docs/lookup-api/#request-parameters)
  - [Response](https://docs.sendblue.com/docs/lookup-api/#response)