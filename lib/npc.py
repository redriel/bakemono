from . import archive


class NPC():
    def __init__(self):
        self.archive = archive.Archive()
        self.ability = self.archive.shuffle(self.archive.abilities).strip()
        self.appearance = self.archive.shuffle(self.archive.appearance).strip()
        self.behaviour = self.archive.shuffle(self.archive.behaviour).strip()
        self.name = self.archive.shuffle(self.archive.names).strip()
        self.origin = self.archive.shuffle(self.archive.origins).strip()
        self.race = self.archive.shuffle(self.archive.races).strip().strip()
        self.surname = self.archive.shuffle(self.archive.surnames).strip()
        self.talent = self.archive.shuffle(self.archive.talents).strip()
        self.gender = self.archive.shuffle(self.archive.gender).strip()
        self.pronoun = "he" if self.gender == "male" else "she"

    def stringify(self):
        self.pronoun = "he" if self.gender == "male" else "she"
        line1 = (f"You meet a {self.gender} {self.race} named {self.name} {self.surname}.\n")
        line2 = (f"{self.name} appears {self.ability}.\n")
        line3 = (f"You notice {self.pronoun} has {self.appearance}.\n")
        line4 = (f"{self.pronoun.capitalize()} tells you {self.pronoun} is a {self.origin}.\n")
        line5 = (f"Few knows that {self.name} {self.talent}.\n")
        line6 = (f"{self.name} seems {self.behaviour}.\n")
        npc_string = ""
        return npc_string.join((line1, line2, line3, line4, line5, line6))
