a = 10
b = 20
# Method 1:
def Swap1():
	a,b = b, a 
	return a,b
#Method 2:
def Swap2(a,b):
	a = a + b
	b = abs(b - a)
	a = abs(a - b)
	return "A = " + str(a) + ", B = " + str(b)

print(Swap2(500,50))
