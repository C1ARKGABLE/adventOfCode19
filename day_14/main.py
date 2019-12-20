from fractions import Fraction
from pprint import pprint
import math

raw_lines = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX""".split("\n")
# with in_file as open("input.txt"):
#     raw_lines = in_file.readlines()

recipe = {}
for line in raw_lines:
    #print(line)
    reactants, product = line.split("=>")    
    reactants = reactants.split(",")
    amt_prod, product = product.strip().split(" ")
    
    final = []

    for reactant in reactants:
        amt_react,reactant = reactant.strip().split(" ")
        final.append((reactant,Fraction(int(amt_react),int(amt_prod))))

    recipe[product.strip()] = final


def get_dependants(recipe, mult=1,product="FUEL"):
    reactants = recipe[product]
    if reactants[0][0] == "ORE":
        return math.ceil(reactants[0][1])*mult
    else:
        return sum(get_dependants(recipe,mult=reactant[1],product=reactant[0]) for reactant in reactants)*mult



pprint(recipe)
print(get_dependants(recipe))
