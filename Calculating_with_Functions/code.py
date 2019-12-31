def zero(f=lambda a: a):
	return f(0)
def one(f=lambda a: a):
	return f(1)
def two(f=lambda a: a):
	return f(2)
def three(f=lambda a: a):
	return f(3)
def four(f=lambda a: a):
	return f(4)
def five(f=lambda a: a):
	return f(5)
def six(f=lambda a: a):
	return f(6)
def seven(f=lambda a: a):
	return f(7)
def eight(f=lambda a: a):
	return f(8)
def nine(f=lambda a: a):
	return f(9)

def plus(f):
	return lambda a: a + f
def minus(f):
	return lambda a: a - f
def times(f):
	return lambda a: a * f
def divided_by(f):
	return lambda a: a // f

def test():
	assert seven(times(five())) == 35
	assert four(plus(nine())) == 13
	assert eight(minus(three())) == 5
	assert six(divided_by(two())) == 3
	pass

if __name__ == "__main__":
	test()
	pass