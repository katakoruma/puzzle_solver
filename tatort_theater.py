from puzzle import puzzle
import numpy as np
import pandas as pd
idx = pd.IndexSlice

from tatort_conditions import *

puz = puzzle(classes)


puz.set(a11.set, mode='set')
#puz.set(a11.unset, mode='unset')


puz.solve()
puz.possible_combinations()
puz.return_results()
