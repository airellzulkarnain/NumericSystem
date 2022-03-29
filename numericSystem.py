def convert(base:int, num:str, to:int)->str: 
	symbols = "0123456789ABCDEF"
	num = list(num)
	result = 0
	trueResult = []
	if not(num == None) and 1 <= base <= 16: 
		validated = []
		for symbol in num: 
			validated += [symbol in symbols[:base]]
		if all(validated): 
			count = len(num)-1
			for symbol in num: 
				result += symbols.index(symbol) * base ** count
				count -= 1
			while result >= to: 
				trueResult += [symbols[result % to]]
				result //= to
			if result >= 0: 
				trueResult += [symbols[result]]
	return "".join(reversed(trueResult))

def fromAscii(words:str, to:int)->str: 
	return " ".join([convert(10, str(ord(char)), to) for char in words])

def toAscii(num:str, From:int)->str:
	return "".join([chr(int(convert(From, char, 10))) for char in num.split(" ")])