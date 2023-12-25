def take_string(some_string, number_chars):

    current_string = []
    for char_index in range(number_chars):
        current_string.append(some_string[char_index])
    return current_string


def skip_string(some_string, number_chars):
    for scip_index in range(number_chars):
        some_string.pop(0)
    return some_string


# Read user input
string_elements = input()
list_digits = []
list_chars = []
# Logics
for element in string_elements:
    if element.isdigit():
        list_digits.append(int(element))
    else:
        list_chars.append(element)
take_list = []
skip_list = []
for num in range(len(list_digits)):
    if num % 2 == 0:
        take_list.append(list_digits[num])
    else:
        skip_list.append(list_digits[num])
taken_string = []
take_index = 0
skip_index = 0
for command_index in range(1, len(list_digits) + 1):
    if len(list_chars) == 0:
        break
    if command_index % 2 != 0:
        current_result = take_string(list_chars, take_list[take_index])
        taken_string += current_result
        list_chars = list_chars[take_list[take_index]:]
        take_index += 1

    else:
        list_chars = skip_string(list_chars, skip_list[skip_index])
        skip_index += 1
# Output
print("".join(taken_string))
