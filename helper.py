import rules
import re

START_SYMBOL = "<Document>"
RE_NONTERMINAL = re.compile(r'(<[^<> ]*>)')

def nonterminals(expansion):
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return re.findall(RE_NONTERMINAL, expansion)

def is_nonterminal(s):
    return re.match(RE_NONTERMINAL, s)

def all_expansions(grammar=rules.EXPR_GRAMMAR):
    expansions = set()
    for key, values in grammar.items():
        for value in values:
            expansions.add(key + " -> " + value)
    return expansions

def count_dict_helper(sum_dict, count_dict, set, symbol, grammar = rules.EXPR_GRAMMAR):
    if symbol in sum_dict:
        return sum_dict[symbol]
    set.add(symbol)
    path_count = 0
    count_dict[symbol] = []
    for children in grammar[symbol]:
        children_path_count = 0
        nonterm_children = nonterminals(children)
        if len(nonterm_children)==0:
            path_count+=1
            count_dict[symbol].append(1)
            continue
        for nonterm_child in nonterm_children:
            if nonterm_child in sum_dict:
                children_path_count += sum_dict[nonterm_child]
            elif nonterm_child in set:
                children_path_count += len(grammar[nonterm_child])
                continue
            else:
                children_path_count += count_dict_helper(sum_dict, count_dict, set,nonterm_child,grammar)
                #dict[nonterm_child] = children_path_count
        count_dict[symbol].append(children_path_count)
        path_count += children_path_count
    sum_dict[symbol] = path_count
    return sum_dict[symbol]

def get_expansions_count_dict(grammar=rules.EXPR_GRAMMAR, start_symbol = START_SYMBOL):
    sum_dict = {}
    count_dict = {}

    s = set()
    count_dict_helper(sum_dict,count_dict,s,start_symbol,grammar)
    return sum_dict,count_dict

def depth_dict_helper(depth_dict,children_depth_dict,seen, start_symbol,grammar):
    if start_symbol in depth_dict:
        return depth_dict[start_symbol]
    if is_nonterminal(start_symbol)==False :
        depth_dict[start_symbol] = 1
        return 1
    if start_symbol in seen:
        return 0
    maxd = 0
    seen.add(start_symbol)
    children_depth_dict[start_symbol] = []
    for children in grammar[start_symbol]:
        depth_sum = 0
        for nonterm_child in nonterminals(children):
            child_depth = depth_dict_helper(depth_dict,children_depth_dict,seen,nonterm_child,grammar)
            maxd = max(maxd, child_depth)
            depth_sum+=child_depth
        children_depth_dict[start_symbol].append(depth_sum)
    depth_dict[start_symbol] = maxd+1
    return maxd

def get_depth_dict(grammar=rules.EXPR_GRAMMAR, start_symbol = START_SYMBOL):
    depth_dict = {}
    children_depth_dict = {}
    seen = set()
    depth_dict_helper(depth_dict,children_depth_dict,seen,start_symbol,grammar)
    return depth_dict,children_depth_dict
