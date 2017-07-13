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


class Tooltips:
    VERSION = "Ghost Master MiniEditor v0.3.0"
    UNLIMITED_PLASM = "Affects all scenarios. \n\nPowers can be used even if \nthey appear to be too expensive."
    UNLIMITED_GOLDPLASM = "Affects all scenarios."
    INSTANT_POWER_RECHARGE = "Affects all scenarios. \n\nThis also modifies continuous powers, \nwhich are no longer channeled." \
                             "\nInstead their effects becomes permanent on \ncasting and can be stacked multiple times."
    RESPONSIVE_EMPTY_PORTRAITS = "Affects all scenarios. \n\nClicking on an empty portrait of a hidden mortal \nwill reveal his name, stats and bio button." \
                                 "\nClicking on an empty portrait of a hidden ghost \nwill reveal his name and more." \
                                 "\nPortraits of normal restless ghosts are responsive \neven without first finding them in game. (silhouette)"
    GHOST_CLONING = "Affects all scenarios. \n\nYou can choose the same ghost multiple times in Team Selection." \
                    "\nClicking on empty portraits in Team Selection is NOT recommended."
    INSIDE_OUTSIDE_ON_ALL_GHOSTS = "Affects all scenarios."
    FETTER_SHARING = "Affects all scenarios. \n\nEach fetter may be shared by multiple ghosts." \
                     "\nBecause possessed mortals are fetters, they also may be shared" \
                     "\n(extra ghosts will be benched when the possession ends)."
    IGNORE_WARDS = "Affects all scenarios."
    DISABLE_FIRE_EXTINGUISHERS = "Affects all scenarios."
    MOVABLE_RESTLESS_GHOSTS = "Affects all scenarios. \n\nYou can rebind restless ghosts to other matching fetters." \
                              "\nNOTE: bind button will work despite being greyed out."
    DISABLE_MADNESS_IMMUNITY = "Affects all scenarios. \n\nDisables madness immunity affecting certain mortals in game." \
                               "\nEnables insanity slider for those mortals (default insanity is 1%)." \
                               "\n\nDeselects current mortal to register changes."
    UNCOVER_FEARS = "Affects all scenarios. \n\nMortals start with their fears already exposed" \
                    "\n(Paranoias & Super Paranoias can be scored)."
