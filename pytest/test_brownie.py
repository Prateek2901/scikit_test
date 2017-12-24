import brownie
import pandas as pd
from random import randint , choice
import string

df=pd.read_csv("merge.csv")
rating = list(df['Rating'])
title = list(df['Title'])



# in list movie
def test_in_name():
	i = randint(0,len(title))
	t = str(title[i])
	rate = brownie.fun_name(t)
	assert rate == rating[i]
"""

out of list testing

"""
"""
def test_out_name():
	i = randint(0,len(title))
	t = title[i]
	if i%3 == 0:
		#add one character
		ch = choice(string.ascii_letters)
		pos = randint(0,len(t)-1)
		a_t = t[:pos]+ch+t[pos:]
		rate = brownie.fun_name(a_t)
		assert rate == rating[i]
	elif i%3 == 1:
		pos = randint(0,len(t)-1)
		s_t = t[:pos-1]+t[pos:]
		rate = brownie.fun_name(s_t)
		assert rate == rating[i]		
	else:
		#substitute one character with another one.
		pos = randint(0,len(t)-1)
		ch = choice(string.ascii_letters)
		sub_t = t[:pos-1]+ch+t[pos:]
		rate = brownie.fun_name(sub_t)
		assert round(rate,2) == rating[i]		
"""


def test_out_name():
	i = randint(0,len(title))
	t = title[i]
	if i%2 == 0:
		#add one character
		ch = choice(string.ascii_letters)
		pos = randint(0,len(t)-1)
		a_t = t[:pos]+ch+t[pos:]
		rate = brownie.fun_name(a_t)
		assert rate == rating[i]
	elif i%2 == 1:
		pos = randint(0,len(t)-1)
		s_t = t[:pos-1]+t[pos:]
		rate = brownie.fun_name(s_t)
		assert rate == rating[i]