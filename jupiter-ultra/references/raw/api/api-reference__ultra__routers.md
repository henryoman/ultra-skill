> ## Documentation Index
> Fetch the complete documentation index at: https://dev.jup.ag/llms.txt
> Use this file to discover all available pages before exploring further.

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