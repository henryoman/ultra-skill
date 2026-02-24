---
title: Add Integrator Fees
source_url: https://dev.jup.ag/docs/ultra/add-fees-to-ultra
section: developer
---

# Add Integrator Fees

Add custom integrator fees to Ultra orders using Referral Program accounts.

## What Matters

- Configure `referralAccount` and `referralFee` on `/order`.
- Create referral token accounts for fee collection mints you want to support.
- `feeMint` is selected by Ultra per route.
- If required referral token account is missing, swap may execute without your integrator fee.

## Get Order With Integrator Fee

```js
const url = new URL('https://api.jup.ag/ultra/v1/order');
url.searchParams.set('inputMint', '<INPUT_MINT>');
url.searchParams.set('outputMint', '<OUTPUT_MINT>');
url.searchParams.set('amount', '<AMOUNT_IN_BASE_UNITS>');
url.searchParams.set('taker', '<TAKER_PUBKEY>');
url.searchParams.set('referralAccount', '<REFERRAL_ACCOUNT_PUBKEY>');
url.searchParams.set('referralFee', '100'); // bps, example

const orderResponse = await (
  await fetch(url, {
    headers: { 'x-api-key': process.env.JUP_API_KEY }
  })
).json();

console.log(orderResponse.feeBps, orderResponse.feeMint);
```

## Execute Signed Order

```js
const executeResponse = await (
  await fetch('https://api.jup.ag/ultra/v1/execute', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': process.env.JUP_API_KEY
    },
    body: JSON.stringify({
      signedTransaction,
      requestId: orderResponse.requestId
    })
  })
).json();

console.log(executeResponse.status, executeResponse.signature);
```

## Operational Checks

- Validate `feeBps` in order response matches your intended configuration.
- Track `feeMint` and ensure referral token account readiness for that mint.
- Alert on orders where fee fields are absent or defaulted.
