# Queue Worker service document

Queue Worker consumes jobs emitted by Ledger API. It has no direct dependency on gateway headers. A loss of accepted gateway traffic propagates through Ledger API and reduces the jobs available to this worker.
