# Edge Gateway service document

The Edge Gateway requires `X-Route-Key` on every routed request. Its public interface rejects a request when that header is missing. Downstream services receive only requests accepted by this gateway.
