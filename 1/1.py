#!/usr/bin/env python3

nums = open("input.txt").read().split()
nums = map(lambda x: int(x), nums)
nums = list(nums)

for i, a in enumerate(nums):
	for b in nums[i:]:
		if a + b == 2020:
			print(a, b)
			exit()
