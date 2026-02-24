---
title: Ultra Swap API
source_url: https://dev.jup.ag/api-reference/ultra
section: api
---

# Ultra Swap API

> Endpoints for quotes, execution, token search, holdings, and security checks.

<CardGroup>
  <Card title="order" href="/api-reference/ultra/order" icon="file-lines" horizontal>
    Request for a base64-encoded unsigned swap transaction to be used in `POST /ultra/v1/execute`
  </Card>

  <Card title="execute" href="/api-reference/ultra/execute" icon="file-lines" horizontal>
    Execute the signed transaction and get the execution status
  </Card>

  <Card title="holdings" href="/api-reference/ultra/holdings" icon="file-lines" horizontal>
    Request for token balances of an account
  </Card>

  <Card title="shield" href="/api-reference/ultra/shield" icon="file-lines" horizontal>
    Request for token information and warnings of mints
  </Card>

  <Card title="balances (deprecated)" href="/api-reference/ultra/balances" icon="file-lines" horizontal>
    Request for token balances of an account
  </Card>

  <Card title="search" href="/api-reference/ultra/search" icon="file-lines" horizontal>
    Request a search by token's symbol, name or mint address
  </Card>

  <Card title="routers" href="/api-reference/ultra/routers" icon="file-lines" horizontal>
    Request for the list of routers available in the routing engine of Ultra Swap, which is [Juno](/docs/routing#juno-liquidity-engine)
  </Card>
</CardGroup>

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
