#!/usr/bin/env python3

slopes = [
	[1,1], [3, 1], [5,1], [7,1], [1,2]
]

lines = open("input.txt").read().splitlines()
prod = 1

for slope in slopes:
	dx = slope[0]
	dy = slope[1]
	x = 0
	y = 0
	trees = 0

	while y < len(lines):
		if lines[y][x % len(lines[0])] == "#":
			trees += 1
		x += dx
		y += dy

	print("trees", trees)
	prod *= trees

print("product", prod)
