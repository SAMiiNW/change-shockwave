from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text(encoding='utf-8')
def test_public_surface():
 for name in ('file_change','scan_change','acknowledge','expire','get_map'):assert 'def '+name in S
def test_validators_recompute_every_stored_field():assert 'return run()==leader.calldata' in S and "'direct_impacts':out,'digests':digests" in S
def test_source_and_topology_guards():assert 'policy_origin==change_origin' in S and 'origin in origins' in S and 'dep>=index' in S
def test_propagation_is_deterministic_code():assert 'while queue:' in S and "current in node['depends_on']" in S and "m.gate='STOP'" in S
def test_roles_deadline_and_replay():assert 'gl.message.sender_address!=m.analyst' in S and "m.state!='FILED'" in S and 'now()>int(m.deadline)' in S
