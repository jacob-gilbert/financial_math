import json

def readJsonFile():
    with open('incomeTax.json', "r") as file:
        return json.load(file)
    
class State:
    def __init__(self, name, bracket):
        self.name = name
        self.tax_bracket = self.convert_bracket(bracket)
        
    def convert_bracket(self, bracket):
        return bracket
        
    def __str__(self):
        return f"{self.name}: {self.tax_bracket}"
    
class StateIncomeTax:
    def __init__(self):
        # States are keys and the values are a list of tuples (a, b) where
        # a means income > a and b is the tax pecent
        self.state_map = dict()
        self.data = readJsonFile()
        
        # set state_map with states' tax info
        self.no_tax()
        self.flat_tax()
        self.graduated_tax()
    
    def no_tax(self):
        no_tx = self.data["no_tax"]
        for key, value in no_tx["states"].items():
            self.state_map[key] = State(key, [(0, value)])
       
    def flat_tax(self): 
        flat_tx = self.data["flat_rate"]
        for key, value in flat_tx["states"].items():
            self.state_map[key] = State(key, [(0, value)])
            
    def graduated_tax(self):
        grad_tx = self.data["vary_rate"]
        for key, value in grad_tx["states"].items():
            temp = []
            for key2, value2 in value.items():
                temp.append((int(key2), value2))
            self.state_map[key] = State(key, temp)
            
    def get_state_info(self, state):
        return self.state_map[state]
            
    def determine_tax(self, state, income):
        # get state information
        if state in self.state_map:
            state_info = self.state_map[state].tax_bracket
            
            # will need to computer deductions at some point
            
            # determine if state has a flat rate or no tax
            if len(state_info) == 1:
                tax_prct = state_info[0][1]
                tax = (income * tax_prct // 100)
                return tax, income - tax
            else:
                tot_tx = 0
                income_copy = income
                prv_cap = 0
                for i in range(len(state_info) - 1):
                    # if this is zero we have accounted for all our income
                    if income_copy == 0:
                        break
                    
                    # get cap for the current tax percent
                    inc = state_info[i + 1][0]
                    txprct = state_info[i][1]
                    #print("Range:", inc - prv_cap, income_copy, (inc - prv_cap) * txprct // 100)
                    if income_copy - (inc - prv_cap) >= 0:
                        tot_tx += (inc - prv_cap) * txprct // 100
                        income_copy = max(income_copy - (inc - prv_cap), 0)
                    else:
                        tot_tx += income_copy * txprct // 100
                        income_copy = 0
                    prv_cap = inc
                if income_copy > 0:
                    tot_tx += income_copy * state_info[i + 1][1] // 100
                return (tot_tx, income - tot_tx)
                
        else:
            print("Error, input was not a valid State")
        
        pass
        
a = StateIncomeTax()
print(a.determine_tax("Texas", 60000))
print(a.determine_tax("Pennsylvania", 60000))
print(a.determine_tax("Maine", 60000)) #- (15000 + 5216)))
print(a.get_state_info("Maine"))