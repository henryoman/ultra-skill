# Ultra API: Search Tokens

- Source: https://dev.jup.ag/api-reference/ultra/search
- Snapshot: ../../raw/api/api-reference__ultra__search.md

---

## Source Content

### Search Token

> Request a search by token's symbol, name or mint address



## OpenAPI Specification

````yaml openapi-spec/ultra/ultra.yaml get /search
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
  /search:
    get:
      summary: search
      description: |
        Request a search by token's symbol, name or mint address
      parameters:
        - in: query
          name: query
          schema:
            type: string
            default: EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
          required: true
          description: >
            - Search for a token and its information by its symbol, name or mint
            address

            - Comma-separate to search for multiple

            - Limit to 100 mint addresses in query

            - Default to 20 mints in response when searching via symbol or name
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/MintInformation'
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
  schemas:
    MintInformation:
      type: object
      properties:
        id:
          type: string
          description: The token's mint address
        name:
          type: string
        symbol:
          type: string
        icon:
          type: string
          nullable: true
        decimals:
          type: number
        twitter:
          type: string
          nullable: true
        telegram:
          type: string
          nullable: true
        website:
          type: string
          nullable: true
        dev:
          type: string
          nullable: true
          description: The token's developer address
        circSupply:
          type: number
          nullable: true
        totalSupply:
          type: number
          nullable: true
        tokenProgram:
          type: string
          description: The token program address
        launchpad:
          type: string
          nullable: true
        partnerConfig:
          type: string
          nullable: true
        graduatedPool:
          type: string
          nullable: true
        graduatedAt:
          type: string
          nullable: true
        holderCount:
          type: number
          nullable: true
        fdv:
          type: number
          nullable: true
        mcap:
          type: number
          nullable: true
        usdPrice:
          type: number
          nullable: true
        priceBlockId:
          type: number
          nullable: true
        liquidity:
          type: number
          nullable: true
        stats5m:
          $ref: '#/components/schemas/SwapStats'
          nullable: true
        stats1h:
          $ref: '#/components/schemas/SwapStats'
          nullable: true
        stats6h:
          $ref: '#/components/schemas/SwapStats'
          nullable: true
        stats24h:
          $ref: '#/components/schemas/SwapStats'
          nullable: true
        firstPool:
          type: object
          nullable: true
          properties:
            id:
              type: string
            createdAt:
              type: string
        audit:
          type: object
          nullable: true
          properties:
            isSus:
              type: boolean
              nullable: true
            mintAuthorityDisabled:
              type: boolean
              nullable: true
            freezeAuthorityDisabled:
              type: boolean
              nullable: true
            topHoldersPercentage:
              type: number
              nullable: true
            devBalancePercentage:
              type: number
              nullable: true
            devMigrations:
              type: number
              nullable: true
        organicScore:
          type: number
        organicScoreLabel:
          type: string
          enum:
            - high
            - medium
            - low
        isVerified:
          type: boolean
          nullable: true
        cexes:
          type: array
          items:
            type: string
          nullable: true
        tags:
          type: array
          items:
            type: string
          nullable: true
        updatedAt:
          type: string
          format: date-time
    SwapStats:
      type: object
      properties:
        priceChange:
          type: number
          nullable: true
        holderChange:
          type: number
          nullable: true
        liquidityChange:
          type: number
          nullable: true
        volumeChange:
          type: number
          nullable: true
        buyVolume:
          type: number
          nullable: true
        sellVolume:
          type: number
          nullable: true
        buyOrganicVolume:
          type: number
          nullable: true
        sellOrganicVolume:
          type: number
          nullable: true
        numBuys:
          type: number
          nullable: true
        numSells:
          type: number
          nullable: true
        numTraders:
          type: number
          nullable: true
        numOrganicBuyers:
          type: number
          nullable: true
        numNetBuyers:
          type: number
          nullable: true
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: Get API key via https://portal.jup.ag

````
