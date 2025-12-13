def read_input(input_file_name):
    with open (input_file_name) as file:
        lines = [x. strip() for x in file.readlines()]

    return lines

def greatest_two_numbers(bank):
    first_number = max(bank[:len(bank)-1])
    index = bank.index(first_number)

    second_number = max(bank[index+1:])

    result = int(first_number + second_number)
    return result

# main program
if __name__ == "__main__":
    lines = read_input("puzzle_input")
    result_list = []

    for bank in lines:
        number = greatest_two_numbers(bank)
        result_list.append(number)

    print(result_list)
    total = sum(result_list)
    print(f"The total is {total}")
