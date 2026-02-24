---
title: Setting Up API Key
source_url: https://dev.jup.ag/portal/setup
section: portal
---

# Setting Up API Key

> Generate a free API key at portal.jup.ag with Free, Pro, and Ultra tier options.

<Note>
  To use your API key, pass in via header as `x-api-key`.
</Note>

| Tier  | Rate Limit Model                                    | Base URL                    | API Key  |
| ----- | --------------------------------------------------- | --------------------------- | -------- |
| Free  | Fixed Rate Limit                                    | `https://api.jup.ag/`       | Required |
| Pro   | Fixed Tiered Rate Limits (1 RPS to 500 RPS plans)   | `https://api.jup.ag/`       | Required |
| Ultra | Dynamic Rate Limits (based on executed swap volume) | `https://api.jup.ag/ultra/` | Required |

<Steps>
  <Step>
    Open Portal at [https://portal.jup.ag/](https://portal.jup.ag/)
  </Step>

  <Step>
    Connect via email
  </Step>

  <Step>
    <Card title="Free" icon="1" horizontal>
      You are just starting out and want to try Jupiter via API.

      1. Generate an API key
      2. Use the API key with the base URL `https://api.jup.ag/`
    </Card>

    <Card title="Pro" icon="2" horizontal>
      Both small projects and large enterprises can utilize this with the tiered rate limits.

      1. Choose a plan (1 RPS to 500 RPS plans)
      2. Pay via **Helio (USDC on Solana manual renewal)**
      3. Or via **Coinflow (credit card subscription)**

      * Refer to [Payment Method](/portal/payment) for more details
    </Card>

    <Card title="Ultra" icon="3" horizontal>
      For all types of projects, Ultra Swap API uses a Dynamic Rate Limit model that scales with your swap executions.

      1. Generate an API key
      2. Use the API key with the base URL `https://api.jup.ag/ultra/`

      <Tip>
        [Using Ultra Swap API comes with many benefits](/docs/ultra) where Jupiter handles the entire end-to-end execution without the need of an RPC from you.
      </Tip>
    </Card>
  </Step>
</Steps>

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
