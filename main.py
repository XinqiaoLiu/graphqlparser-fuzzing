import re
import random
import rules
START_SYMBOL = "<Document>"
RE_NONTERMINAL = re.compile(r'(<[^<> ]*>)')
f1 = open('sample.graphql','w')
f2 = open('samplepath.txt','w')
def nonterminals(expansion):
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return re.findall(RE_NONTERMINAL, expansion)

def is_nonterminal(s):
    return re.match(RE_NONTERMINAL, s)

class ExpansionError(Exception):
    pass

def simple_grammar_fuzzer(grammar, start_symbol=START_SYMBOL,
                          max_nonterminals=10, max_expansion_trials=50,
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
                #print("%-40s" % (symbol_to_expand + " -> " + expansion), term)
                print("%-40s" % (symbol_to_expand + " -> " + expansion), term, file=f2)
                print('\n',file=f2)
            expansion_trials = 0
        else:
            expansion_trials += 1
            if expansion_trials >= max_expansion_trials:
                raise ExpansionError("Cannot expand " + repr(term))
        print('\n',file=f2)
    return term

ret = simple_grammar_fuzzer(grammar=rules.EXPR_GRAMMAR, max_nonterminals=30, log=1)
print(ret,file=f1)
