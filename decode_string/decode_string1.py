class Decode_string():
	def __init__(self):
		self.stack = []
	
	def decode(self, input_str):
		curnum = 0
		curstring = ''
		previous = ''

		for c in input_str:
			if c == "[":
				self.stack.append(curstring)
				self.stack.append(curnum)
				curstring =''
				curnum = 0
			elif c == ']':
				num = self.stack.pop()
				previous = self.stack.pop()
				curstring = previous + 	num*curstring
			elif c.isdigit():
				curnum = 10*curnum + int(c)
			else:
				curstring += c	
		return curstring
				


obj = Decode_string()
print(obj.decode("3[a2[bc]d]"))
