[Skip to main content](https://docs.sendblue.com/docs/create-media-object/#__docusaurus_skipToContent_fallback)

On this page

The Sendblue API allows you to create a media object by uploading a file using the specified endpoint.

## Create Media Object [​](https://docs.sendblue.com/docs/create-media-object/\#create-media-object "Direct link to Create Media Object")

To create a media object, make a POST request to the following endpoint:

`POST https://api.sendblue.co/api/upload-media-object`

### Request Parameters [​](https://docs.sendblue.com/docs/create-media-object/\#request-parameters "Direct link to Request Parameters")

- `media_url` (string): The URL containing the media object.

### Sample Request [​](https://docs.sendblue.com/docs/create-media-object/\#sample-request "Direct link to Sample Request")

```codeBlockLines_e6Vv
curl --location --request POST 'https://api.sendblue.co/api/upload-media-object' \
--header 'sb-api-key-id: YOUR_SB_API_KEY_ID' \
--header 'sb-api-secret-key: YOUR_SB_API_SECRET_KEY' \
--data-raw '{
  "media_url": "URL_TO_YOUR_MEDIA_OBJECT"
}'

```

Here is the same in Node.js with Axios

```codeBlockLines_e6Vv
const axios = require("axios");

const url = "https://api.sendblue.co/api/upload-media-object";

axios
  .post(
    url,
    {
      media_url: "URL_TO_YOUR_MEDIA_OBJECT",
    },
    {
      headers: {
        "sb-api-key-id": "YOUR_SB_API_KEY_ID",
        "sb-api-secret-key": "YOUR_SB_API_SECRET_KEY",
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

Sample Responses

Successful Response (Status 201)

```codeBlockLines_e6Vv
{
  "status": "OK",
  "message": "File uploaded successfully",
  "mediaObjectId": "MO_asdasdasdasdasd.jpg"
}

```

Error Response (Status 400)

```codeBlockLines_e6Vv
{
  "status": "ERROR",
  "message": "Invalid media URL"
}

```

Please make sure to replace placeholders like YOUR\_SB\_API\_KEY\_ID and YOUR\_SB\_API\_SECRET\_KEY with your actual API credentials in the sample requests.

- [Create Media Object](https://docs.sendblue.com/docs/create-media-object/#create-media-object)
  - [Request Parameters](https://docs.sendblue.com/docs/create-media-object/#request-parameters)
  - [Sample Request](https://docs.sendblue.com/docs/create-media-object/#sample-request)