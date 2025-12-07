# input_file_name = "Sample Input"
input_file_name = "Puzzle Input"

with open (input_file_name) as file:
    lines = [x. strip() for x in file.readlines()]

dial_position = 50
zero_count = 0

def process_dial_turns():
    global dial_position
    global lines
    global zero_count

    for line in lines:
        print(f'dial rotation:', line)
        print(f'Current dial position: {dial_position}')
        rotation = int(line[1:])
        direction = line[0]

        dial_started_at_zero = False
        if dial_position == 0:
            dial_started_at_zero = True

        if direction == "L":
            dial_position -= rotation
        else:
            dial_position += rotation

        while dial_position < 0 or dial_position > 99:
            if dial_position < 0:
                dial_position += 100

                if dial_started_at_zero == False:
                    zero_count += 1
                dial_started_at_zero = False

            if dial_position > 99:
                dial_position -= 100
                if dial_position != 0:
                    zero_count += 1

        if dial_position == 0:
             zero_count += 1

        print(f"New dial position: {dial_position}")
        print(f"There are {zero_count} zeros so far")

    print(f'There are {zero_count} zeros total')
    # 5828 is a wrong answer, too low
    # 6228 is a wrong answer, too high

#main program
process_dial_turns()


#tests
# right but not crossing 0
def test_right_5():
    global dial_position
    global lines

    print("test test_right_5")
    dial_position = 50
    lines = ["R5"]
    process_dial_turns()
    assert dial_position == 55
    assert zero_count == 0

#left but not crossing 0
def test_left_5():
    global dial_position
    global lines

    print("test test_left_5")
    dial_position = 50
    lines = ["L5"]
    process_dial_turns()
    assert dial_position == 45
    assert zero_count == 0

#right but crossing 0
def test_right_65():
    global dial_position
    global lines
    global zero_count

    print("test test_right_65")
    zero_count = 0
    dial_position = 50
    lines = ["R65"]
    process_dial_turns()
    assert dial_position == 15
    assert zero_count == 1

#left but crossing 0
def test_left_65():
    global dial_position
    global lines
    global zero_count
    print("test test_left_65")

    zero_count = 0
    dial_position = 50
    lines = ["L65"]
    process_dial_turns()
    assert dial_position == 85
    assert zero_count == 1

#2 dial turns going right starting on 50
def test_2_dial_turns_right():
    global dial_position
    global lines
    global zero_count
    print("test test_2_dial_turns_right")

    zero_count = 0
    dial_position = 50
    lines = ["R200"]
    process_dial_turns()
    assert dial_position == 50
    assert zero_count == 2

#2 dial turns going left starting on 50
def test_2_dial_turns_left():
    global dial_position
    global lines
    global zero_count
    print("test test_2_dial_turns_left")

    zero_count = 0
    dial_position = 50
    lines = ["L200"]
    process_dial_turns()
    assert dial_position == 50
    assert zero_count == 2

#2 dial turns going right starting on 0
def test_2_dial_turns_right_0_start():
    global dial_position
    global lines
    global zero_count
    print("test test_2_dial_turns_right_0_start")

    zero_count = 0
    dial_position = 0
    lines = ["R200"]
    process_dial_turns()
    assert dial_position == 0
    assert zero_count == 2

#2 dial turns going left starting on 0
def test_2_dial_turns_left_0_start():
    global dial_position
    global lines
    global zero_count
    print("test test_2_dial_turns_left_0_start")

    zero_count = 0
    dial_position = 0
    lines = ["L200"]
    process_dial_turns()
    assert dial_position == 0
    assert zero_count == 2

def test_0_start_0_end_right():
    global dial_position
    global lines
    global zero_count
    print("test test_0_start_0_end_right")

    zero_count = 0
    dial_position = 0
    lines = ["R100"]
    process_dial_turns()
    assert dial_position == 0
    assert zero_count == 1

def test_0_start_0_end_left():
    global dial_position
    global lines
    global zero_count
    print("test test_0_start_0_end_left")

    zero_count = 0
    dial_position = 0
    lines = ["L100"]
    process_dial_turns()
    assert dial_position == 0
    assert zero_count == 1


# Call the tests!
# test_right_5()
# test_left_5()
# test_right_65()
# test_left_65()
# test_2_dial_turns_right()
# test_2_dial_turns_left()
# test_2_dial_turns_right_0_start()
# test_2_dial_turns_left_0_start()
# test_0_start_0_end_right()




