# Day 6 — Trash Compactor

**Advent of Code 2025**  
https://adventofcode.com/2025/day/6

---

## Problem Summary

### Part 1
- Evaluate each vertical problem set using the operator (+ or *) in the bottom row
- Sum the results of all vertical problems

### Part 2
- Reconstruct numbers using cephalopod math rules, reading right to left one column at a time
- Use bottom row operators to define problem boundaries
- Sum the results of all reconstructed problems

---

## Solution Overview

### Part 1
- Parsed input into a list of numeric row and operator row lists
- Iterated column-by-column
- Applied the operator from the final row to each column's problem
- Wrote a 'pytest' unit test to validate final computation

### Part 2
- Read input as raw strings to preserve character position and spacing
- Treated input as a coordinate-based grid using (x, y) to access character locations
- Identified problem boundaries using bottom row operators
- Reconstructed numbers by reading characters vertically and skipping blank spaces
- Evaluated each problem independently and accumulated the total
- Wrote 'pytest' unit tests to validate each helper function as it was implemented

---

## Key Takeaways
- Minor changes in input structure required fundamentally different parsing strategies
- Incremental testing was essential for reasoning through and validating complex spatial logic


