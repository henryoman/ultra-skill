---
title: Get Balances
source_url: https://dev.jup.ag/api-reference/ultra/balances
section: api
---

# Get Balances

> Request for token balances of an account (Deprecated - use /holdings instead)

## OpenAPI

````yaml openapi-spec/ultra/ultra.yaml get /balances/{address}
openapi: 3.0.3
info:
  title: Jupiter Ultra Swap API
  version: 1.0.0
  description: Jupiter Ultra Swap API Schema
servers:
  - url: https://api.jup.ag/ultra/v1
    description: Jupiter Ultra Swap API Endpoint
security: []
paths:
  /balances/{address}:
    get:
      summary: balances
      description: |
        Request for token balances of an account
      parameters:
        - schema:
            type: string
          in: path
          name: address
          required: true
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  type: object
                  properties:
                    amount:
                      type: string
                    uiAmount:
                      type: number
                    slot:
                      type: number
                    isFrozen:
                      type: boolean
                  required:
                    - amount
                    - uiAmount
                    - slot
                    - isFrozen
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                required:
                  - error
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                required:
                  - error
      deprecated: true
      security:
        - ApiKeyAuth: []
components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: Get API key via https://portal.jup.ag

````

## JavaScript Example (API)

```js
const url = new URL('https://api.jup.ag/ultra/v1/balances');
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
