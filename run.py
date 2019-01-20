from blockchain import *
from ds import Block

#our blockchain as a list
blchain=[create_genesis_block()]
previous_block=blchain[-1]

#create umm 30 new blocks
for i in range(30):
    new_block=next_block(previous_block,data="Hello "+str(previous_block.index)+" incremented")
    blchain.append(new_block)
    previous_block=blchain[-1]
    print("Added new block of hash:- "+str(new_block.hash)+" of index :- "+str(new_block.index)+"\n")

print("end!")
