# Ledger API service document

Ledger API receives authenticated requests from Edge Gateway. It does not read the routing header itself, but it cannot receive traffic when the gateway rejects the request. Its direct interface is unchanged by the proposed header rename.
