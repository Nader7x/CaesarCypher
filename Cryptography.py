import os

with open('files/original.txt', 'r') as file:
    lines = file.readlines()

with open('files/alphabet.txt', 'r') as file:
    alphabet_string = file.read()

after_substitution = []
after_transposition = []

# Empty the file
with open("files/output.txt", 'w'):
    pass


def append_strings_to_file(file_path, strings_to_append):
    with open(file_path, 'a') as file:
        for string in strings_to_append:
            file.write(string + '\n')


def substitute(message, alphabet):
    message = message.rstrip()
    new_message = ""
    for letter in message:
        if letter == ' ':
            new_message += letter
            continue
        index = alphabet.find(letter.lower())
        new_index = (index + 3) % 26
        if letter.isupper():
            new_message += alphabet[new_index].upper()
        else:
            new_message += alphabet[new_index]
    after_substitution.append(new_message)


def transpose(message):
    even_str = ""
    odd_str = ""

    for i in range(len(message)):
        if i % 2 == 0:
            even_str += message[i]
        else:
            odd_str += message[i]

    new_message = even_str + odd_str
    after_transposition.append(new_message)


for line in lines:
    substitute(line, alphabet_string)

for line in after_substitution:
    transpose(line.replace(" ", ""))



after_substitution.insert(0, "=========== Substitution =================")
append_strings_to_file("files/output.txt", after_substitution)
after_transposition.insert(0, "===============Transposition===================")
append_strings_to_file("files/output.txt", after_transposition)


# Taking the whole file as one word only =============================
# with open("files/original.txt", "r") as file:
#     message = file.read().replace('\n', '')
#
# with open('files/alphabet.txt', 'r') as file:
#     alphabet_string = file.read()
#
# substitute(message, alphabet_string)
# transpose(after_substitution[0].replace(" ", ""))
#
# append_strings_to_file("files/output.txt", after_substitution)
# append_strings_to_file("files/output.txt", after_transposition)
