from flask import Flask
from flask import request
from blockchain import *
from ds import Block
import requests
from uuid import getnode as get_mac
import hashlib 
import json

sha=hashlib.sha256()

def p_o_w(last_proof):
    inc=last_proof+1
    while inc%11!=0 and inc%last_proof!=0:
        inc+=1
    return inc


peer=Flask(__name__)

#storing this node's transaction
this_node=[]

blchain=[create_genesis_block()]
previous_block=blchain[-1]

peer_nodes=["localhost:5000"]

sha.update(str(get_mac()).encode('utf-8'))
miner_address=sha.hexdigest()

mining=True

def blockchain_r():
    return blchain

@peer.route("/trans",methods=["POST"])
def transaction():
    if request.method=="POST":
        t=request.get_json()
        this_node.append(t)
        print(t)
        return "Transaction stored successfully"
        

@peer.route("/mine",methods=["GET"])
def miner():
    
    last_proof=blchain[-1].data["pow"]
    pow=p_o_w(last_proof)
    #Work done

    this_node.append(
    { "from": "network", "to": miner_address, "amount": 1 }
    )
    mined_block=next_block(blchain[-1],{"data":{ "from": "network", "to": miner_address, "amount": 1 },"pow":pow})

    print("Mined")
    blchain.append(mined_block)

    return json.dumps({"hash":mined_block.hash,"index":mined_block.index,"last_block_hash":blchain[-2].hash}) + "\n"

@peer.route("/blocklist",methods=["GET"])
def get_block():
    bccp=blchain[:]
    ck=[]
    for block in bccp:
        index=str(block.index)
        hsh=str(block.hash)
        ts=str(block.tstmp)
        data=str(block.data)
        block={"index":index,"hash":hsh,"time":ts,"data":data}
        ck.append(block)
    
    return json.dumps(ck)

def check_other_nodes():
    chains=[]
    for node in peer_nodes:
        chains.append(json.loads(requests.get("http://"+node+"/blocklist").content.decode('utf-8')))
    print(chains)
    return chains


def consensus():
    
    other_nodes=check_other_nodes()
    mx=sorted(other_nodes,key=lambda x:len(x),reverse=True)[0]
    blchain = mx
    return blchain



peer.run()













