# Day 7 — Laboratories

**Advent of Code 2025**  
https://adventofcode.com/2025/day/7

---

## Problem Summary

### Part 1
- Count how many times the beam is split
- Each `^` splits the beam to the left and right

### Part 2
- Count how many unique path permutations the beam can take to reach the bottom of the map
- Each `^` still splits the beam to the left and right

---

## Solution Overview

### Part 1
- Skipped rows containing only `.`
- Considered storing data for beams and splitters, but instead used comparisons between the current and previous rows

### Part 2
- Used an object to represent the map
- Implemented a recursive algorithm to find all possible permutations
- Wrote `pytest` unit tests for each function, method, and dataset
- Encountered performance issues with large datasets
- Resolved performance issues by adding memoization using `lru_cache`
- Reused Part 1 functions where applicable

---

## Key Takeaways

### Part 1
- Skipping blank rows significantly improved efficiency

### Part 2
- Recursive algorithms operating on large datasets benefit greatly from memoization
- Unit tests accelerated debugging by allowing development against simpler datasets
