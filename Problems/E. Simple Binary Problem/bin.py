def isEven(bin1, bin2):
	if (int(list(bin1)[-1]) + int(list(bin2)[-1]))%2==0:
		return 'Yes'
	return 'No'
	
if __name__ == "__main__":
	for tc in xrange(int(raw_input())):
		bins=raw_input().split()
		print isEven(bins[0],bins[1])
