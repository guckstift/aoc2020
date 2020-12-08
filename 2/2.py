#!/usr/bin/env python3

import re

pattern = re.compile(r"^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")

lines = open("input.txt").read().splitlines()
correctcount = 0

for l in lines:
	m = pattern.match(l)
	mini = int(m.group(1))
	maxi = int(m.group(2))
	letter = m.group(3)
	password = m.group(4)
	count = 0
	
	for c in password:
		if c == letter:
			count += 1
	
	if count >= mini and count <= maxi:
		correctcount += 1
		print(password, "is", "correct")
	else:
		print(password, "is", "bcrupted")

print("total correct", correctcount)
