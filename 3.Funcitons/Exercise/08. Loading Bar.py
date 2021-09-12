# You will receive a single integer number between 0 and 100 (inclusive) which is divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function which returns a loading bar depending on the number you have received in the input. Print the result on the console.
# For more clarification see the examples below.

def loading_bar(percent):
    number_of_symbols_to_be_printed = percent // 10
    if percent == 100:
        print("100% Complete!")
        return print("[%%%%%%%%%%]")
    else:
        print(f"""{percent}% [{(number_of_symbols_to_be_printed * "%") + ((10 - number_of_symbols_to_be_printed) * ".")}]""")
    return print("Still loading...")


number = int(input())
loading_bar(number)