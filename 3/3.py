#!/usr/bin/env python3

lines = open("input.txt").read().splitlines()
x = 0
y = 0
trees = 0

while y < len(lines):
	if lines[y][x % len(lines[0])] == "#":
		trees += 1
	x += 3
	y += 1

print("trees", trees)
