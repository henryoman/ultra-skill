---
title: Response Codes
source_url: https://dev.jup.ag/portal/responses
section: portal
---

# Response Codes

> Response codes for Jupiter APIs

<Tip>
  **Help Us Debug**

  If you face any issues, please provide clear and concise description of the error/issue.

  Additionally, **logging the response headers** will be helpful for us to identify your requests.
</Tip>

<Note>
  **Product Specific Error Codes**

  For product-level response codes, please refer to each product pages for more information.
</Note>

| Common Codes | Description           | Debug                                                                                       |
| :----------- | :-------------------- | :------------------------------------------------------------------------------------------ |
| 200          | Good                  | Success!                                                                                    |
| 400          | Bad Request           | Likely a problem with the request, check the request parameters, syntax, etc.               |
| 401          | Unauthorized          | Likely a problem with the API key, check if the API key is correct.                         |
| 404          | Not Found             | Likely a broken or invalid endpoint.                                                        |
| 429          | Rate Limited          | You are being rate limited. Either slow down requests, reduce bursts, or upgrade your plan. |
| 500          | Internal Server Error | Please reach out in [Discord](https://discord.gg/jup).                                      |
| 502          | Bad Gateway           | Please reach out in [Discord](https://discord.gg/jup).                                      |
| 503          | Service Unavailable   | Please reach out in [Discord](https://discord.gg/jup).                                      |
| 504          | Gateway Timeout       | Please reach out in [Discord](https://discord.gg/jup).                                      |

## JavaScript Example (API)

```js
const url = new URL('https://api.jup.ag/ultra/v1/order');
// Add required params as needed for this endpoint
// url.searchParams.set('inputMint', '<MINT>');
// url.searchParams.set('outputMint', '<MINT>');
// url.searchParams.set('amount', '<AMOUNT_IN_BASE_UNITS>');

const res = await fetch(url, {
  headers: { 'x-api-key': process.env.JUP_API_KEY }
});
const data = await res.json();
console.log(data);
```
