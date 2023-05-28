def generate_fibonacci(stop=10):
	current_fib, next_fib = 0, 1
	for _ in range(0, stop):
		fib_number = current_fib
		current_fib, next_fib = next_fib, current_fib + next_fib
		yield fib_number


print(list(generate_fibonacci()))

gen_num = (elem + 5 for elem in range(10))
for i in gen_num:
	print(i)
