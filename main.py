alphabet_en = "abcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyz1234567890"

x = input("enter your message: ")
key = int(5)
x = x.lower()
y = ""

for letter in x:
    position = alphabet_en.find(letter)
    new_position = position + key
    if letter in alphabet_en:
        y = y + alphabet_en[new_position]


print("your cipher is:", y)