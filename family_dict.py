# # Create an empty dictionary
# animal = dict()
# # Add k/v pairs
# animal["name"] = "Kevin"
# animal["breed"] = "Bulldog"
# animal["age"] = 5

# # Create the dictionary with k/v pairs and assign to variable
# animal = {
#     "name": "Kevin",
#     "breed": "Bulldog",
#     "age": 5
# }

# for (key, value) in animal.items():
#     print(f"{key}: {value}")

# # Output
# name: Kevin
# breed: Bulldog
# age: 5

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example:
   word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["Strong"] = "To have a lot of strength"
word_definitions["Fast"] = "To be zippy"
word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Curious"] = "The desire to know stuff"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["Fast"])
print(word_definitions["Strong"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
word = word_definitions.items()
for word in words:
    print(f"The definition of {word[0]} is {word[1]}")

# another way to write the above
for (key, value) in word_definitions.items():
    print(f"{key}: {value}")

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}
for (key, value) in idioms.items():
    print(f'{key}: {" ".join(value)}')


my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

for (key, value) in my_family.items():
    name = value["name"]
    age = value["age"]
    print(f'{name} is my {key} age: {age} ')
