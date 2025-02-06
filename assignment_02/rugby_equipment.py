#!/usr/bin/env python3

class KnowledgeBase:
    def __init__(self):  # A constructor used to initiaize the knowledge base

        # dictionary containing rugby equipment, their features, and suggestions
        self.equipment = {
            "boots":{"features":["metal_studs", "black"],"price_range":["high", "medium", "low"], "suggestion": "canterbury rugby boots"},
            "shorts":{"features": ["black", "large"], "price_range":["high", "medium", "low"], "suggestion": "adidas rugby short"},
            "jersey":{"features": ["short_sleeved", "black"], "price_range":["high", "medium", "low"], "suggestion": "adidas rugby jersey"},
            "rugby_ball":{"features":["white", "size_5"], "price_range": ["high", "medium", "low"], "suggestion": "samurai rugby ball"},
            "hit_shield":{"features":["yellow", "medium"], "price_range":["high", "medium", "low"], "suggestion": "tessen hit shields" },
            "sausage_bags":{"features":["yellow", "short"], "price_range":["high", "medium", "low"], "suggestion": "tessen sausage bags"},
            "headgear":{"features":["black", "laced"], "price_range": ["high", "medium", "low"], "suggestion": "canterbury headgear"},
            "cones":{"features": ["red"], "price_range":["high", "medium", "low"], "suggestion": "samurai cones"},
            }

        # dictionary mapping each feature to possible equipment
        self.relationships = {
            "metal_studs": ["boots"],
            "black": ["boots", "shorts", "jersey", "headgear"],
            "large": ["shorts"],
            "short_sleeved": ["jersey"],
            "white": ["rugby_ball"],
            "size_5": ["rugby_ball"],
            "yellow": ["hit_shield", "sausage_bags"],
            "medium": ["hit_shield"],
            "short": ["sausage_bags"],
            "laced": ["headgear"],
            "red": ["cones"]
            }

    # determines equipment to be suggested based on the features provided by the user
    def get_equipment(self, features):
        # dictionary used to check occurences of equipment based on the features provided
        possible = {}
        for feature in features:  # iterate through the features provided by the user
            for equipment in self.relationshps.get(feature, []):   # check if the feature exists in the relationships dictionary
                possible[equipment] = possible.get(equipment, 0) + 1   # increase the count of how many features match each equipment

        # list to store equipment where all required features match
        matches = []
        for equipment, count in possible.items():
            required_features = self.equipment[equipment]["features"]
            # ensure all required features are present and count matches
            if count == len(required_features) and all (s in features for s in required_features):
                matches.append(equipment)

        return matches  # return the list of matching equipment

# create and instance for the KnowledgeBase
kb = KnowledgeBase()

# display system information
print("\n Welcome to the Rugby Equipment Suggestion System!")
print("Available features:", ", ".join(kb.relationships.keys()))
print("\n Enter the features you want (coma-seperated): ")

# get user input and clean it
user_input = input("> ").lower().replace(" ", "_").split(',')
features = [f.strip() for f in user_input if f.strip() in kb.relationships]

#check if the user entered valid features
if not features:
    print("\n Invalid features entered. Please try again.")
else:
    # get possible suggestions based on the features
    suggestions = kb.get_equipment(features)

    # display results
    if suggestions:
        print("\n Possible suggestions:")
        for equipment in suggestions:
            print(f"- {equipment}: {kb.equipment[equipment]['suggestion']}")   # display equipment name and suggestion
    else:
        print("\n No matching suggestion found.")
