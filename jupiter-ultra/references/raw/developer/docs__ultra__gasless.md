> ## Documentation Index
> Fetch the complete documentation index at: https://dev.jup.ag/llms.txt
> Use this file to discover all available pages before exploring further.

# Gasless Support

> Gasless swap mechanisms that let users trade without holding SOL for transaction fees.

The Jupiter Ultra Swap includes **2 different gasless mechanisms** that allow users to
execute swaps without having to pay for network fees, priority fees/tips or rent in SOL. This
feature reduces onboarding friction and supports a smoother user experience where end-users
don't need to hold SOL just to trade tokens.

## Quick Overview

| Gasless Mechanism              | Coverage                                                                               | Requirements & Notes                                                                                                                                                                                                            |
| ------------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ultra<br />Gasless Support** | - Base network fee<br />- Priority fee/tips<br />- ATA rent<br />- Other accounts rent | - Taker has less than 0.01 SOL<br />- Minimum trade size of \~10 USD<br />- Gas is taken from swap amount which increases swap fee<br />- Does not work with referral/payer params<br />- Does not work with manual mode params |
| **JupiterZ<br />(RFQ)**        | - Base network fee<br />- Priority fee/tips                                            | - Always gasless for network/prio fees (paid by MM)<br />- ATA rent NOT covered: user must have enough SOL<br />- No minimum trade size<br />- Only applies if a market maker provides a route                                  |
| **Other Routers**              | -                                                                                      | -                                                                                                                                                                                                                               |

## Types of Gas

1. Base network transaction fee
2. Associated Token Account (ATA) rent
3. Priority fee (or tips, etc)
4. Other accounts rent (some DEX may require additional accounts opened per taker (e.g. Pumpfun))

## Types of Gasless Mechanism

<Note>
  Refer to [Payer](/docs/ultra/add-payer) section for more details and usage on the Integrator Gas Payer.
</Note>

