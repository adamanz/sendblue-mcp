[Skip to main content](https://docs.sendblue.com/docs/get-messages/#__docusaurus_skipToContent_fallback)

On this page

The Sendblue API allows you to retrieve messages sent or received for your account.

## Get Messages [​](https://docs.sendblue.com/docs/get-messages/\#get-messages "Direct link to Get Messages")

To retrieve messages, make a GET request to the following endpoint:

`GET https://api.sendblue.co/accounts/messages`

### Query Parameters [​](https://docs.sendblue.com/docs/get-messages/\#query-parameters "Direct link to Query Parameters")

- `cid` (optional): Filter messages by conversation ID (contact ID).
- `number` (optional): Filter messages by the sender or recipient's phone number.
- `limit` (optional): The maximum number of messages to retrieve per request.
- `offset` (optional): The offset for paginating through messages.
- `from_date` (optional): Filter messages sent after the specified date and time (e.g., "2023-06-15 12:00:00").

If no `cid` or `number` is defined, the endpoint will return all messages for the contact making the request (defined by your keys sent by the headers).

### Sample Request [​](https://docs.sendblue.com/docs/get-messages/\#sample-request "Direct link to Sample Request")

```codeBlockLines_e6Vv
curl --location --request GET 'https://api.sendblue.co/accounts/messages?limit=50&offset=10&number=+12345678912&from_date=2023-06-15%2012:00:00' \
--header 'sb-api-key-id: YOUR_SB_API_KEY_ID' \
--header 'sb-api-secret-key: YOUR_SB_API_SECRET_KEY'

```

Here is the same with Node.js and Axios

```codeBlockLines_e6Vv
const axios = require("axios");

const url = "https://api.sendblue.co/accounts/messages";

axios
  .get(url, {
    headers: {
      "SB-API-KEY-ID": "YOUR_SB_API_KEY_ID",
      "SB-API-SECRET-KEY": "YOUR_SB_API_SECRET_KEY",
    },
    params: {
      limit: 50,
      offset: 0,
      number: "+12345678912",
      from_date: "2023-06-15 12:00:00",
    },
  })
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.log(error);
  });

```

## Sample Response [​](https://docs.sendblue.com/docs/get-messages/\#sample-response "Direct link to Sample Response")

```codeBlockLines_e6Vv
{
  "messages": [\
    {\
      "date": "2023-08-15T16:04:38.866Z",\
      "allowSMS": null,\
      "sendStyle": "",\
      "type": "message",\
      "uuid": "e8942f7a-c1d2-49e1-b35f-68958754635d",\
      "media_url": "",\
      "content": "Hey",\
      "number": "+12345678912",\
      "is_outbound": true,\
      "accountEmail": "youremail@gmail.com",\
      "was_downgraded": false,\
      "callbackURL": "",\
      "row_id": null,\
      "status": "QUEUED"\
    },\
    {\
      "error_message": null,\
      "date": "2023-09-21T20:22:05.066Z",\
      "to_number": "+12345678912",\
      "date_sent": {\
        "_seconds": 1695327725,\
        "_nanoseconds": 66000000\
      },\
      "date_updated": {\
        "_seconds": 1695327725,\
        "_nanoseconds": 456000000\
      },\
      "error_detail": null,\
      "phoneID": "worker_5s_spacegray_1",\
      "message_type": "message",\
      "uuid": "595578e5-6701-4b89-ac9b-28cbfe99cd",\
      "media_url": "",\
      "content": "test\n - Sent using sendblue.co",\
      "send_style": "",\
      "callback_url": "",\
      "is_outbound": true,\
      "allow_sms": false,\
      "accountEmail": "youremail@gmail.com",\
      "was_downgraded": null,\
      "group_id": "",\
      "from_number": "+88888888888",\
      "error_code": 22,\
      "row_id": "4444",\
      "status": "ERROR"\
    }\
  ]
}

```

- [Get Messages](https://docs.sendblue.com/docs/get-messages/#get-messages)
  - [Query Parameters](https://docs.sendblue.com/docs/get-messages/#query-parameters)
  - [Sample Request](https://docs.sendblue.com/docs/get-messages/#sample-request)
- [Sample Response](https://docs.sendblue.com/docs/get-messages/#sample-response)