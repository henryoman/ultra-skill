---
title: Get Shield
source_url: https://dev.jup.ag/api-reference/ultra/shield
section: api
---

# Get Shield

> Request for token information and warnings of mints

## OpenAPI

````yaml openapi-spec/ultra/ultra.yaml get /shield
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
  /shield:
    get:
      summary: shield
      description: |
        Request for token information and warnings of mints
      parameters:
        - in: query
          name: mints
          schema:
            type: string
            default: >-
              So11111111111111111111111111111111111111112,EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
          required: true
          description: |
            - Comma separated list of mints to get information for
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  warnings:
                    type: object
                    additionalProperties:
                      description: |
                        - Token mint address as key
                      type: array
                      items:
                        type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - NOT_VERIFIED
                              - LOW_LIQUIDITY
                              - NOT_SELLABLE
                              - LOW_ORGANIC_ACTIVITY
                              - HAS_MINT_AUTHORITY
                              - HAS_FREEZE_AUTHORITY
                              - HAS_PERMANENT_DELEGATE
                              - NEW_LISTING
                              - VERY_LOW_TRADING_ACTIVITY
                              - HIGH_SUPPLY_CONCENTRATION
                              - NON_TRANSFERABLE
                              - MUTABLE_TRANSFER_FEES
                              - SUSPICIOUS_DEV_ACTIVITY
                              - SUSPICIOUS_TOP_HOLDER_ACTIVITY
                              - HIGH_SINGLE_OWNERSHIP
                              - '{}%_TRANSFER_FEES'
                            description: |
                              - Type of warning for the token
                          message:
                            type: string
                            description: |
                              - Human-readable warning message
                          severity:
                            type: string
                            enum:
                              - info
                              - warning
                              - critical
                            description: |
                              - Severity level of the warning
                          source:
                            type: string
                            enum:
                              - RugCheck
                            description: |
                              - Optional external source of the warning
                required:
                  - warnings
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
const url = new URL('https://api.jup.ag/ultra/v1/shield');
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
