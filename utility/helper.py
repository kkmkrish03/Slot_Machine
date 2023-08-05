def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def is_string_equal_to_case_insensitive(input_string):
    return input_string.lower() == 'y' or input_string.lower() == 'yes'

def is_string_valid_boolean(input_string):
    return input_string.lower() == 'y' or input_string.lower() == 'yes' or input_string.lower() == 'n' or input_string.lower() == 'no'