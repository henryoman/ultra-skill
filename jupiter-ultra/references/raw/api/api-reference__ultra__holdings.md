> ## Documentation Index
> Fetch the complete documentation index at: https://dev.jup.ag/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Holdings

> Request for token balances of an account including token account information



## OpenAPI

````yaml openapi-spec/ultra/ultra.yaml get /holdings/{address}
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
  /holdings/{address}:
    get:
      summary: holdings
      description: >
        Request for token balances of an account including token account
        information
      parameters:
        - schema:
            type: string
            default: BQ72nSv9f3PRyRKCBnHLVrerrv37CYTHm5h3s9VSGQDV
          in: path
          name: address
          required: true
          description: The wallet address to get holdings for
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HoldingsResponse'
      security:
        - ApiKeyAuth: []
components:
  schemas:
    HoldingsResponse:
      type: object
      properties:
        amount:
          type: string
          description: Total SOL in lamports
        uiAmount:
          type: number
          description: Total SOL in UI units after applying decimals
        uiAmountString:
          type: string
          description: Total SOL as string in UI units after applying decimals
        tokens:
          type: object
          description: Other token holdings organized by mint address as keys
          additionalProperties:
            description: Token mint address as key
            type: array
            items:
              $ref: '#/components/schemas/TokenAccount'
      required:
        - amount
        - uiAmount
        - uiAmountString
        - tokens
    TokenAccount:
      type: object
      properties:
        account:
          type: string
          description: The token account address
        amount:
          type: string
          description: Token amount in atomic/raw units
        uiAmount:
          type: number
          description: Token amount in UI units after applying decimals
        uiAmountString:
          type: string
          description: Token amount as string in UI units after applying decimals
        isFrozen:
          type: boolean
          description: Whether the token account is frozen
        isAssociatedTokenAccount:
          type: boolean
          description: Whether this is an associated token account
        decimals:
          type: number
          description: Number of decimal places for the token
        programId:
          type: string
          description: The token program ID
      required:
        - account
        - amount
        - uiAmount
        - uiAmountString
        - isFrozen
        - isAssociatedTokenAccount
        - decimals
        - programId
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: Get API key via https://portal.jup.ag

````