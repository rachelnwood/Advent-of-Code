# Day 2 — Gift Shop

**Advent of Code 2025**  
https://adventofcode.com/2025/day/2

---

## Problem Summary

### Part 1
- Find invalid IDs; the first half is equal to the last half
- Accumulate the invalid IDs

### Part 2
- Find invalid IDs; any sequence of repeating numbers
- Accumulate the invalid IDs 

---

## Solution Overview

### Part 1
- Loop over each range
- Check if the first half exactly matches the second half
- If the halves match, accumulate the invalid ID into the total

### Part 2
- Loop over each range
- Each individual number is checked for repeating patterns of digit_count (1, 2, 3...)
- If the number does have a repeating pattern, accumulate the invalid ID into the total

---

## Key Takeaways

### Part 1
- Odd length numbers can't have two repetitions and were filtered out

### Part 2
- Checked number length (via modulo %) by digit_count to skip processing numbers that could not be invalid