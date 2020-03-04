class Decode_String():
	def __init__(self):
		self.stack = []

	def decode(self, input_str):
		print(input_str)
		if not input_str:
			return None
		
		i = len(input_str) - 1
		replicate_str = ""
		while i >= 0:
			if input_str[i] == '[':
				j = len(self.stack) - 1
				replicate_str=""
				while j >= 0:
					if self.stack[j] == "]":
						del self.stack[j]
						break
					else:
						replicate_str += self.stack[j]
					j = j - 1
			elif input_str[i].isdigit():
				print(replicate_str)
				replicate_str *= int(input_str[i]) - 1
				print(replicate_str)
				z = len(replicate_str) - 1

				while z >= 0:
					self.stack.append(replicate_str[z])
					z = z - 1
			elif input_str[i] == ']' or input_str[i] >= 'a' or input_str[i] <= 'z':
				self.stack.append(input_str[i])
			i = i - 1
		print(self.stack)
				
				
	

obj = Decode_String()
print(obj.decode("2[abc]3[cd]ef"))
