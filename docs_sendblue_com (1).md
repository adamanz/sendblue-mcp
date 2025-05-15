[Skip to main content](https://docs.sendblue.com/docs/inbound/#__docusaurus_skipToContent_fallback)

On this page

caution

A user must be registered as a contact on your account before their messages will be routed to you. This can be done by sending them a message or adding them as a contact.

Need receive-first texting? [Talk to us](mailto:support@sendblue.com) about our dedicated plans.

### Receiving Messages [​](https://docs.sendblue.com/docs/inbound/\#receiving-messages "Direct link to Receiving Messages")

In order to enable receiving messages, you have to specify the webhooks that you want to use in your api dashboard.

Received Messages will be sent as a POST request to the webhook which you define. These messages will be delivered in the JSON of a POST body which looks like this:

```codeBlockLines_e6Vv
{
  "accountEmail": "support@sendblue.com",
  "content": "Ahoy Developer!",
  "media_url": "some_cdn_link.png",
  "is_outbound": false,
  "status": "RECEIVED",
  "error_code": null,
  "error_message": null,
  "message_handle": "xxxxx",
  "date_sent": "2020-09-10T06:15:05.962Z",
  "date_updated": "2020-09-10T06:15:05.962Z",
  "from_number": "+19998887777",
  "number": "+19998887777",
  "to_number": "+15122164639",
  "was_downgraded": false,
  "plan": "blue"
}

```

important

You must send a response to our server in order to avoid receiving multiple webhook calls.

## Webhook Body Parsing [​](https://docs.sendblue.com/docs/inbound/\#webhook-body-parsing "Direct link to Webhook Body Parsing")

| Callback Body Field | Type | Description |
| --- | --- | --- |
| accountEmail | `string` | Associated account email |
| content | `string` | Message content |
| media\_url | `string` | A CDN link to the image that was sent to your sendblue number from an end-user. This link expires after 30 days |
| is\_outbound | `boolean` | True if message is sent, false if message is received |
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

- [Receiving Messages](https://docs.sendblue.com/docs/inbound/#receiving-messages)
- [Webhook Body Parsing](https://docs.sendblue.com/docs/inbound/#webhook-body-parsing)