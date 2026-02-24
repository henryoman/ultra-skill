> ## Documentation Index
> Fetch the complete documentation index at: https://dev.jup.ag/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Order

> Request for a base64-encoded unsigned swap transaction to be used in POST /ultra/v1/execute



## OpenAPI

````yaml openapi-spec/ultra/ultra.yaml get /order
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
  /order:
    get:
      summary: order
      description: >
        Request for a base64-encoded unsigned swap transaction to be used in
        `POST /ultra/v1/execute`
      parameters:
        - in: query
          name: inputMint
          schema:
            type: string
            default: So11111111111111111111111111111111111111112
          required: true
        - in: query
          name: outputMint
          schema:
            type: string
            default: EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
          required: true
        - in: query
          name: amount
          schema:
            type: string
            default: '10000000'
          required: true
        - in: query
          name: taker
          schema:
            type: string
            default: BQ72nSv9f3PRyRKCBnHLVrerrv37CYTHm5h3s9VSGQDV
          required: false
        - in: query
          name: receiver
          description: >
            - The public key of the account that will receive the output tokens

            - If not provided, the output tokens will be sent to the taker like
            default

            - It expects an account (NOT a token account)

            - If the output is non-SOL tokens, it only transfers to ATAs (not
            token accounts)

            - If the destination token account is not initialized, an additional
            create ATA instruction will be added to the transaction

            - If the output is SOL, it will transfer native SOL directly to the
            receiver account

            - It does not support destination WSOL token account
          schema:
            type: string
          required: false
        - in: query
          name: payer
          description: >
            - The public key of an account that will be used to cover
            'gas-related' fees on behalf of the taker

            - Gas related fees such as signature fees, priority fees and rent.
            Note that enabling this may result in different routing decisions.

            - Refer to [Integrator Payer](/docs/ultra/add-payer) for more
            details
          schema:
            type: string
          required: false
        - in: query
          name: closeAuthority
          description: >
            - Optional. If used, requires `payer`

            - Ignored, if `payer` is not provided

            - The public key of an account to set as the close authority of ATAs
            created during the swap transaction. Only applies to non-wSOL ATAs
            that persist beyond the execution of the transaction.

            - If `closeAuthority` is not provided, we will default to `taker`

            - If `closeAuthority` is provided and is different from `taker`, we
            will add the instruction to set the new `closeAuthority`
          schema:
            type: string
          required: false
        - in: query
          name: referralAccount
          description: >
            - Refer to [Integrator Fees](/docs/ultra/add-fees-to-ultra) for more
            details
          schema:
            type: string
          required: false
        - in: query
          name: referralFee
          description: >
            - Refer to [Integrator Fees](/docs/ultra/add-fees-to-ultra) for more
            details
          schema:
            type: number
            minimum: 50
            maximum: 255
          required: false
        - in: query
          name: excludeRouters
          schema:
            type: string
            enum:
              - iris
              - jupiterz
              - dflow
              - okx
          required: false
        - in: query
          name: excludeDexes
          description: >
            - [Full list of DEXes
            here](https://dev.jup.ag/api-reference/swap/program-id-to-label),
            for example: `excludeDexes=Raydium,Orca+V2,Meteora+DLMM`

            - **Important**: This only excludes DEXes on the Iris router, does
            not apply to other routers

            - For example:
              - **Exclude** Raydium: `excludeRouters=<all-except-Iris>` and `excludeDexes=Raydium`
              - **Only include** Meteora DLMM: `excludeRouters=<all-except-Iris>` and `excludeDexes=<all-except-MeteoraDLMM>`
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  mode:
                    type: string
                  inputMint:
                    type: string
                  outputMint:
                    type: string
                  inAmount:
                    type: string
                  outAmount:
                    type: string
                  inUsdValue:
                    type: number
                  outUsdValue:
                    type: number
                  priceImpact:
                    type: number
                  swapUsdValue:
                    type: number
                  otherAmountThreshold:
                    type: string
                  swapMode:
                    type: string
                  slippageBps:
                    type: number
                  priceImpactPct:
                    type: string
                    description: >
                      - Please use `priceImpact` field instead, this is still
                      available only for backwards compatibility
                  routePlan:
                    type: array
                    items:
                      type: object
                      properties:
                        swapInfo:
                          type: object
                          properties:
                            ammKey:
                              type: string
                            label:
                              type: string
                            inputMint:
                              type: string
                            outputMint:
                              type: string
                            inAmount:
                              type: string
                            outAmount:
                              type: string
                          required:
                            - ammKey
                            - label
                            - inputMint
                            - outputMint
                            - inAmount
                            - outAmount
                        percent:
                          type: number
                        bps:
                          type: number
                        usdValue:
                          type: number
                      required:
                        - swapInfo
                        - percent
                        - bps
                  referralAccount:
                    type: string
                  feeMint:
                    type: string
                  feeBps:
                    type: number
                    description: >
                      - The fee includes either Ultra default fee or your
                      integrator fee, depending on if referral and/or payer
                      params are passed in

                      - If `referralAccount`, `referralFee` (and `payer` if
                      passed in) are passed in, the fee will be the integrator
                      fee only

                      - If no additional referral params are passed in, the fee
                      will be the Ultra default fee only and can include
                      additional fees for gasless support mechanism
                  platformFee:
                    type: object
                    description: >
                      - This field shows the platform fee only, does not include
                      fee for gas

                      - Platform fee can either be the Ultra default fee or your
                      integrator fee
                    properties:
                      amount:
                        type: string
                      feeBps:
                        type: number
                    required:
                      - feeBps
                  signatureFeeLamports:
                    type: number
                    description: >
                      - The number of lamports the `taker`, `maker` (JupiterZ's
                      MM) or `payer` has to pay for the base network fee, if a
                      valid transaction is returned.
                  signatureFeePayer:
                    type: string
                    nullable: true
                    description: >
                      - The public key of the account that will cover the
                      signature fee, it can be either `taker`, `maker`
                      (JupiterZ's MM) or `payer` if passed in
                  prioritizationFeeLamports:
                    type: number
                    description: >
                      - The number of lamports the `taker`, `maker` (JupiterZ's
                      MM) or `payer` has to pay for higher priority landing, if
                      a valid transaction is returned

                      - Includes priority fees and tips for services such as
                      Jito, etc, if any
                  prioritizationFeePayer:
                    type: string
                    nullable: true
                    description: >
                      - The public key of the account that will cover the
                      prioritization fee, it can be either `taker`, `maker`
                      (JupiterZ's MM) or `payer` if passed in
                  rentFeeLamports:
                    type: number
                    description: >
                      - The number of lamports the `taker` or `payer` has to pay
                      for account rent, if a valid transaction is returned

                      - Note that this value is just an estimate

                      - JupiterZ's MM currently does not cover for rent fees
                  rentFeePayer:
                    type: string
                    nullable: true
                    description: >
                      - The public key of the account that will cover the rent
                      fee, it can be either `taker` or `payer` if passed in

                      - JupiterZ's MM currently does not cover for rent fees
                  swapType:
                    type: string
                    description: |
                      - Deprecated, in favour of router
                  router:
                    type: string
                    enum:
                      - iris
                      - jupiterz
                      - dflow
                      - okx
                  transaction:
                    type: string
                    nullable: true
                    description: >
                      - Unsigned base-64 encoded transaction to be signed and
                      used in `/execute`

                      - If `taker` is null, this field will be null.

                      - If the `transaction` field is empty, it is returned with
                      `errorCode` and `errorMessage` such as Insufficient Funds
                  gasless:
                    type: boolean
                  requestId:
                    description: |
                      - Required to make a request to `/execute`
                    type: string
                  totalTime:
                    type: number
                  taker:
                    type: string
                    nullable: true
                  quoteId:
                    type: string
                  maker:
                    type: string
                  expireAt:
                    type: string
                  errorCode:
                    type: number
                    enum:
                      - 1
                      - 2
                      - 3
                    description: >
                      - This field will be present if `taker` is defined and
                      `transaction` is an empty string

                      - It is unique for each error scenarios
                  errorMessage:
                    type: string
                    enum:
                      - Insufficient funds
                      - Top up `${solAmount}` SOL for gas
                      - Minimum `${swapAmount}` for gasless
                    description: >
                      - This field will be present if `taker` is defined and
                      `transaction` is an empty string

                      - This field can still return despite having a valid
                      order/quote

                      - This is meant for display purposes only and it is
                      discouraged to match these error messages as they could be
                      parameterized
                required:
                  - mode
                  - inputMint
                  - outputMint
                  - inAmount
                  - outAmount
                  - otherAmountThreshold
                  - swapMode
                  - slippageBps
                  - priceImpactPct
                  - routePlan
                  - feeBps
                  - platformFee
                  - signatureFeeLamports
                  - signatureFeePayer
                  - prioritizationFeeLamports
                  - prioritizationFeePayer
                  - rentFeeLamports
                  - rentFeePayer
                  - swapType
                  - router
                  - transaction
                  - gasless
                  - requestId
                  - totalTime
                  - taker
              example:
                mode: ExactIn
                inputMint: So11111111111111111111111111111111111111112
                outputMint: EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
                inAmount: '100000000'
                outAmount: '17057460'
                inUsdValue: 17.13
                outUsdValue: 17.06
                priceImpact: 0.0001
                swapUsdValue: 17.06
                otherAmountThreshold: '17040402'
                swapMode: ExactIn
                slippageBps: 1
                priceImpactPct: '0.0001'
                routePlan:
                  - swapInfo:
                      ammKey: HXpGFJGCEEFdV31tDmjDBaJMEB1fKLiAoKoWr3Fnonid
                      label: Meteora DLMM
                      inputMint: So11111111111111111111111111111111111111112
                      outputMint: EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
                      inAmount: '100000000'
                      outAmount: '17057460'
                    percent: 100
                    bps: 10000
                    usdValue: 17.06
                feeMint: EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
                feeBps: 5
                platformFee:
                  amount: '8529'
                  feeBps: 5
                signatureFeeLamports: 5000
                signatureFeePayer: null
                prioritizationFeeLamports: 254600
                prioritizationFeePayer: null
                rentFeeLamports: 0
                rentFeePayer: null
                swapType: aggregator
                router: iris
                transaction: >-
                  AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAEN...
                gasless: false
                requestId: b5e5f3a7-8c4d-4e2f-9a1b-3c6d8e0f2a4b
                totalTime: 320
                taker: BQ72nSv9f3PRyRKCBnHLVrerrv37CYTHm5h3s9VSGQDV
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Failed to get quotes
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