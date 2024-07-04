###################################
##                               ##
##       Bachelors Thesis        ##
##                               ##
##  Author: Tereza Straková      ##
##  2023                         ##
###################################


from enum import Enum
from dataclasses import dataclass
from modules.color_terminal import *

@dataclass
class InputString:
    string: list[str]
    current_index: int = 0

    def __str__(self):
        return_string = ''
        for i in range(self.current_index,len(self.string)):
            return_string+='<'+self.string[i]+'> '
        return return_string
    
    def get_current_token(self):
        if not self.is_parsed():
            return self.string[self.current_index]
        else:
            return None

    def read_token(self):
        self.current_index+=1
        if not self.is_parsed():
            return self.string[self.current_index]
        else:
            return None
    
    def reset(self):
        self.current_index = 0

    def is_parsed(self):
        return self.current_index >= len(self.string)


@dataclass
class Rule:
    lhs: list[str]
    rhs: list[list[str]]
    
    def __str__(self):
        return_rule_str = '('
        for symbol in self.lhs:
            return_rule_str += '<'+symbol+'>'
        return_rule_str+=') -> ('
        first = True
        for component in self.rhs:
            if first:
                first = False
            else:
                return_rule_str += ','
            for symbol in component:
                return_rule_str += '<'+symbol+'>'

        return_rule_str+= ')'
        return return_rule_str

    
@dataclass
class Variation:
    # rules: list[Rule]
    llTable: dict

    def has_rule(self,pd_nonterminal,input_token):
        if (pd_nonterminal,input_token) in self.llTable:
            return True
        else:
            return False

    def get_rule_index(self,pd_nonterminal,input_token):
        if self.has_rule(pd_nonterminal,input_token):
            return self.llTable[(pd_nonterminal,input_token)]
        else:
            return None

class DelayList:
    def __init__(self) -> None:
        self.delay_list_dictionary = {}

    def __str__(self) -> str:
        ret = P+'Delay-List: '+W
        for r in self.delay_list_dictionary:
            ret += '\n<{}, {}>'.format(r[0], B+str(self.delay_list_dictionary[r])+W)
        ret += P+'\nkeys: '+W
        for r in self.delay_list_dictionary:
            ret += str(r)
        return ret

    # `rule` je pouzite pravidlo
    # do delayLisu sa prida jeho odlozena cast
    # tzn. pravidlo bez prvych komponentov
    def push_rule(self, rule, generation):

        if len(rule.lhs) > 1 and (generation, rule.lhs[1]) not in self.delay_list_dictionary:

            self.delay_list_dictionary[(generation, rule.lhs[1])] = Rule(rule.lhs[1:], rule.rhs[1:])


    # Delay-List[N,g] vracia odlozene casti pravidla
    # s najmensou generaciou vacsou nez `g` a
    # neterminalom `N` ako lava strana prvej komponenty pravidla
    def get_delayed_rule(self, nonterminal, generation_of_rule):
        return_min_generation = None
        return_rule = None

        # r_key je kluc v tvare (generacia, neterminal)
        for r_key in self.delay_list_dictionary:

            if r_key[1] == nonterminal and r_key[0] > generation_of_rule and (return_min_generation is None or r_key[0] < return_min_generation):
                return_min_generation = r_key[0]
                return_rule = self.delay_list_dictionary[(return_min_generation, nonterminal)]

        return return_rule, return_min_generation

    def replace_delayed_rule(self, nonterminal, rule_generation, rule):

        del self.delay_list_dictionary[(rule_generation, nonterminal)]

        self.push_rule(rule, rule_generation)
# class DelayList

