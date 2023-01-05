
class pm:

    class v1:

        classes = { 
        'Tag':          [9,18,21,26,30],
        'Monat':        ['April', 'Juni', 'Juli', 'September', 'November'], 
        'Seitenanzahl': [3,12,17,20,31], 
        'Thema':        ['Brown. Beweg', 'Masse-Energie', 'Molekuelgroesse', 'Fotoeffekt', 'spez. Relativitaet'], 
             }

        set = []
        unset = []

        set.append({ 
                        'Monat':            ['September'], 
                        'Seitenanzahl':     [31], 
                    },)

        set.append({ 
                        'Monat':            ['Juni'], 
                        'Thema':            ['Fotoeffekt'], 
                    },)

        set.append({ 
                        'Tag':              [18], 
                        'Monat':            ['Juli'], 
                    },)

        set.append({ 
                        'Tag':              [9], 
                        'Seitenanzahl':     [17], 
                    },)
        
        set.append({ 
                        'Seitenanzahl':     [20], 
                        'Thema':            ['Molekuelgroesse'], 
                    },)

        set.append({ 
                        'Tag':              [26], 
                        'Thema':            ['spez. Relativitaet'], 
                    },)

        set.append({ 
                        'Tag':              [21], 
                        'Monat':            ['November']
                    },)


        unset.append({  
                        'Tag':              [18], 
                        'Seitenanzahl':     [3,20]
                    },)

        unset.append({ 
                        'Tag':              [21], 
                        'Seitenanzahl':     [20], 
                    },)

        unset.append({ 
                        'Thema':            ['Masse-Energie'] , 
                        'Monat':            ['April'], 
                    },)

        unset.append({ 
                        'Thema':            ['Masse-Energie'] , 
                        'Seitenanzahl':     [12], 
                    },)

    class v2:

        classes = { 
        'Name':           ['Kepler-1649c', 'Proxima b', 'Teegarden b', 'TOI-700 d', 'Trappist-1 d'], 
        'Masse':          [0.39, 1.05, 1.20, 1.27, 1.57],
        'Temperatur':     [257, 278, 296, 298, 303], 
        'Entfernung':     [4.2, 12, 41, 101, 301], 
             }

        set = []
        unset = []

        set.append({ 
                        'Name':             ['Trappist-1 d'] , 
                        'Masse':            [0.39], 
                    },)

        set.append({ 
                        'Entfernung':       [301] , 
                        #'Masse':            [1.05, 1.20, 1.27,], 
                    },) 

        set.append({ 
                        'Entfernung':       [12] , 
                        'Temperatur':       [298], 
                    },) 

        set.append({ 
                        'Temperatur':       [278] , 
                        'Masse':            [1.57], 
                    },) 

        set.append({ 
                        'Name':             ['TOI-700 d'] , 
                        'Entfernung':       [4.2], 
                    },) 



        unset.append({ 
                        'Masse':            [1.20] , 
                        'Temperatur':       [296], 
                    },)



        unset.append({ 
                        'Entfernung':       [301] , 
                        'Name':             ['Teegarden b'],
                    },)

        unset.append({ 
                        'Entfernung':       [301],
                        'Temperatur' :      [257],
                    },)
        
        unset.append({ 
                        'Name':             ['Teegarden b'],
                        'Temperatur' :      [257]
                    },)



        unset.append({ 
                        'Name':             ['Teegarden b'],
                        'Masse':            [1.27, 1.57] 
                    },)
                    
        unset.append({ 
                        'Temperatur':             [257],
                        'Masse':            [0.39, 1.05,] 
                    },)

        unset.append({ 
                        'Entfernung':       [101] , 
                        'Masse':            [1.27], 
                    },) 

        unset.append({ 
                        'Name':             ['TOI-700 d'] , 
                        'Masse':            [0.39]
                    },)

        unset.append({ 
                        'Temperatur':       [298], 
                        'Masse':            [0.39]
                    },) 
        
        unset.append({ 
                        'Entfernung':       [301] , 
                        'Masse':            [0.39, 1.57] 
                    },) 
        



