grocery_item = "Grilled Chicken Salad"
length_of_item = len(grocery_item)
first_char = grocery_item[0]
second_char = grocery_item[8]
third_char = grocery_item[16]
last_char1 = grocery_item[6]
last_char2 = grocery_item[14]
last_char3 = grocery_item[20]

# Testing
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)

words = grocery_item.split() 

first_chars = []
last_chars  = []

for w in words:
    first_chars.append(w[0])
    last_chars .append(w[-1])

print("First chars:", first_chars)   # ['G', 'C', 'S']
print("Last chars: ", last_chars)    # ['d', 'n', 'd']

first_chars_2 = [w[0]  for w in words]
last_chars_2  = [w[-1] for w in words]