dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary['cat'])
print(phone_numbers['Suzy'])

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

# hanging indents 
# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

# Example 2:
phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }

# accessing the dict 

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for item in pol_eng_dictionary:
    print(item) 

# outputs: zamek
#          woda
#          gleba


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
print(dictionary)
dictionary['cat'] = 'minou'
print(dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
print(dictionary)
dictionary['swan'] = 'cygne'
print(dictionary)


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
print(dictionary)
del dictionary['dog']
print(dictionary)
dictionary.popitem()
print(dictionary)
