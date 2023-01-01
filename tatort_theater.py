from puzzle import puzzle
import numpy as np
import pandas as pd
idx = pd.IndexSlice

classes = { 
            'Anordnung':    [1,2,3,4,5],
            'Zimmer':       ['blau', 'rot', 'gruen', 'weiss', 'gelb'], 
            'Name':         ['Joan', 'John', 'Martin', 'Mary', 'Marlon'], 
            'Gegenstand':   ['Whiskeyflasche', 'Seil', 'Bueste', 'Schere', 'Leuchter'], 
            'Besucher':     ['Platzanweiserin', 'Buehnenarbeiter', 'Regisseurin', 'Barkeeper', 'Maskenbildnerin'], 
            'Uhrzeit':      ['03:00', '09:00', '12:00', '18:00', '21:00'],
        }

puz = puzzle(classes)

index = (slice('blau', 'rot'), 'Joan', 'Seil', 'Regisseurin', '3:00')
print(puz.cube.loc[idx[[],:,:,['Maskenbildnerin'],:]])


import tatort_conditions as conditions

puz.set(conditions.set, mode='set')
#puz.set(conditions.unset, mode='unset')


puz.solve()
puz.return_results()
