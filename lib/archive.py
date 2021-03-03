import random


class Archive():
    def __init__(self):
        self.abilities = openSource("abilities")
        self.appearance = openSource("appearance")
        self.behaviour = openSource("behaviour")
        self.names = openSource("names")
        self.origins = openSource("origins")
        self.races = openSource("races")
        self.surnames = openSource("surnames")
        self.talents = openSource("talents")
        self.gender = ["male", "female"]


    def shuffle(self, source_list):
        random.shuffle(source_list)
        return source_list.pop()



def openSource(file):
    f = open(f"sources/{file}.txt", "r")
    list = []
    for line in f:
        list.append(line)
    f.close()
    return list
