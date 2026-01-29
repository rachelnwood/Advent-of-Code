# Day 5 — Cafeteria

**Advent of Code 2025**  
https://adventofcode.com/2025/day/5

---

## Problem Summary

### Part 1
- Calculate the number of ingredient IDs that fall within at least one freshness range.

### Part 2
- Count the total number of ingredient IDs that are considered fresh based on the given freshness ranges.

---

## Solution Overview

### Part 1
- Read ingredient IDs and freshness ranges from input files.
- Parse freshness ranges into integer tuples.
- Check if each ingredient ID falls within any range.
- Count each ID only once, even if it matches multiple ranges.

### Part 2
- Read and parse freshness ranges into integer tuples.
- Sort ranges by their starting values.
- Merge overlapping freshness ranges into a consolidated list.
- Calculate the total number of ingredient IDs covered by the merged ranges. 

---

## Key Takeaways

### Part 1
- Breaking out of loops once a match is found avoided unnecessary work.

### Part 2
- Sorting ranges simplified overlap detection.
- Merging ranges prevented double-counting ingredient IDs.