class Parser:
    
    def __init__(self, input_alphabet, rules, ll_tables) -> None:
        
        self.input_alphabet = input_alphabet
        self.rules = rules
        
        self.variations = ll_tables
        self.variations_types = []

        self.pushdown = None # ? Pushdown()
        
        self.variations_results = []
        
        self.show = False

    def set_input_string(self, input_string):
        self.input_string = InputString(input_string+['$']) #input string dataclass init
    
    def set_variation_types(self, variation_types_keys):

        self.variations_types = variation_types_keys

    def set_rules(self, rules):
        self.rules = rules

    def set_input_alphabet(self,input_alphabet):
        self.input_alphabet = input_alphabet
    
    def get_variations_results(self):
        return self.variations_results
    
    def set_show(self,show):
        self.show = show

    # `rhs_first_component` is list of tokens
    # pushes symbols to pushdown in reversed order
    def push_reversal_to_pushdown(self, rhs_first_component, generation, pushing_variation=False):
        for sym in list(reversed(rhs_first_component)):
            if sym in self.input_alphabet:
                self.pushdown.push(
                    SymbolType.VARIATION_TERMINAL if pushing_variation else SymbolType.TERMINAL, sym, generation)
            else:
                self.pushdown.push(
                    SymbolType.NONTERMINAL, sym, generation)


    def generate_variations(self):
        for variation_type in self.variations_types:

            self.parse(self.variations[variation_type])

    def parse(self,variation):
        rules = self.rules
        llTable = variation.llTable


        generation = 0
        delayList = DelayList()

        self.input_string.reset()
        
        # restart
        self.pushdown = Pushdown()
        variation_result = []

        while self.pushdown.top != None:

            if self.show:
                print('------ loop started here ------')
                print(self.pushdown, 'input string:', self.input_string)

            X = self.pushdown.top
            token = self.input_string.get_current_token()
            

            if X.data == '$':

                if len(delayList.delay_list_dictionary) == 0 and token == '$':
                    self.variations_results.append(variation_result)
                    self.pushdown.pop()
                    if self.show:
                        print(GG+"=================== SUCCESS ==================="+W)
                else:
                    raise Exception("pd top $, delay list or input string not empty")


            elif X.symbolType == SymbolType.TERMINAL:

                if X.data == token:
                    self.pushdown.pop()
                    self.input_string.read_token()
                else:
                    raise Exception("internal - top terminal symbols don't match")

            
            elif X.symbolType == SymbolType.VARIATION_TERMINAL:
                variation_result.append(self.pushdown.pop())
                
                if self.show:
                    print(GG+'variation: '+W,variation_result)

            elif X.symbolType == SymbolType.NONTERMINAL:

                delayed_rule, generation_of_delayed_rule = delayList.get_delayed_rule(X.data, X.generation)

                # DelayList[N,g] not empty
                if delayed_rule is not None:
                    if self.show:
                        print(P+"rule from delayList: "+W, str(delayed_rule))

                    self.pushdown.pop()
                    first_component_rhs = delayed_rule.rhs[0]

                    if first_component_rhs[0] != 'eps':
                        self.push_reversal_to_pushdown(first_component_rhs,
                                                       generation_of_delayed_rule,
                                                       pushing_variation=True)

                    delayList.replace_delayed_rule(X.data, generation_of_delayed_rule, delayed_rule)
                

                elif (X.data, token) in llTable:

                    rule_index = llTable[(X.data, token)]
                    rule = rules[rule_index]

                    if self.show:
                        print("rule from LL Table: ",rule_index,B, rule,W)

                    generation += 1
                    self.pushdown.pop()
                    first_component_rhs = rule.rhs[0]
                    if first_component_rhs[0] == 'eps':

                        delayList.push_rule(rule, generation)
                        continue
                    self.push_reversal_to_pushdown(first_component_rhs, generation)
                    delayList.push_rule(rule, generation)
                
                else:
                    raise Exception("internal no rule for: "+str(X.data + " , " + self.input_string.get_current_token()))

            else:
                raise Exception("internal")

    
    

class Pushdown:
    def __init__(self) -> None:
        self.bottom = Symbol(symbolType=SymbolType.TERMINAL, data='$', generation=0)
        self.top = Symbol(symbolType=SymbolType.NONTERMINAL, data='S', generation=0, next_symbol=self.bottom)

    def __str__(self) -> str:
        cur = self.top
        ret = "Stack: "
        while cur:
            ret += ' '+str(cur)+''
            cur = cur.next_symbol
        return ret+'\n'

    def push(self, symbolType, data, generation):
        new_symbol = Symbol(symbolType, data, generation, next_symbol=self.top)

        self.top = new_symbol

    def pop(self):
        if self.top is None or self.top.data is None:
            return None
        
        return_popped_data = self.top.data
        
        if self.top.next_symbol is None:
            self.top = None

        else:
            new_top = self.top.next_symbol
            self.top.next_symbol = None
            self.top = new_top
        return return_popped_data


class Symbol:
    def __init__(self, symbolType, data, generation, next_symbol=None) -> None:
        self.symbolType = symbolType # TERMINAL, NONTERMINAL or VARIATION_TERMINAL
        self.data = data # symbol from alphabet
        self.generation = generation # generation of the symbol on pushdown
        self.next_symbol = next_symbol

    def __str__(self) -> str:
        if self.symbolType == SymbolType.NONTERMINAL:
            return O+'<{:>3}({}), {}>'.format(self.data, self.symbolType.name[0], str(self.generation))+W
        else:
            return G+'<{:>3}({}), {}>'.format(self.data, self.symbolType.name[0], str(self.generation))+W


class SymbolType(Enum):
    TERMINAL = 1
    NONTERMINAL = 2
    VARIATION_TERMINAL = 3