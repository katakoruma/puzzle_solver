from puzzle import puzzle
import numpy as np
import pandas as pd
idx = pd.IndexSlice

from conditions import *

puz = puzzle(tatort_theater.classes)


puz.set(tatort_theater.b6.set, mode='set')
puz.set(tatort_theater.b6.unset, mode='unset')


puz.solve()
puz.possible_combinations()
puz.return_results()
