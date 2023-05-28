from functools import wraps
from time import perf_counter
def do_twice(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		value = fn(*args, **kwargs)
		return value
	return wrapper

def time(fn):
	@wraps(fn)
	def timer(*args, **kwargs):
		start = perf_counter()
		value = fn(*args, **kwargs)
		end = perf_counter()
		delta = end - start
		print(f"time needed {delta:.5f}")
		return value
	return timer
	
def debug(fn):
	def wrapper_debug(*args, **kwargs):
		args_rep = [repr(a) for a in args]
		kwarg_rep = [f"{k}={v}" for k, v in kwargs.items()]
		signatue = ", ".join(args_rep + kwarg_rep)
		print(signatue)
		value = fn(*args, **kwargs)
		return value
	return wrapper_debug




def validate_input(min, max):
	def wrapper(fn):
		def inner(*args, **kwargs):
			fn(*args, **kwargs)
			for i in args:
				if isinstance(i, int) and min < i < max:
					pass
				else:
					raise ValueError("argument is not integer or/and out of range")
			
		return inner
	return wrapper
	
	
@validate_input(3, 10)
def my_func(a, b, c):
	print(a, b, c)



my_func(4,7,12)














