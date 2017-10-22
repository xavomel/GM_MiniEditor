class Mortal:
    def __init__(self):
        self.belief = "NULL"
        self.insanity = "NULL"
        self.willpower = "NULL"
        self.fearcon = "NULL"
        self.fearsub = "NULL"
        self.fearext = "NULL"
        self.name = "NULL"

    def setBelief(self, address):
        self.belief = address

    def setInsanity(self, address):
        self.insanity = address

    def setWillpower(self, address):
        self.willpower = address

    def setFearcon(self, address):
        self.fearcon = address

    def setFearsub(self, address):
        self.fearsub = address

    def setFearext(self, address):
        self.fearext = address

    def setName(self, name):
        self.name = name


class Scenario:
    def __init__(self):
        self.max_haunters = "NULL"
        self.mean_terror = "NULL"
        self.mood = ["NULL"]

    def setMaxHaunters(self, address):
        self.max_haunters = address

    def setMeanTerror(self, address):
        self.mean_terror = address

    def setMood(self, address_list):
        self.mood = list(address_list)


class Tooltips:
    VERSION = "Ghost Master MiniEditor v0.3.5"
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
    MOVABLE_RESTLESS_GHOSTS = "Affects all scenarios. \n\nYou can rebind restless and banished ghosts to other matching fetters." \
                              "\nNOTE: bind button will work despite being greyed out."
    DISABLE_MADNESS_IMMUNITY = "Affects all scenarios. \n\nDisables madness immunity affecting certain mortals in game." \
                               "\nEnables insanity slider for those mortals (default insanity is 1%)."
    UNCOVER_FEARS = "Affects all scenarios. \n\nMortals start with their fears already exposed" \
                    "\n(Paranoias & Super Paranoias can be scored)."
    UNLOCK_MISSING_FEARS = "Affects all scenarios. \n\nFears that were previously uneditable can now" \
                           "\nbe changed (defaults to mortal's original fears)."
    DISABLE_CALMING_EFFECTS = "Affects all scenarios. \n\nPrevents mortals from calming down via" \
                              "\nnormal means or through Unearthly Calm power."
    UNLOCK_EXTRA_FEARS = "Affects all scenarios. \n\nYou can select an additional concious fear for each mortal," \
                         "\nas if they were hit with Phobia power." \
                         "\nYou can see it ingame by revealing the first concious fear."
    FIX_COLD_PHOBIA = "Affects all scenarios. \n\nCold phobia exists but there are no powers of that type." \
                      "\n\nThis changes the power type of Icy Touch and Frozen Stiff" \
                      "\nfrom normal to cold so that cold phobia may be triggered."
