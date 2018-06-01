class Mortal:
    def __init__(self):
        self.belief = "NULL"
        self.insanity = "NULL"
        self.willpower = "NULL"
        self.terror = "NULL"
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

    def setTerror(self, address):
        self.terror = address

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
        self.mood = ["NULL"]
        self.mean_terror_push = ["NULL"]
        self.mean_terror_call = ["NULL"]

    def setMaxHaunters(self, address):
        self.max_haunters = address

    def setMood(self, address_list):
        self.mood = list(address_list)

    def setMeanTerrorPush(self, address_list):
        self.mean_terror_push = list(address_list)

    def setMeanTerrorCall(self, address_list):
        self.mean_terror_call = list(address_list)


class Constants:
    NO_OF_CHECKS = 19
    VERSION = "Ghost Master MiniEditor v0.4.2b"
    FEATURE_DISABLED = "This feature has been disabled.\n\n" \
                       "REASON:\n" \
                       "Outdated version of this feature was detected in the .exe.\n\n" \
                       "SOLUTIONS:\n" \
                       "1)\n" \
                       "Open the .exe in an older version of MiniEditor, uncheck\n" \
                       "this feature and save. The new .exe should work fine.\n" \
                       "2)\n" \
                       "Start over with a clean, unmodified .exe."
    INVALID = "All checks have FAILED - opened file is not a valid .exe"
    FAILED = "Some checks have FAILED - there are features in undefined state"
    OUTDATED = "Some features are OUTDATED - opened file was modified in an older version of MiniEditor"
    INVALID_SOLUTION = "Solutions:\n" \
                       "1)\n" \
                       "open a valid .exe"
    FAILED_SOLUTION = "Solutions for FAILED:\n" \
                      "1)\n" \
                      "reset the feature by enabling and disabling it\n" \
                      "then choose your preferred setting\n" \
                      "2)\n" \
                      "ignore it if you made any custom changes by yourself "
    OUTDATED_SOLUTION = "Solutions for OUTDATED:\n" \
                        "1)\n" \
                        "Open the .exe in specified version of MiniEditor (or older), disable the offending feature and save." \
                        " The new .exe should work fine.\n" \
                        "2)\n" \
                        "Start over with a clean, unmodified .exe."
    UNLIMITED_PLASM = "Affects all scenarios."
    UNLIMITED_GOLDPLASM = "Affects all scenarios."
    INSTANT_POWER_RECHARGE = "Affects all scenarios."
    CONTINUOUS_POWER_RECASTING = "Affects all scenarios. \n\nContinuous powers are no longer channeled." \
                                 "\nInstead their effects become permanent on \ncasting and can be stacked multiple times." \
                                 "\n\nHINT: try casting Hidden Maze a few times."
    RESPONSIVE_EMPTY_PORTRAITS = "Affects all scenarios. \n\nClicking on an empty portrait of a hidden mortal \nwill reveal his name, stats and bio button." \
                                 "\nClicking on an empty portrait of a hidden ghost \nwill reveal his name and more." \
                                 "\nPortraits of normal restless ghosts are responsive \neven without first finding them in game. (silhouette)"
    GHOST_CLONING = "Affects all scenarios. \n\nYou can choose the same ghost multiple times in Team Selection."
    INSIDE_OUTSIDE_ON_ALL_GHOSTS = "Affects all scenarios."
    FETTER_SHARING = "Affects all scenarios. \n\nEach fetter may be shared by multiple ghosts." \
                     "\nBecause possessed mortals are fetters, they also may be shared" \
                     "\n(extra ghosts will be benched when the possession ends)."
    IGNORE_WARDS = "Affects all scenarios."
    DISABLE_FIRE_EXTINGUISHERS = "Affects all scenarios."
    MOVABLE_RESTLESS_GHOSTS = "Affects all scenarios. \n\nYou can rebind restless and banished ghosts to other matching fetters."
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
    MANUAL_TERROR = "Affects current scenario. \n\nEnables terror slider for all mortals." \
                    "\n\nWARNING: selecting this option sets the terror value of all mortals to 0." \
                    "\nUnless some terror is assigned the starting plasm will also" \
                    "\nequal 0 causing an automatic loss at the start of scenario."
    GLOBAL_GHOST_LEVEL = "Affects all scenarios. \n\nChanges the training level of all ghosts." \
                         "\n\nGhosts will continue to gain experience but" \
                         "\nthey cannot level up while this option is enabled."
    GHOST_RETRAINING = "Affects all scenarios." \
                       "\n\nLearned powers can be repicked in the Ghoul Room for the original price." \
                       "\n\nWARNING: Trainspooking cinematic will no longer be displayed after" \
                       "\nWhat Lies Over the Cuckoos Nest is completed for the first time."
