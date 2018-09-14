x = input("enter the number=")
def fibonacci(x):
	fib1 = 0
	fib2 = 1
	for n in range(x):
		fib3 = fib1 + fib2
		print(fib3)	
		fib1 = fib2
		fib2 = fib3	


fibonacci(int(x))