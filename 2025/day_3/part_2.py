def read_input(input_file_name):
    with open (input_file_name) as file:
        lines = [x. strip() for x in file.readlines()]

    return lines

def greatest_twelve_numbers(bank: str) -> int:
    digits_needed = 12
    result = ''

    # equation: total candidates-(needed digits-1) = amount looking at
    while digits_needed > 0:
        candidate_window = len(bank) - (digits_needed-1)

        digit = max(bank[:candidate_window])
        result += digit
        digits_needed -= 1

        digit_index = bank.index(digit)
        bank = bank[digit_index+1:]

    result_as_a_number = int(result)
    return result_as_a_number

# main program
if __name__ == "__main__":
    lines = read_input("puzzle_input")
    result_list = []

    for bank in lines:
        number = greatest_twelve_numbers(bank)
        result_list.append(number)

    print(result_list)
    total = sum(result_list)
    print(f"The total is {total}")