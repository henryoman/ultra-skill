---
title: Get Routers
source_url: https://dev.jup.ag/api-reference/ultra/routers
section: api
---

# Get Routers

> Request for the list of routers available in the routing engine of Ultra

## OpenAPI

````yaml openapi-spec/ultra/ultra.yaml get /order/routers
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
  /order/routers:
    get:
      summary: routers
      description: >
        Request for the list of routers available in the routing engine of
        Ultra, which is [Juno](/docs/routing#juno-liquidity-engine)
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                    name:
                      type: string
                      enum:
                        - Iris
                        - JupiterZ
                        - DFlow
                        - OKX DEX Router
                    icon:
                      type: string
                  required:
                    - id
                    - name
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
const url = new URL('https://api.jup.ag/ultra/v1/routers');
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
