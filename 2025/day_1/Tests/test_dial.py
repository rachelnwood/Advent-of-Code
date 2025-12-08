from day_1.Day_1_Part_2_Main import process_dial_turns

# right but not crossing 0
def test_right_5():
    dial_position = 50
    lines = ["R5"]
    zero_count = 0
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 55
    assert zero_count == 0

#left but not crossing 0
def test_left_5():
    dial_position = 50
    lines = ["L5"]
    zero_count = 0
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 45
    assert zero_count == 0

#right but crossing 0
def test_right_65():
    zero_count = 0
    dial_position = 50
    lines = ["R65"]
    zero_count = 0
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 15
    assert zero_count == 1

#left but crossing 0
def test_left_65():
    zero_count = 0
    dial_position = 50
    lines = ["L65"]
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 85
    assert zero_count == 1

#2 dial turns going right starting on 50
def test_2_dial_turns_right():
    zero_count = 0
    dial_position = 50
    lines = ["R200"]
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 50
    assert zero_count == 2

#2 dial turns going left starting on 50
def test_2_dial_turns_left():
    zero_count = 0
    dial_position = 50
    lines = ["L200"]
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 50
    assert zero_count == 2

#2 dial turns going right starting on 0
def test_2_dial_turns_right_0_start():
    zero_count = 0
    dial_position = 0
    lines = ["R200"]
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 0
    assert zero_count == 2

#2 dial turns going left starting on 0
def test_2_dial_turns_left_0_start():
    zero_count = 0
    dial_position = 0
    lines = ["L200"]
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 0
    assert zero_count == 2

def test_0_start_0_end_right():
    zero_count = 0
    dial_position = 0
    lines = ["R100"]
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 0
    assert zero_count == 1

def test_0_start_0_end_left():
    zero_count = 0
    dial_position = 0
    lines = ["L100"]
    dial_position, zero_count = process_dial_turns(dial_position, lines, zero_count)
    assert dial_position == 0
    assert zero_count == 1