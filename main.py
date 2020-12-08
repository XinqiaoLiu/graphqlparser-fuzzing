import re
import random
import rules
import queue
import os
import subprocess
import time
import helper
START_SYMBOL = "<Document>"
RE_NONTERMINAL = re.compile(r'(<[^<> ]*>)')
#f1 = open('sample.graphql','w')
#f2 = open('samplepath.txt','w')
#f3 = open('coverage_output.txt','w')


class ExpansionError(Exception):
    pass

def simple_grammar_fuzzer(grammar=rules.EXPR_GRAMMAR, start_symbol=START_SYMBOL,
                          max_nonterminals=10, max_expansion_trials=5000,
                          log=False):
    term = start_symbol
    expansion_trials = 0

    while len(nonterminals(term)) > 0:
        symbol_to_expand = random.choice(nonterminals(term))
        expansions = grammar[symbol_to_expand]
        expansion = random.choice(expansions)
        new_term = term.replace(symbol_to_expand, expansion, 1)

        if len(nonterminals(new_term)) < max_nonterminals:
            term = new_term
            if log:
                with open('samplepath.txt','w') as f2:
                #print("%-40s" % (symbol_to_expand + " -> " + expansion), term)
                    print("%-40s" % (symbol_to_expand + " -> " + expansion), term, file=f2)
                    print('\n',file=f2)
            expansion_trials = 0
        else:
            expansion_trials += 1
            if expansion_trials >= max_expansion_trials:
                raise ExpansionError("Cannot expand " + repr(term))
        with open('samplepath.txt','w') as f2:
            print('\n',file=f2)
    return term

#ret = simple_grammar_fuzzer(grammar=rules.EXPR_GRAMMAR, max_nonterminals=2000, log=1)
#print(ret,file=f1)







def coverage_grammar_fuzzer(count_dict,sum_dict,depth_dict,count_depth_dict,f2,grammar=rules.EXPR_GRAMMAR, start_symbol=START_SYMBOL,
                          max_nonterminals=500, max_expansion_trials=1000,
                          log=True):
    term = start_symbol
    expansion_trials = 0
    while True:
        weight_list = []
        nonterminal_list = []
        depth_list = []
        f6 = open('coverage_err.txt','w')
        f6.write(term)
        f6.write('\n')
        f6.close()
        for cur_term in helper.nonterminals(term):
            if cur_term not in sum_dict:
                continue
            nonterminal_list.append(cur_term)
            weight_list.append(sum_dict[cur_term])
            depth_list.append(depth_dict[cur_term])

        if len(nonterminal_list) == 0:
            break
        # find out the most weighted nonterminal to expand
        if len(nonterminal_list)*4<max_nonterminals:
            symbol_to_expand = random.choices(nonterminal_list,weights=weight_list)[0]
        else:
            depth_sum = sum(depth_list)
            for i in range(len(depth_list)):
                depth_list[i] = depth_sum-depth_list[i]+1
            symbol_to_expand = random.choices(nonterminal_list,weights=depth_list)[0]

        #decrease the weight of this nonterminal
        sum_dict[symbol_to_expand] = max(sum_dict[symbol_to_expand]-1,1)
        expansions = grammar[symbol_to_expand]

        if len(nonterminal_list)*4<max_nonterminals:
            expansion = random.choices(expansions,weights=count_dict[symbol_to_expand])[0]
        else:
            depth_sum = sum(count_depth_dict[symbol_to_expand])
            depth_list = []
            for child_depth in count_depth_dict[symbol_to_expand]:
                 depth_list.append(depth_sum-child_depth+1)
            expansion = random.choices(expansions,weights=depth_list)[0]

        idx = grammar[symbol_to_expand].index(expansion)
        count_dict[symbol_to_expand][idx] = max(count_dict[symbol_to_expand][idx]-1,1)
        new_term = term.replace(symbol_to_expand, expansion, 1)

        if len(nonterminal_list) < max_nonterminals:
            term = new_term
            if log:
                f2.write("expand expression: ")
                f2.write(symbol_to_expand + " -> " + expansion)
                f2.write('\n')
                f2.write(term)
                f2.write('\n')
            expansion_trials = 0
        else:
            expansion_trials += 1
            if expansion_trials >= max_expansion_trials:
                raise ExpansionError("Cannot expand " + repr(term))

    return term

sdict,cdict = helper.get_expansions_count_dict()
depth_dict, cdepth_dict = helper.get_depth_dict()

count = 0
f5 = open('coverage_history.txt','w')

while(sdict[START_SYMBOL]>200000):

    f2 = open('samplepath.txt','w')
    t1 = time.time()
    ret_term = coverage_grammar_fuzzer(cdict,sdict,depth_dict,cdepth_dict,f2)
    t2 = time.time()
    f2.close()
    #print(ret_term)
    f1 = open('sample.graphql','w')
    f1.write(ret_term)
    f1.close()
    count+=1
    print("round:",count)
    print(sdict[START_SYMBOL])

    wstr = "round: "+str(count)
    f5.write(wstr)
    f5.write('\n')

    wstr = "explored: "+str(283733-sdict[START_SYMBOL])
    f5.write(wstr)
    f5.write('\n')

    wstr = "timestamp: "+str(t2-t1)
    f5.write(wstr)
    f5.write('\n')

    f5.write(ret_term)
    f5.write('\n')
    #os.system('../libgraphqlparser-master/dump_json_ast ../ababa/sample.graphql')
    f4 = open('coverage_err.txt','w')
    with open('coverage_output.txt','w') as f3:
        subprocess.run(['/Users/xinqiaoliu/Desktop/libgraphqlparser-master/dump_json_ast', '/Users/xinqiaoliu/Desktop/ababa/sample.graphql'], stdout=f3,stderr=f4)
    f4.close()
    if os.stat("coverage_err.txt").st_size != 0:
        print("error: ",  os.stat("coverage_err.txt").st_size)
        break
f5.close()
