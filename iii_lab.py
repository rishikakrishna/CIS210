def sum_even(ar):
	sum = 0
	for i in ar:
		if i % 2 == 0:
			sum += i 
	return sum

def score_word(word):			#LEARN ABOUT DICTIONARIES
	sum = 0
	for letter in word:
		sum += VALUES{letter} 
	return sum

#q4() prints 12
#q4() returns 10

def mx_mag(li):
    mx = 0
    for x in li:
        if x < 0:
            x = 0 -x
        if x > mx:
            mx = x
    return mx

def normalize(m):
    mag = mx_mag(m)
    for i in range (len(m)):
        m[i] = m[i] / mag
        
def q3():
    x = [10,-50,-100,75]
    normalize(x)
    y = x[2]
    print(y)


