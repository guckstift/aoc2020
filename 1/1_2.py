#!/usr/bin/env python3

nums = open("input.txt").read().split()
nums = map(lambda x: int(x), nums)
nums = list(nums)

while len(nums) > 0:
	a = nums.pop(0)
	bs = nums[:]
	
	while len(bs) > 0:
		b = bs.pop(0)
		cs = bs[:]
		
		while len(cs) > 0:
			c = cs.pop(0)
			
			if a + b + c == 2020:
				print(a, b, c)
				exit()
