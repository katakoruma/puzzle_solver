import numpy as np
import pandas as pd
from iteration_utilities import deepflatten


class puzzle:

    idx = pd.IndexSlice

    def __init__(self, classes=None) -> None:
        
        if classes:
            self.multiIndex = classes
            self.build_cube()


    @property
    def multiIndex(self):
        return self._multiIndex

    @multiIndex.setter
    def multiIndex(self, classes):

        self.keys = list(classes.keys())
        self.classes = classes
        self._multiIndex = pd.MultiIndex.from_product(classes.values(), names=classes.keys())

    @property
    def cube(self):
        return self._cube

    @cube.setter
    def cube(self, cube):
        self._cube = cube

    @cube.getter
    def cube(self):
        # pd.set_option('display.max_rows', len(self._cube))
        # print(self._cube)
        # pd.reset_option('display.max_rows')
        return self._cube



    def build_cube(self):

        self.cube = pd.Series(0, index=self._multiIndex)


    def set(self, *args, mode):

        for elements in list(deepflatten(args, ignore=dict)):

            if not set(elements.keys()).issubset(self.keys):
                raise(IndexError(f'Incorrect class name(s) in: {elements.keys()}'))

            for value in elements.keys():
                if not set(elements[value]).issubset(self.classes[value]):
                    raise(IndexError(f'Incorrect variable(s) in: {elements[value]}'))
                    

            for value in self.keys:
                if not value in elements:
                    elements[value] = self.classes[value]

            elements = {value: elements[value] for value in self.keys}

            if mode == 'set':
            
                elements_bu = elements.copy()
                for value in self.keys:

                    elements[value] = set(self.classes[value]) ^ set(elements[value])

                    index = pd.MultiIndex.from_product(elements.values(), names=elements.keys())
                    self._cube.loc[index] = -1

                    elements = elements_bu.copy()
                
                index = pd.MultiIndex.from_product(elements.values(), names=elements.keys())
                if all(self._cube.loc[index] == -1) and not self._cube.loc[index].empty:
                    raise(ValueError('Information are contradictory'))

            elif mode == 'unset':
                
                index = pd.MultiIndex.from_product(elements.values(), names=elements.keys())
                self._cube.loc[index] = -1

                elements_bu = elements.copy()
                for value in self.keys:

                    elements[value] = set(self.classes[value]) ^ set(elements[value])

                    index = pd.MultiIndex.from_product(elements.values(), names=elements.keys())
                    if all(self._cube.loc[index] == -1) and not self._cube.loc[index].empty:
                        raise(ValueError('Information are contradictory'))

                    elements = elements_bu.copy()

                

    def solve(self):

        change = 0

        while change <= 2:

            for value in self.keys:
                for element in self.classes[value]:

                    classes = self.classes.copy()

                    classes[value] = [element]

                    index = pd.MultiIndex.from_product(classes.values(), names=classes.keys())

                    if np.count_nonzero(self._cube.loc[index] == 0) == 1:
                        elements = self._cube.loc[index].index[self._cube.loc[index] == 0].tolist()[0]
                        self._cube.loc[elements] = 1

                        elements = {self.keys[i] : [elements[i]] for i in range(len(self.keys))}
                        elements_bu = elements.copy()

                        for val in self.keys:

                            elements = elements_bu.copy()

                            elements[val] = set(self.classes[val]) ^ set(elements[val])

                            single_index = pd.MultiIndex.from_product(elements.values(), names=elements.keys())

                            self._cube.loc[single_index] = -1

                        change = 0



            change += 1

        if np.count_nonzero(self._cube == 0) != 0 :

            print('WARNING! Puzzle cannot be solved. More information needed.')

    def possible_combinations(self, type=list):
        
        if type == list:
            return self.cube.index[self.cube == 0].tolist()
        else:
            return self.cube.index[self.cube == 0]

    def return_results(self, type=None):

        print(self.cube.index[self.cube == 1])
        if type == list:
            return self.cube.index[self.cube == 1].tolist()
        else:
            return self.cube.index[self.cube == 1]



