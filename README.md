# CHANGE SHOCKWAVE / PREFLIGHT FIELD SHEET

One service changes. The graph answers what moves next.

The owner files an ordered service topology, a change policy, the proposed change, a separate analyst wallet, and one independently hosted document per service. GenLayer validators fetch every source and name only the directly impacted service indexes with `BREAK`, `DEGRADE`, or `OBSERVE`. They do not calculate the blast radius.

## Propagation law

Contract code walks reverse dependencies from the agreed direct set. It stores every affected node, propagation depth, severity, an explicit `STOP`, `STAGE`, or `MONITOR` gate, and a deepest-first rollback order. A malformed graph, repeated source origin, duplicate ID, late analyst, replay, or unauthorized acknowledgement is rejected.

Lifecycle: `FILED -> SCANNED -> ACKNOWLEDGED`; an abandoned filed change becomes `EXPIRED` permissionlessly after its review deadline.

## Field drill

```text
python -m pytest -q
genvm-lint lint contracts/contract.py
```

The bundled documents and wallets are operator-controlled rehearsal fixtures. They prove enforcement and propagation, not independent production authority.