class tatort_theater:

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

    class b6:

        set = []
        unset = []

        set.append([
                { 
                    'Anordnung':        [2,], 
                    'Zimmer':           ['gruen'], 
                    'Gegenstand':       ['Whiskeyflasche']
                },

                { 
                    'Anordnung':        [3,], 
                    'Zimmer':           ['weiss'], 
                    'Name':             ['Martin']
                },

                { 
                    'Anordnung':        [4,], 
                    'Zimmer':           ['blau'], 
                    'Uhrzeit':          ['18:00']
                },

                ])

        set.append({ 
                    'Name':             ['Joan'], 
                    'Gegenstand':       ['Seil'], 
                    'Uhrzeit':          ['03:00']
                    },)

        set.append({ 
                    'Besucher':         ['Platzanweiserin'], 
                    'Gegenstand':       ['Schere'], 
                    'Uhrzeit':          ['12:00']
                    },)

        set.append({ 
                    'Name':             ['Marlon'], 
                    'Gegenstand':       ['Leuchter'], 
                    },)

        set.append({ 
                    'Zimmer':           ['rot'],
                    'Besucher':         ['Buehnenarbeiter'], 
                    },)

        set.append({ 
                    'Name':             ['John'], 
                    'Besucher':         ['Regisseurin'], 
                    'Uhrzeit':          ['21:00']
                    },)



        unset.append({ 
                    'Zimmer':           ['gelb'], 
                    'Gegenstand':       ['Seil'], 
                    },)

        unset.append({ 
                    'Anordnung':        [1],
                    'Zimmer':           ['gelb'], 
                    },)

        unset.append({ 
                    'Anordnung':        [5],
                    'Gegenstand':       ['Seil'], 
                    },)

        unset.append({ 
                    'Name':             ['Joan', 'Mary'],
                    'Gegenstand':       ['Bueste'], 
                    },)
        
        unset.append({ 
                    'Name':             ['Martin', 'Marlon', 'John'],
                    'Besucher':         ['Maskenbildnerin'], 
                    },)


    class b15:

        set = []
        unset = []

        set.append([
                { 
                    'Anordnung':        [1,], 
                    'Zimmer':           ['gruen'], 
                    'Name':             ['Joan']
                },

                { 
                    'Anordnung':        [5,], 
                    'Zimmer':           ['rot'], 
                    'Besucher':         ['Regisseurin']
                },
                ])

        set.append([
                    { 
                    'Anordnung':        [2],
                    'Name':             ['Mary'], 
                    'Besucher':         ['Platzanweiserin'],
                    #'Uhrzeit':          ['18:00'],
                    },

                    { 
                    'Anordnung':        [3],
                    'Zimmer':           ['gelb'], 
                    'Uhrzeit':          ['03:00']
                    }, 

                    { 
                    'Anordnung':        [4],
                    'Gegenstand':       ['Leuchter'], 
                    'Besucher':         ['Barkeeper']
                    },                
                    ])


        set.append({ 
                    'Zimmer':           ['blau'], 
                    'Name':             ['Marlon'], 
                    'Uhrzeit':          ['12:00']
                    },)

        set.append({ 
                    'Gegenstand':       ['Whiskeyflasche'], 
                    'Uhrzeit':          ['09:00']
                    },)

        set.append(
                    { 
                    'Name':             ['Martin'], 
                    'Gegenstand':       ['Bueste']
                    },)




        unset.append([             
                    { 
                    'Zimmer':           ['gelb'], 
                    'Name':             ['Mary']
                    }, 

                    { 
                    'Zimmer':           ['gelb'], 
                    'Gegenstand':       ['Leuchter']
                    },

                    { 
                    'Name':             ['Mary'], 
                    'Gegenstand':       ['Leuchter'],
                    },
                    ])


        unset.append({ 
                    'Name':             ['Joan', 'Mary'],
                    'Gegenstand':       ['Whiskeyflasche'], 
                    },)


        unset.append([             
                    { 
                    'Zimmer':           ['weiss'], 
                    'Besucher':         ['Buehnenarbeiter']
                    }, 

                    { 
                    'Zimmer':           ['weiss'], 
                    'Gegenstand':       ['Schere']
                    },

                    { 
                    'Besucher':         ['Buehnenarbeiter'], 
                    'Gegenstand':       ['Schere']
                    },
                    ])



        

