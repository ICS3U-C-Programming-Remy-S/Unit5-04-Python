#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Dec 4, 2023
# This program will ask for 2 numbers
# and a operation and find the result
# of the two number to the operation


def calculate(sign, first_number, second_number):
    # statement for each operation
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        return first_number / second_number
    elif sign == "%":
        return first_number % second_number
    else:
        print("The operation entered is invalid.")


def main():
    # get nums and operation and display message to user
    print("This program will ask for 2 numbers")
    print("and an operation and find the result")
    print("of the two numbers to the operation.")
    user_num1_str = input("Please enter your first number: ")
    user_num2_str = input("Please enter your second number: ")
    user_operation_str = input("Please enter the operation you want done: ")

    # convert nums and operations
    try:
        user_num1_float = float(user_num1_str)
        user_num2_float = float(user_num2_str)
        user_operation_char = user_operation_str[0]

        # Call function and store the result
        result = calculate(user_operation_char, user_num1_float, user_num2_float)

        # Check if the input is valid
        if user_operation_char == "%" and (
            user_num2_float == 0 or user_num1_float == 0
        ):
            print(f"You can't find the remainder using 0")
        elif user_operation_char == "/" and (
            user_num2_float == 0 or user_num1_float == 0
        ):
            print(f"You can't divide using 0")
        else:
            print(
                f"{user_num1_float} {user_operation_char} {user_num2_float} = {result}"
            )

    # catch invalid input
    except Exception:
        print(
            f"{user_num1_str}, {user_operation_str}, {user_num2_str} are not valid numbers and/or operations"
        )


if __name__ == "__main__":
    main()
