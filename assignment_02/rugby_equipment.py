#!/usr/bin/env python3

class KnowledgeBase:
    def __init__(self):  # A constructor used to initiaize the knowledge base

        # dictionary containing rugby equipment, their features, and suggestions
        self.equipment = {
            "boots":{"features":["metal_studs", "black"], "suggestion": "canterbury rugby boots"},
            "shorts":{"features": ["black", "large"], "suggestion": "adidas rugby short"},
            "jersey":{"features": ["short_sleeved", "black"], "suggestion": "adidas rugby jersey"},
            "rugby_ball":{"features":["white", "size_5"], "suggestion": "samurai rugby ball"},
            "hit_shield":{"features":["yellow", "medium"], "suggestion": "tessen hit shields" },
            "sausage_bags":{"features":["yellow", "short"], "suggestion": "tessen sausage bags"},
            "headgear":{"features":["black", "laced"], "suggestion": "canterbury headgear"},
            "cones":{"features": ["red"], "suggestion": "samurai cones"}
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
            for equipment in self.relationships.get(feature, []):   # check if the feature exists in the relationships dictionary
                possible[equipment] = possible.get(equipment, 0) + 1   # increase the count of how many features match each equipment

        # instead of requiring all features to match, we allow for partial matches and sort by relevance (highest match count first)
        matches = sorted(possible.keys(), key=lambda x: -possible[x])

        return matches  # return the list of matching equipment

# initialize the KnowledgeBase
kb = KnowledgeBase()

# display system information
print("\n Welcome to the Rugby Equipment Suggestion System!")
print("Available features:", ", ".join(kb.relationships.keys()))
print("\n Enter the features you want (comma-seperated): ")

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
