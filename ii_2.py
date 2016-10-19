'''
sum = 0                         #Note the initialization of sum (to 0) before the for loop)
for i in range(0, N+1):
    sum = sum + f(i)            #This is an ADDITIVE version of the accumulator pattern

product = 1                     #Note the DIFFERENT initial condition for the accumulator
for i in range(0, N+1):
    product = product * f(i)    #This is a MULTIPLICATIVE version of the accumulator pattern

def f(a,x):
	index = len(a) - 1
	sum = a[index]
	ondex -= 1
	while index >= 0:
		sum = x * sum + a[index]
		index -= 1
	return sum
'''
                        
#LIVE CODING: (Slide 8)
import math
import argparse

def my_pi(terms):
	sign = 1
	power3 = 1
	sum = 0
	for i in range(terms):
		sum = sum + sign / ((2 * 1 + 1) * power3)
		sign = -1 * sign
		power3 = 3 * power3

	return sum * math.sqrt(12)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("TERMS", type=int)
	args = parser.parse_args()
	terms = args.TERMS
	approx_pi = my_pi (terms)
	difference = math.fabs(approx_pi - math.pi)
	print('Approx of pi after summin', terms, 'terms is', approx_pi)
	print('Percentage error relative to math.pi is {:.5%}', format(difference/math.pi))

if __name__== "__main__":
	main()