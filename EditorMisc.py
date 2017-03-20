class Mortal:
    def __init__(self):
        self.belief = "NULL"
        self.insanity = "NULL"
        self.willpower = "NULL"
        self.fearcon = "NULL"
        self.fearsub = "NULL"
        self.name = "NULL"

    def setBelief(self, location):
        self.belief = location

    def setInsanity(self, location):
        self.insanity = location

    def setWillpower(self, location):
        self.willpower = location

    def setFearcon(self, location):
        self.fearcon = location

    def setFearsub(self, location):
        self.fearsub = location

    def setName(self, name):
        self.name = name


class Scenario:
    def __init__(self):
        self.max_haunters = "NULL"
        self.mood = ["NULL"]

    def setMaxHaunters(self, location):
        self.max_haunters = location

    def setMood(self, location_list):
        self.mood = list(location_list)
