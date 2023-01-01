from puzzle import puzzle
import numpy as np
import pandas as pd
idx = pd.IndexSlice

classes = { 1: [1,2,3], 
            2: ['a','b','c'],
            3: ['A','B','C']
       }

puz = puzzle(classes)


print(puz.cube.loc[idx[slice(1, 3), :, 'B']])


set = { 1: [1,2], 
        2: ['a','b'],
       }

#puz.set(set, mode='unset')
puz.set(set, mode='set')

set = { 2: ['c'], 
        3: ['C'],
       }

puz.set(set, mode='set')

set = { 2: ['b'], 
        3: ['A'],
       }

puz.set(set, mode='set')

set = { 1: [3], 
        2: ['c'],
       }

puz.set(set, mode='set')

puz.solve()
puz.return_results()

