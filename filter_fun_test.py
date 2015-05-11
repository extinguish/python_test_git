#!/usr/bin/env python
# test the filter functions
# the filter function are really useful stack on Python
scores = [55, 100, 200, -2020, 323, 1898]

def score_filter(score):
	return score >= 80 and score < 100000

# the result set are here
filtered_score = []

# this the normal processing, we will not apply this, but using 
# an even more advanced mode
for each in scores:
	if score_filter(each):
		filtered_score.append( each )

print filtered_score

# using the python built-in filter function module
print filter(score_filter, scores)

