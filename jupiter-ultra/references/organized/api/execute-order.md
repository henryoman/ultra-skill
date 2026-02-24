# Ultra API: Execute Order

- Source: https://dev.jup.ag/api-reference/ultra/execute
- Snapshot: ../../raw/api/api-reference__ultra__execute.md

---

## Source Content

### Execute

> Execute the signed transaction and get the execution status

<Info>
  **NOTE**

  * The `requestId` is found in the response of `/order`
</Info>


## OpenAPI Specification

````yaml openapi-spec/ultra/ultra.yaml post /execute
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
  /execute:
    post:
      summary: execute
      description: |
        Execute the signed transaction and get the execution status
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                signedTransaction:
                  type: string
                  description: |
                    - The signed transaction to execute
                requestId:
                  type: string
                  description: |
                    - Found in response of `/order`
              required:
                - signedTransaction
                - requestId
            example:
              signedTransaction: >-
                AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAEN...
              requestId: b5e5f3a7-8c4d-4e2f-9a1b-3c6d8e0f2a4b
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    enum:
                      - Success
                      - Failed
                  signature:
                    type: string
                  slot:
                    type: string
                  error:
                    type: string
                  code:
                    type: number
                  totalInputAmount:
                    type: string
                  totalOutputAmount:
                    type: string
                  inputAmountResult:
                    type: string
                  outputAmountResult:
                    type: string
                  swapEvents:
                    type: array
                    items:
                      type: object
                      properties:
                        inputMint:
                          type: string
                        inputAmount:
                          type: string
                        outputMint:
                          type: string
                        outputAmount:
                          type: string
                      required:
                        - inputMint
                        - inputAmount
                        - outputMint
                        - outputAmount
                required:
                  - status
                  - code
              example:
                status: Success
                signature: >-
                  5UfDuX7hXbTiKFJqS1MzGsNpbXTzMKJe2bZP1zrd7DnFBSChKvF2FVDNAuqz7SJpaHXTB9E5DP6tMjfZmVDMJRs
                slot: '324307186'
                code: 0
                totalInputAmount: '100000000'
                totalOutputAmount: '17057460'
                inputAmountResult: '100000000'
                outputAmountResult: '17057460'
                swapEvents:
                  - inputMint: So11111111111111111111111111111111111111112
                    inputAmount: '100000000'
                    outputMint: EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
                    outputAmount: '17057460'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                  code:
                    type: number
                required:
                  - error
                  - code
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                  code:
                    type: number
                required:
                  - error
                  - code
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