<Tabs>
  <Tab title="Jupiter Ultra Gasless Support">
    1. **When does it apply?**
       * Gasless Support only kicks in for Iris router.
       * Requires taker to have less than 0.01 SOL.
       * Minimum trade size of 10 USD is required, but this is dynamic as priority fees/tips can vary based on the current market conditions.

    2. **What does it cover?**
       * Base network transaction fee
       * Priority fee/tips
       * Associated token account rent
       * Other accounts rent

    3. **How does it work?**
       * It calculates the required SOL amount to cover the cost of gasless support, and increases the swap fee to cover the cost, this means the taker will recieve lesser output tokens. You can use the `feeBps` field to identify the increased fee.
       * It adds a secondary signer to the transaction to pay to be the gas payer which is Jupiter Ultra's self gas payer.

    4. **What are the limitations?**
       * It only works for default Ultra transactions
       * It does not work when passing in integrator parameters like `referralAccount`, `referralFee`, `payer`, etc.
       * It does not work when passing in manual mode parameters like `slippageBps`, `priorityFeeLamports`, `excludeRouters`, etc.

        <img src="https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/gasless-support-mechanism.png?fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=6ff068675e3c62dda2494b23b841a05b" alt="Gasless Support Mechanism" data-og-width="2876" width="2876" data-og-height="1608" height="1608" data-path="static/images/gasless-support-mechanism.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/gasless-support-mechanism.png?w=280&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=9e39c7ba5dc983a8775661a06a4e42ac 280w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/gasless-support-mechanism.png?w=560&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=591550ee694cc4b826edf689c0cc25e8 560w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/gasless-support-mechanism.png?w=840&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=ff368622a33b0b8bc877cfdda47a8087 840w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/gasless-support-mechanism.png?w=1100&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=4aa0947d7cac6c9f505ac0bf6b87128c 1100w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/gasless-support-mechanism.png?w=1650&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=7b286cd0fc42a08ac189ba585ac958bc 1650w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/gasless-support-mechanism.png?w=2500&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=70e0908f1daca3b98470c31b72bd0363 2500w" />
  </Tab>

  <Tab title="Jupiter Z (RFQ) Gasless">
    1. **When does it apply?**
       * JupiterZ is our RFQ engine, it is gasless by default.
       * No minimum trade size required but dependent on if MM provides a quote.

    2. **What does it cover?**
       * Base network transaction fee
       * Priority fee (or tips, etc)
       * **Does not cover for associated token account rent**.
       * It also means the taker will have to pay for the rent themselves, and if they do not have sufficient SOL for rent, JupiterZ will not be routed.

    3. **How does it work?**
       * As long as the JupiterZ (or the market makers) provide a quote for your request, the transaction will be gasless.
       * It adds a secondary signer to the transaction to pay to be the gas payer - which is the market maker.

    4. **What are the limitations?**
       * It only works for default Ultra transactions
       * It does not work when passing in integrator parameters like `referralAccount`, `referralFee`, `payer`, etc.
       * It does not work when passing in manual mode parameters like `slippageBps`, `priorityFeeLamports`, `excludeRouters`, etc.
       * If taker does not have sufficient SOL for rent, JupiterZ will not be routed.

        <img src="https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/jupiterz-gasless-mechanism.png?fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=09c984f1214782a006300ccb80ed31a7" alt="JupiterZ Gasless Mechanism" data-og-width="2954" width="2954" data-og-height="1556" height="1556" data-path="static/images/jupiterz-gasless-mechanism.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/jupiterz-gasless-mechanism.png?w=280&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=9c2ff62367eb29c28543e3ec79410f47 280w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/jupiterz-gasless-mechanism.png?w=560&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=ee8fcc5f901b5b74527f5d9376ef9a13 560w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/jupiterz-gasless-mechanism.png?w=840&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=3755f5acea0553408e7128d5e64447ba 840w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/jupiterz-gasless-mechanism.png?w=1100&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=71678898d6ff14338712a442ff9ed484 1100w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/jupiterz-gasless-mechanism.png?w=1650&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=0219e177c46044d005a4ce663f53c70a 1650w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/jupiterz-gasless-mechanism.png?w=2500&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=bc7f8733497357efc02daa0637373b3d 2500w" />
  </Tab>

  <Tab title="Integrator Gas Payer">
    1. **When does it apply?**
       * Integrator Gas Payer works only when integrator passes in `referralAccount` and `referralFee`, together with `payer` and `closeAuthority`.
       * Regardless of how much SOL the taker has, the payer will be the fee payer.
       * Applying these parameters will default routing to only Iris.

    2. **What does it cover?**
       * The `payer` address will be the fee payer of the entire transaction:
         * Base network transaction fee
         * Priority fee/tips
         * Associated token account rent
         * Other account rents

    3. **How does it work?**
       * The transaction returned will require both taker and payer signature before submitting to `/execute`.
       * The associated token account rent such as:
         * Temporary WSOL ATA will be covered by payer and will be returned to payer in the same transaction.
         * Any other ATAs will be covered by payer, but not returned to payer in the same transaction, since it is likely the ATA holds the tokens post-swap.
       * The `closeAuthority` address will be decided by you, refer to [Payer](/docs/ultra/add-payer) for more details.
       * It adds a secondary signer to the transaction to pay to be the gas payer - which is the integrator.

    4. **What are the limitations?**
       * Passing in `payer` parameters will default routing to only Iris.

        <img src="https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/integrator-gas-payer-mechanism.png?fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=0e2f8e68f2d529efd1306427e539851d" alt="Integrator Gas Payer Mechanism" data-og-width="2148" width="2148" data-og-height="1026" height="1026" data-path="static/images/integrator-gas-payer-mechanism.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/integrator-gas-payer-mechanism.png?w=280&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=15799546c91f65c1d346e9ab3d9e025d 280w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/integrator-gas-payer-mechanism.png?w=560&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=4b40ca1a647060c99e5c113de9cb6c02 560w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/integrator-gas-payer-mechanism.png?w=840&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=eb3b0dd4d32337eecc408254dcb1640b 840w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/integrator-gas-payer-mechanism.png?w=1100&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=3efe9bcc93eb68457f5eb3fb1a4d6980 1100w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/integrator-gas-payer-mechanism.png?w=1650&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=bb1657c49187979b2c700cc09b96f5a5 1650w, https://mintcdn.com/jupiter/5ASJJl7VtSphXLOO/static/images/integrator-gas-payer-mechanism.png?w=2500&fit=max&auto=format&n=5ASJJl7VtSphXLOO&q=85&s=3f9a0eaa71d50fcc40cca8b60b2bffac 2500w" />
  </Tab>
</Tabs>

## Scenario Matrix

| **Scenario**                         | **Ultra<br />Gasless Support**                                                               | **JupiterZ<br />(Assuming if quoted)** |
| ------------------------------------ | -------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Taker has SOL & ATA**              | Taker pays gas                                                                               | MM pays gas                            |
| **Taker has SOL, no ATA**            | Taker pays gas & ATA rent                                                                    | MM pays gas, taker pays ATA rent       |
| **No SOL, has ATA**                  | - Gas taken from swap amount<br />- Min \$10 swap                                            | MM pays gas                            |
| **No SOL, no ATA**                   | - Gas & rent from swap amount<br />- Min \$10 swap                                           | Not supported (no ATA funding)         |
| **No SOL, has ATA,<br />Small swap** | Quote shown, but cannot swap<br />[`errorCode=3`](/docs/ultra/response#order-response-codes) | MM pays gas                            |
| **No SOL, no ATA,<br />Small swap**  | Quote shown, but cannot swap<br />[`errorCode=3`](/docs/ultra/response#order-response-codes) | Not supported (no ATA funding)         |
