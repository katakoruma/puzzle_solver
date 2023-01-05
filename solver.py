from puzzle import puzzle
import numpy as np
import pandas as pd
from pprint import pprint
idx = pd.IndexSlice

from conditions import *

puz = puzzle(tatort_theater.classes)


puz.set(tatort_theater.b15.set, mode='set')
puz.set(tatort_theater.b15.unset, mode='unset')

puz.solve()

print('\nPossible combinations single:\n')
puz.possible_combinations_single()

print('\nFinal results:\n')
puz.return_results()

print('\nPossible combinations:\n')
puz.possible_combinations()

for x in puz.pos_solutions_list:
    print()
    pprint(x.tolist())
