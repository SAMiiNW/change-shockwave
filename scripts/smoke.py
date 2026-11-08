from pathlib import Path
import json,re,subprocess,time
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as ca
R=Path(__file__).parents[1];ROOT=R.parents[3]
def env(name):
 text=(ROOT/'accounts.env').read_text();return re.search(r'^'+re.escape(name)+r'\s*=\s*"?([^"\r\n]+)',text,re.M).group(1).strip()
def calldata(method=None,args=None,kwargs=None):
 out={}
 if method is not None:out['method']=method
 if args:out['args']=args
 if kwargs:out['kwargs']=kwargs
 return out
ca.make_calldata_object=calldata
owner=create_account(account_private_key=env('ACCOUNT_1_GENLAYER_PRIVATE_KEY'));analyst=create_account(account_private_key=env('ACCOUNT_2_GENLAYER_PRIVATE_KEY'));clients={'owner':create_client(chain=studionet,account=owner),'analyst':create_client(chain=studionet,account=analyst)};deployment=json.loads((R/'deployment.json').read_text());address=deployment['contractAddress'];sha=deployment['sourceCommit'];record_id='WAVE-'+str(int(time.time()));raw='https://raw.githubusercontent.com/SAMiiNW/change-shockwave/'+sha+'/evidence/';cdn='https://cdn.jsdelivr.net/gh/SAMiiNW/change-shockwave@'+sha+'/evidence/';gack='https://raw.githack.com/SAMiiNW/change-shockwave/'+sha+'/evidence/';rawcdn='https://rawcdn.githack.com/SAMiiNW/change-shockwave/'+sha+'/evidence/';static='https://cdn.statically.io/gh/SAMiiNW/change-shockwave/'+sha+'/evidence/'
nodes=[{'id':'GATEWAY','label':'Edge Gateway','doc_url':gack+'gateway.md','depends_on':[]},{'id':'LEDGER','label':'Ledger API','doc_url':rawcdn+'ledger.md','depends_on':[0]},{'id':'WORKER','label':'Queue Worker','doc_url':static+'worker.md','depends_on':[1]},{'id':'SCREEN','label':'Operations Screen','doc_url':'https://github.com/SAMiiNW/change-shockwave/blob/'+sha+'/evidence/screen.md','depends_on':[0,2]}]
txs={}
def send(who,method,args):
 tx=clients[who].write_contract(address=address,function_name=method,args=args);receipt=clients[who].wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True);leaders=receipt.get('consensus_data',{}).get('leader_receipt') or [];leaders=[leaders] if isinstance(leaders,dict) else leaders;assert receipt.get('result_name')=='MAJORITY_AGREE' and any(x.get('execution_result')=='SUCCESS' for x in leaders),receipt;txs[method]=str(tx)
send('owner','file_change',[record_id,analyst.address,'Gateway header migration shockwave',raw+'change-policy.md',cdn+'change-notice.md',json.dumps(nodes),3600]);send('analyst','scan_change',[record_id]);scanned=clients['owner'].read_contract(address=address,function_name='get_map',args=[record_id]);assert scanned['state']=='SCANNED' and scanned['gate']=='STOP' and scanned['rollback_order'],scanned;send('owner','acknowledge',[record_id]);final=clients['owner'].read_contract(address=address,function_name='get_map',args=[record_id]);assert final['state']=='ACKNOWLEDGED';out={'recordType':'operator-controlled change rehearsal','recordId':record_id,'contractAddress':address,'wallets':{'owner':owner.address,'analyst':analyst.address},'transactions':txs,'readback':final};(R/'network-run.json').write_text(json.dumps(out,indent=2,default=str)+'\n');print(json.dumps(out,indent=2,default=str),flush=True)
