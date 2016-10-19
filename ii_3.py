# Place fingers on first and last letter
s = (input)
left = 0
right = len(s) - 1;
while left < right:
	if s[left] != s[right]:
		return False					#SyntaxError: 'return' outside fxn
	#Move fingers towards the center
	left = left +1
	right - right -1
return True

#At each step, s is the portion between fingers
while len(s) > 1:
	if s[0] != s [-1]:
		return False
	#Move fingers towards the center
	s = s[1:-1]
return True