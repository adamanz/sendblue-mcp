[Skip to main content](https://docs.sendblue.com/docs/outbound/#__docusaurus_skipToContent_fallback)

On this page

The Sendblue API conforms to REST API standards. Using it, you can send outbound iMessage and SMS to any enabled phone globally. All requests can either be form-encoded or

In this documentation, we will cover how to:

1. [Send iMessages to a destination phone number](https://docs.sendblue.com/docs/outbound/#sending-imessages)
2. [Track the status of your message using webhooks](https://docs.sendblue.com/docs/outbound/#status-callback)

## Sending iMessages [​](https://docs.sendblue.com/docs/outbound/\#sending-imessages "Direct link to Sending iMessages")

You can send a message directly with cURL or by using one of our client libraries by hitting the following endpoint:

`POST https://api.sendblue.co/api/send-message`
Here's what that looks like as a curl request:

```codeBlockLines_e6Vv
curl --location --request POST 'https://api.sendblue.co/api/send-message' \
--header 'sb-api-key-id: YOUR_SB_API_KEY_ID' \
--header 'sb-api-secret-key: YOUR_SB_API_SECRET_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "number": "+19998887777",
    "content": "Hello world!",
    "send_style": "invisible",
    "media_url": "https://picsum.photos/200/300.jpg",
    "status_callback": "https://example.com/message-status/1234abcd"
}'

```

And here's the same in Node.js with Axios

```codeBlockLines_e6Vv
const axios = require("axios");

const url = `https://api.sendblue.co/api/send-message`;

axios
  .post(
    url,
    {
      number: "+19998887777",
      from_number: "+16468528190", // the sendblue number you want to use
      content: "Hello world!",
      send_style: "invisible",
      media_url: "https://picsum.photos/200/300.jpg",
      status_callback: "https://example.com/message-status/1234abcd",
    },
    {
      headers: {
        "sb-api-key-id": "YOUR_SB_API_KEY_ID",
        "sb-api-secret-key": "YOUR_SB_API_SECRET_KEY",
        "content-type": "application/json",
      },
    }
  )
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.error(error);
  });

```

### Request body [​](https://docs.sendblue.com/docs/outbound/\#request-body "Direct link to Request body")

| parameter | type | description |
| --- | --- | --- |
| number | string | The number of the recipient of the message |
| from\_number | string | The number to send the message from |
| content | string | The content of the message |
| send\_style | string | The style of delivery of the message (see [expressive messages](https://docs.sendblue.com/docs/expressive-messages/)) |
| media\_url | string | The URL of the image you want to send |
| status\_callback | string | The URL where you want to receive the status updates of the message |

### Sample response [​](https://docs.sendblue.com/docs/outbound/\#sample-response "Direct link to Sample response")

```codeBlockLines_e6Vv
{
  "accountEmail": "YOUR EMAIL",
  "content": "Hello world!",
  "is_outbound": true,
  "status": "QUEUED",
  "error_code": null,
  "error_message": null,
  "message_handle": "dfd747ba-5600-4a8a-804a-a614a0fbc1c5",
  "date_sent": "2023-09-27T16:35:32.287Z",
  "date_updated": "2023-09-27T16:35:32.703Z",
  "from_number": "+16468528190",
  "number": "+19998887777",
  "to_number": "+19998887777",
  "was_downgraded": null,
  "plan": "dedicated",
  "media_url": "https://picsum.photos/200/300.jpg",
  "message_type": "message",
  "group_id": "",
  "participants": [],
  "send_style": "invisible",
  "opted_out": false,
  "error_detail": null
}

```

## Sending files [​](https://docs.sendblue.com/docs/outbound/\#sending-files "Direct link to Sending files")

You can send images using the `media_url` parameter. This URL should be a CDN link pointing to an image. The URL must end with the proper file extension. We recommend sticking to the standard PascalCase naming convention. So if your image is named "Welcome Image", we recommend uploading it to your CDN as "WelcomeImage.png".

Files are currently capped at **5MB**.

media\_url does not support [signed urls](https://cloud.google.com/storage/docs/access-control/signed-urls#:~:text=about%20request%20signing.-,Overview,specific%20actions%20on%20a%20resource.), please use the [media object](https://docs.sendblue.com/docs/create-media-object/) pattern for that

## Status Callback [​](https://docs.sendblue.com/docs/outbound/\#status-callback "Direct link to Status Callback")

Sendblue will POST the endpoint you provide in `status_callback` whenever the status of a message changes to one of the following:

- queued
- failed
- sent
- delivered
- read

Below is an example of the POST body that is sent to the status\_callback URL for a delivered message:

```codeBlockLines_e6Vv
{
  "accountEmail": "support@sendblue.com",
  "content": "Hello world!",
  "is_outbound": true,
  "status": "DELIVERED",
  "error_code": null,
  "error_message": null,
  "message_handle": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "date_sent": "2020-09-10T06:15:05.962Z",
  "date_updated": "2020-09-10T06:15:14.115Z",
  "from_number": "+15122164639",
  "number": "+19998887777",
  "to_number": "+19998887777",
  "was_downgraded": false,
  "plan": "blue"
}

```

important

You must send a response to our server in order to avoid receiving multiple webhook calls.

## Message Status Resolution [​](https://docs.sendblue.com/docs/outbound/\#message-status-resolution "Direct link to Message Status Resolution")

| Callback Body Field | Type | Description |
| --- | --- | --- |
| accountEmail | `string` | Associated account email |
| content | `string` | Message content |
| is\_outbound | `boolean` | True if message is sent, false if message is received |
| media\_url | `string` | A CDN link to the image that you sent our servers |
| status | `string` | The current status of the message |
| error\_code | `int` | error code (null if no error) |
| error\_message | `string` | descriptive error message (null if no error) |
| message\_handle | `string` | Sendblue message handle |
| date\_sent | `string` | ISO 8601 formatted date string of the date this message was created |
| date\_updated | `string` | ISO 8601 formatted date string of the date this message was last updated |
| from\_number | `string` | E.164 formatted phone number string of the message dispatcher |
| number | `string` | E.164 formatted phone number string of your end-user (not the Sendblue-provided phone number) |
| to\_number | `string` | E.164 formatted phone number string of the message recipient |
| was\_downgraded | `boolean` | true if the end user does not support iMessage, false otherwise |
| plan | `string` | Value of the Sendblue account plan |

### Status [​](https://docs.sendblue.com/docs/outbound/\#status "Direct link to Status")

The status field will report the status. There are currently 7 different possible responses to a send-message request:

| Status | Description |
| --- | --- |
| **QUEUED** | The message has reached our servers, and has passed our validation checks. It has been queued for delivery |
| **SENT** | The message has been sent |
| **DELIVERED** | The message has been sent, and we've received confirmation of delivery (iMessage Only) |
| **READ** | The message has been sent, and we've received confirmation that the end user has read the message (iMessage Only) |
| **ERROR** | The message has failed to send, see the `error_code` field to understaind why |

### Error Codes [​](https://docs.sendblue.com/docs/outbound/\#error-codes "Direct link to Error Codes")

Any Code besides 0 or null is a failure. Some codes are not yet documented.

| Code | Description |
| --- | --- |
| 4000 | Validation Error: see `error_message` field |
| 4001 | Rate Limit Exceeded |
| 4002 | Blacklisted Number (e.g. 911) |
| 5000 | Internal Error |
| 5003 | Server Rate Exceeded |
| 10001 | message failed to send |
| 10002 | failed to resolve message status |

## Limits [​](https://docs.sendblue.com/docs/outbound/\#limits "Direct link to Limits")

Messages sent using Sendblue must be less than 18996 characters in length. If you have larger requirements we recommend breaking the message up into several, smaller messages.

## Useful Information [​](https://docs.sendblue.com/docs/outbound/\#useful-information "Direct link to Useful Information")

### From Number [​](https://docs.sendblue.com/docs/outbound/\#from-number "Direct link to From Number")

caution

Sendblue focuses on message deliverability and end-user experience. This means that each of your users will only ever interact with your business through one Sendblue phone number. However, different clients may see different numbers for texts sent from your company. See [Limits & Queues](https://docs.sendblue.com/docs/message-limits/) for more info

The from\_number field is given as a convenience to you, in case you want to keep track of that info, or tell the client that they should expect a text from the number that you show them.

### Handle [​](https://docs.sendblue.com/docs/outbound/\#handle "Direct link to Handle")

The message handle is used so that you can query the status of each message at a later date. This is especially useful in high volume message\_status=QUEUED cases or TIMEOUT cases.

- [Sending iMessages](https://docs.sendblue.com/docs/outbound/#sending-imessages)
  - [Request body](https://docs.sendblue.com/docs/outbound/#request-body)
  - [Sample response](https://docs.sendblue.com/docs/outbound/#sample-response)
- [Sending files](https://docs.sendblue.com/docs/outbound/#sending-files)
- [Status Callback](https://docs.sendblue.com/docs/outbound/#status-callback)
- [Message Status Resolution](https://docs.sendblue.com/docs/outbound/#message-status-resolution)
  - [Status](https://docs.sendblue.com/docs/outbound/#status)
  - [Error Codes](https://docs.sendblue.com/docs/outbound/#error-codes)
- [Limits](https://docs.sendblue.com/docs/outbound/#limits)
- [Useful Information](https://docs.sendblue.com/docs/outbound/#useful-information)
  - [From Number](https://docs.sendblue.com/docs/outbound/#from-number)
  - [Handle](https://docs.sendblue.com/docs/outbound/#handle)