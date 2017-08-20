def lowestComDenom(denom1, denom2):
	if denom1 == denom2:
		return denom1
	else:
		origDenom1 = denom1
		origDenom2 = denom2
		while denom1 != denom2:
			if denom1 < denom2:
				denom1 += origDenom1
			else:
				denom2 += origDenom2
		return denom1

print(lowestComDenom(2,3))