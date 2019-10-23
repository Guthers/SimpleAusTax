#!/usr/bin/python
import sys

billingPeriods = {
	"weekly": 52, 
	"fortnightly": 26, 
	"monthly": 12,
	"yearly": 1
}

taxBrackets = {
	18200: [0, 0],
	37000: [0.19, 0],
	90000: [0.325, 3572],
	180000: [0.45, 54097]
}

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def checkArgs():
	if (len(sys.argv) != 3):
		print("Usage: run.py amount period")
		exit(1)
	amount = sys.argv[1]
	if not isInt(amount):
		print("First argument must be a number")
		exit(2)
	period = sys.argv[2]
	if period not in billingPeriods.keys():
		print("Second argument must be a valid input")
		exit(3)
	return (int(amount), period)

def main():
	amount, period = checkArgs()
	
	# Calc the total amount - multiply by period
	totalAmount = amount * billingPeriods[period]
	print(f"Amount across the year: {totalAmount}")
	
	# Progress up the tax brackets until we find the one
	i = 0 
	cutoffs = list(taxBrackets.keys())
	while (totalAmount > cutoffs[i]):
		i += 1
		if (i == len(cutoffs)):
			i -= 1
			break
	
	percentage, lump = taxBrackets[cutoffs[i]]
	print(f"This puts you in the {(0 if i == 0 else cutoffs[i-1]) + 1} to {cutoffs[i]} backet")
	print(f"Paying: {lump} plus {percentage*100}c for each dollar over over {(0 if i == 0 else cutoffs[i-1])}")

	alreadyTaxed= 0 if i == 0 else cutoffs[i-1]
	tax = lump + ((totalAmount - alreadyTaxed) *  percentage)
	
	print(f"Total paid in tax in year: \t${tax}")
	print(f"Total paid in tax in period: \t${tax/billingPeriods[period]}")

if __name__ == "__main__":
	main()
