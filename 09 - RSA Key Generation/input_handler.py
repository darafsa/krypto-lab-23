import sys
import os


# asserts that the command line arguments are larger than the specified size
def assert_arguments(size: int):
	if len(get_arguments()) < size:
		print(f"Zu wenige Argumente übergeben. ({len(get_arguments())} < {size})")
		exit()


# returns a list of arguments without the leading program name argument
def get_arguments():
	return sys.argv[1:]


# returns an argument at a specific position
def get_argument(arg_id: int):
	return get_arguments()[arg_id]


# returns the path of the output file
def get_output_file(arg_id: int):
	if not os.path.exists("out"):
		os.makedirs("out")

	return f"out/{get_arguments()[arg_id]}"


# writes a file with the specified content
def write(arg_id: int, data: str):
	with open(get_output_file(arg_id), "w", encoding="utf-8") as f:
		f.write(data)
