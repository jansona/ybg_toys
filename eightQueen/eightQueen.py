
class MyStack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[len(self.items) - 1]

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	#def showTheStack(self):


def is_suitable(x0, y0, x1, y1):
	return (x0 != x1 and y0 != y1 and (x0-y0) != (x1-y1) and (x0+y0) != (x1+y1))



if __name__ == "__main__":
	BOARDSIZE = 8
	leftQueen = 8
	stack_0 = MyStack()
	stack_0.push(0)
	leftQueen -= 1
	# print(stack_0.items[0])
	adjust = False
	while(leftQueen != 0):
		# print("Left Queen is ", leftQueen)
		# print(stack_0.items)
		if adjust:
			init_num = stack_0.pop() + 1
			leftQueen += 1
		else:
			init_num = 0
		for i in range(init_num, 8):
			flag = True
			for mem in range(0, len(stack_0.items)):
				if not is_suitable(mem, stack_0.items[mem], BOARDSIZE-leftQueen, i):
					flag = False
					break
			if flag:
				stack_0.push(i)
				leftQueen -= 1
				break
		if flag:
			adjust = False
		else:
			adjust = True
			# print("It's my turn.")
	print(stack_0.items)
	for i in range(0, BOARDSIZE):
		print("#" * stack_0.items[i], end = "")
		print("O", end = "")
		print("#" * (BOARDSIZE - stack_0.items[i] - 1))




