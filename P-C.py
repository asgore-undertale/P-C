def P(n, r = None):
	#if not isinstance(n, int) or not isinstance(r, int): return
	
	if r == None:	r = n
	if n < r:	return
	result = 1
	for i in range(r):
		result *= n - i
	print("P("+str(n)+", "+str(r)+") = " + str(result))#
	return result

def C(n, r = None, Print = True):
	if r == None:	r = n
	if n < r:	return None
	result = P(n) / (P(n - r) * P(r))
	print("C("+str(n)+", "+str(r)+") = " + str(result))#
	return result

print("\n------------")
print(P(9, 3)*P(8, 2))
print("------------\n")
print("\n------------")
print(C(6, 4))
print("------------\n")

print("\n------------")
print(C(95, 5) == C(95, 90))
print("------------\n")