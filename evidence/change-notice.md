# Proposed change fixture

The edge gateway will rename the required request header from `X-Route-Key` to `X-Service-Key` without accepting the old name. No adapter or dual-read period is planned. The change directly breaks the current Edge Gateway interface. It does not directly modify Ledger API, Queue Worker, or Operations Screen source code.
