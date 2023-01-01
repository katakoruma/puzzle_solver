from puzzle import puzzle
import numpy as np
import pandas as pd


classes = { 
            'Zimmer':       ['blau', 'rot', 'gruen', 'weiss', 'gelb'], 
            'Name':         ['Joan', 'John', 'Martin', 'Mary', 'Jason'], 
            'Gegenstand':   ['Whiskeyflasche', 'Seil', 'Bueste', 'Schere', 'Pistole'], 
            'Besucher':     ['Platzanweiserin', 'Buehnenarbeiter', 'Regisseurin', 'Barkeeper', 'Maskenbildnerin'], 
            'Uhrzeit':      ['3:00', '9:00', '12:00', '18:00', '21:00'],
        }

classes = { 1: [1,2,3], 
            2: ['a','b','c'],
            3: ['A','B','C']
       }

puz = puzzle()
puz.multiIndex = classes

puz.build_cube()

idx = pd.IndexSlice
index = (slice('blau', 'rot'), 'Joan', 'Seil', 'Regisseurin', '3:00')

print(puz.cube.loc[idx[[],:,:,['Maskenbildnerin'],:]])



set = { 
            'Zimmer':       ['blau', 'rot',], 
            'Name':         ['Joan', 'John'], 
        }

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


#print(puz.cube.loc[idx[['gruen'],['Joan'],:,:,:]])

#print(np.count_nonzero(puz.cube.loc[idx[['gruen'],['Joan'],:,:,:]] == -1 ))