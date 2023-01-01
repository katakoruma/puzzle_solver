
classes = { 
            'Anordnung':    [1,2,3,4,5],
            'Zimmer':       ['blau', 'rot', 'gruen', 'weiss', 'gelb'], 
            'Name':         ['Joan', 'John', 'Martin', 'Mary', 'Marlon'], 
            'Gegenstand':   ['Whiskeyflasche', 'Seil', 'Bueste', 'Schere', 'Leuchter'], 
            'Besucher':     ['Platzanweiserin', 'Buehnenarbeiter', 'Regisseurin', 'Barkeeper', 'Maskenbildnerin'], 
            'Uhrzeit':      ['03:00', '09:00', '12:00', '18:00', '21:00'],
        }

class a1:
    set1 = [{ 
                'Anordnung':       [1,], 
                'Zimmer':         ['weiss'], 
            },

            { 
                'Anordnung':       [2,], 
                'Zimmer':         ['gelb'], 
            },

            { 
                'Anordnung':       [3,], 
                'Zimmer':         ['gruen'], 
            },

            { 
                'Anordnung':       [4,], 
                'Zimmer':         ['blau'], 
            },

            { 
                'Anordnung':       [5,], 
                'Zimmer':         ['rot'], 
            },]

    set2  = {  
                'Zimmer':       ['gruen'], 
                'Name':         ['Mary'], 
                'Besucher':     ['Regisseurin'], 
            },

    set3 = { 
                'Gegenstand':   ['Bueste'], 
                'Besucher':     ['Buehnenarbeiter'], 
                'Uhrzeit':      ['03:00'], 
            },

    set4 = { 
                'Name':         ['Joan'], 
                'Uhrzeit':      ['21:00'], 
            },

    set5 = { 
                'Zimmer':       ['blau'], 
                'Gegenstand':   ['Leuchter'], 
                'Uhrzeit':      ['18:00'], 
            },

    set6 = { 
                'Name':         ['John'], 
                'Gegenstand':   ['Schere'], 
            },

    set7 = { 
                'Zimmer':       ['rot'], 
                'Besucher':     ['Platzanweiserin'], 
            },

    set8 = { 
                'Gegenstand':   ['Whiskeyflasche'], 
                'Besucher':     ['Barkeeper'], 
            },

    set9 = { 
                'Name':         ['John'], 
                'Uhrzeit':      ['09:00'], 
            },

    set10 = { 
                'Zimmer':       ['gelb'],
                'Name':         ['Marlon'],  
            },

    set = [set1,set2, set3, set4, set5, set6, set7, set8, set9, set10]
    unset = []

class a11:

    set = []
    unset = []

    set.append([{ 
                'Anordnung':       [1,], 
                'Zimmer':         ['blau'], 
            },

            { 
                'Anordnung':       [2,], 
                'Zimmer':         ['gelb'], 
            },

            { 
                'Anordnung':       [3,], 
                'Zimmer':         ['gruen'], 
            },

            { 
                'Anordnung':       [4,], 
                'Zimmer':         ['rot'], 
            },

            { 
                'Anordnung':       [5,], 
                'Zimmer':         ['weiss'], 
            },])

    set.append({ 
                'Zimmer':       ['gruen'], 
                'Besucher':     ['Maskenbildnerin'], 
            },)

    set.append({ 
                'Gegenstand':   ['Schere'], 
                'Uhrzeit':      ['12:00'], 
            },)

    set.append({ 
                'Zimmer':       ['rot'],
                'Name':         ['Marlon'],  
            },)

    set.append({ 
                'Gegenstand':   ['Leuchter'], 
                'Besucher':     ['Barkeeper'], 
                'Uhrzeit':      ['03:00'], 
            },)

    set.append({ 
                'Gegenstand':   ['Seil'], 
                'Name':         ['Joan'], 
                'Uhrzeit':      ['21:00'], 
            },)

    set.append({ 
                'Name':         ['Martin'],  
                'Gegenstand':   ['Whiskeyflasche'],
            },)

    set.append({  
                'Name':         ['Marlon'], 
                'Besucher':     ['Platzanweiserin'], 
            },)

    set.append({ 
                'Zimmer':       ['weiss'], 
                'Uhrzeit':      ['18:00'], 
            },)

    set.append({ 
                'Gegenstand':   ['Whiskeyflasche'], 
                'Besucher':     ['Regisseurin'], 
            },)

    set.append({ 
                'Zimmer':       ['gelb'], 
                'Besucher':     ['Buehnenarbeiter'], 
            },)

    unset.append({
                'Zimmer':          ['gruen'], 
                'Gegenstand':      ['Seil'], 
            },)

    unset.append({
                'Zimmer':          ['rot'], 
                'Gegenstand':      ['Schere'], 
            },)

    unset.append({
                'Zimmer':          ['blau'], 
                'Name':            ['Mary'], 
            },)