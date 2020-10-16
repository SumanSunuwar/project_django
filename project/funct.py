def smart_division(div):
	def wrapper(*args, **kwargs): # *args, **kwargs
		if args[1] == 0:
			return "Can not divide by zero"
		else:
			return div(*args)
	return wrapper


@smart_division
def division(dividend, divisor):
	return dividend / divisor


print(division(10, 5))
print(division(100, 0))



