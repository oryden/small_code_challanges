"""
https://projecteuler.net/problem=79

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""
import os


def check_if_code_ok(code, sign_ins_this_far):
    for sign_in in sign_ins_this_far:
        if code.find(sign_in[0]) < code.find(sign_in[1]) < code.find(sign_in[2]):
            pass
        else:
            return False

    # If no problems return True
    return True


# Check which numbers that are in the code
def find_unique_numbers(sign_ins):
    numbers_list = []
    for number in range(0, 10):
        for sign_in in sign_ins:
            if sign_in.find(str(number)) >= 0:
                numbers_list.append(number)
                break
    return numbers_list


# Check if there is a number that is always first
def first_number_list_creator(sign_ins):
    numbers_list = find_unique_numbers(sign_ins)
    first_number_list = []
    for number_loop in numbers_list:
        first_number = True
        for sign_in_loop in sign_ins:
            if sign_in_loop.find(str(number_loop)) > 0:
                first_number = False
                break
        if first_number:
            first_number_list.append(number_loop)

    return first_number_list


def remove_first_digit(digit, sign_ins):
    sign_ins_new = []
    for i in range(0, len(sign_ins)):
        sign_in = sign_ins[i]

        if sign_in[0] == digit:
            if len(sign_in) > 1:
                sign_ins_new.append(sign_in[1:])
        else:
            sign_ins_new.append(sign_in)

    return sign_ins_new


def main(file_path, file_name, development_print=False):
    # Read the data
    text_file = open(os.path.join(file_path, file_name), "r")
    lines = text_file.readlines()
    text_file.close()

    # Clean the data
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    sign_ins = lines

    # loop through the code
    pass_code = ""
    while len(sign_ins) > 0:

        pass_code_digit = first_number_list_creator(sign_ins)

        # Only print part solutions
        if development_print:
            print(sign_ins)
            print(pass_code_digit)

        # Algorithm doesn't work if 2 numbers are unique
        if len(pass_code_digit) > 1:
            raise ValueError("Algorithm doesn't work for this case")

        pass_code_digit_string = str(pass_code_digit[0])
        pass_code += pass_code_digit_string

        sign_ins = remove_first_digit(pass_code_digit_string, sign_ins)

    print("The shortest possible pass_code are: {}".format(pass_code))
    print("Lenght of passcode: {}".format(str(len(pass_code))))

    print("Is the produced code correct: {}".format(check_if_code_ok(pass_code, lines)))

    if development_print:
        print("Print raw data")
        print(lines)


if __name__ == '__main__':

    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "raw_data")
    file_name = "p079_keylog.txt"

    main(file_path, file_name)








