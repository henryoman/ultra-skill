---
title: Execute Order
source_url: https://dev.jup.ag/docs/ultra/execute-order
section: developer
---

# Execute Order

Submit a signed Ultra Swap transaction via `POST /ultra/v1/execute`.

## Flow

1. Call `GET /ultra/v1/order` to receive `transaction` and `requestId`.
2. Sign the returned transaction with your wallet flow (Solana Kit or wallet adapter).
3. Submit `signedTransaction` + `requestId` to `/execute`.
4. Re-submit the same payload for status polling (up to about 2 minutes).

## Execute Request

```js
const executeResponse = await (
  await fetch('https://api.jup.ag/ultra/v1/execute', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': process.env.JUP_API_KEY
    },
    body: JSON.stringify({
      signedTransaction, // base64 signed tx
      requestId: orderResponse.requestId
    })
  })
).json();

console.log(executeResponse);
```

## Status Check

```js
if (executeResponse.status === 'Success') {
  console.log('Swap success:', executeResponse.signature);
} else {
  console.log('Swap state:', executeResponse.status);
  console.log('Signature:', executeResponse.signature);
}
```

## Notes

- Reusing the same `signedTransaction` and `requestId` does not double-execute.
- If the order expired, execution can fail with no finalized swap.
- Keep request/response logs with `requestId` for operational debugging.
