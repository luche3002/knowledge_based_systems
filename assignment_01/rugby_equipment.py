#!/usr/bin/env python3

#import the necessary modules
import collections.abc
collections.Mapping = collections.abc.Mapping
from experta import *    # Importing the Experta library, which is used to build rule-based expert systems.


# Define a knowledge-engine class for the suggestion system
# This class represents the knowledge-based suggestion system.
# It contains rules to provide suggestions for rugby equipment based on user preferences.

class Suggest(KnowledgeEngine):

    # Rules for suggesting equipment based on detailed preferences
    @Rule(Fact(category = 'boots', price_range = 'medium', feature = 'metal studs'))
    def canterbury(self):
        print("Suggested boots: Canterbury Phoenix")

    @Rule(Fact(category = 'shorts', price_range = 'high', feature = 'black'))
    def adidas(self):
        print("Suggested shorts: Adidas Rugby shorts")

    @Rule(Fact(category = 'jersey', price_range = 'low', feature = 'short sleeved'))
    def under_amour(self):
        print("Suggested jersey: Under Ammour jersey")

    # Fallback rule for equipment when only the category is specified
    @Rule(Fact(category = 'boots', price_range = 'low', feature = 'other'))
    def default_boots(self):
        print("Suggested boots: Generic rugby boots")
    @Rule(Fact(category = 'boots', price_range = 'high', feature = 'other'))
    def default_boots(self):
        print("Suggested boots: Generic rugby boots")

    @Rule(Fact(category = 'shorts', price_range = 'medium', feature = 'other'))
    def default_shorts(self):
        print("Suggested shorts: Generic rugby shorts")
    @Rule(Fact(category = 'shorts', price_range = 'low', feature = 'other'))
    def default_shorts(self):
        print("Suggested shorts: Generic rugby shorts")

    @Rule(Fact(category = 'jersey', price_range = 'medium', feature = 'long sleeved'))
    def default_jersey(self):
        print("Suggested jersey: Generic rugby jersey")
    @Rule(Fact(category = 'jersey', price_range = 'high', feature = 'other'))
    def default_jersey(self):
        print("Suggested jersey: Generic rugby jersey")

# Create an instance of the Suggest knowledge engine
engine = Suggest()
engine.reset()    # Reset the engine to prepare it for new facts (user inputs).
print("\n Welcome to the rugby equipment suggestion system! \n")

# Main program loop
while True:
    # Ask the user how they want to provide input
    preference = input ("\n Do you want to specify detailed preferences or just a category? (d/c):").strip().lower()

    # If the user wants to provide detailed preferences, collect detailed inputs for category, price range, and feature
    if preference == 'd':
        category = input("Enter the category of the equipment you want(boots/short/jersey): ").strip().lower()
        price_range = input("Enter the price range (low/medium/high): ").strip().lower()
        feature = input("Enter the feature you want: boots[metal studs/other], shorts[black/other], jersey[short sleeved/long sleeved] ").strip().lower()
        # Declare a fact (user input) to the knowledge engine
        engine.declare(Fact(category = category, price_range = price_range, feature = feature))

    # If the user wants to provide only the category, collect input for category
    elif preference == 'c':
        category = input("Enter the category of the equipment you want(boots/shorts/jersey): ").strip().lower()
        # Declare a fact (user input) to the knowledge engine
        engine.declare(Fact(category = category))

    # Incase the user provides invalid input
    else:
        print("Invalid option. Please enter 'd' for detailed or 'c' for category.")
        continue    # Skip to the next iteration of the loop

    # Run the knowledge engine to process the user's input and generate a suggestion
    print("\n Suggested Products: ")
    engine.run()

    # Ask the user if they want another recommendation
    iteration2 = input("\n Would you like another recommendation? (y/n): ").strip().lower()

    # Exit the loop if the user chooses 'n'
    if iteration2 == 'n':
        print ("\n Thank you for using the Rugby equipment Suggestion System, goodbye! ")
        break

    # Start a new iteration if the user chooses 'y'
    elif iteration2 == 'y':
        engine.reset()

    # Incase the user provides an invalid option
    else:
        input("\n Invalid option. Please enter 'y' to continue or 'n' to quit.")
        continue

    # Reset the engine for the next iteration
    engine.reset()
