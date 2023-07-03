"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Smětala
email: x213@centrum.cz
discord: DavidS#1682
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
users = {"bob" : "123", "ann" : "pass123", "mike" : "pasword123", "liz" : "pas123"}
jmeno = input("username: ")
cara = ("-" * 40)
pocet_textu = (len(TEXTS))
if jmeno not in users or (input("password: ") != users.get(jmeno)):
    print("unregistered user, terminating the program..")
    quit(10)
else: 
    print(cara)
    print(f"Welcome to the app, {jmeno}")
    print(f"We have {pocet_textu} text to be analyzed.")
    print(cara)
    try:
        volba_textu = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")
        volba_textu = int(volba_textu)
    except ValueError:
        pass
    print(cara)
    if volba_textu not in range(pocet_textu + 1):
        print(f"Wrong input, terminating the program..")
        quit(20)    
    else:
        data_graf = {}
        pocet_slov = 0
        zacina_velkym = 0
        cele_velke = 0
        cele_male = 0
        cisla = 0
        soucet_cisel = 0
        textpom = TEXTS[volba_textu - 1]
        text = textpom.split()
        for _ in text:
            if len(_) not in data_graf: data_graf[len(_)] = 1
            else:  data_graf[len(_)] += 1
            pocet_slov += 1
            slovo = _.strip(".,")
            if slovo.istitle(): zacina_velkym += 1
            if slovo.isupper(): cele_velke += 1
            if slovo.islower(): cele_male += 1
            if slovo.isnumeric():
                cisla += 1
                soucet_cisel = soucet_cisel + int(slovo)
        print(f"{pocet_slov}, {zacina_velkym}, {cele_velke}, {cele_male}, {cisla}, {soucet_cisel}")
        print(data_graf)

            




    


