#!/usr/bin/env python3

import re

pattern = re.compile(r"^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")

lines = open("input.txt").read().splitlines()
correctcount = 0

for l in lines:
	m = pattern.match(l)
	i1 = int(m.group(1))
	i2 = int(m.group(2))
	letter = m.group(3)
	password = m.group(4)
	parity = (password[i1 - 1] == letter) + (password[i2 - 1] == letter)
	
	if parity == 1:
		correctcount += 1

print("total correct", correctcount)
