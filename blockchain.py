from ds import Block
import datetime
def create_genesis_block():
    #first block in chain
    return Block(0,datetime.datetime.now(),{"data":"First Block","pow":11},0)

def next_block(cur_block,data):
    #function to create new blocks
    return Block(cur_block.index+1,datetime.datetime.now(),data,cur_block.hash)