# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def dictMaker(l):
    res = {}
    for i in l:
        if(res.get(i[0])):
            res[i[0]] = res.get(i[0]) + [i[1]]
        else:
            res[i[0]] = [i[1]]
    return res

def main(name):
    merge_sublists = lambda l : [i for subl in l for i in subl]
    
    hm = dictMaker(merge_sublists(name))

    return [(k, v) for k, v in hm.items()]
