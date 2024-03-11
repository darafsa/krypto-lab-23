import sys
import os


def assert_arguments(size: int):
	if len(get_arguments()) < size:
		print(f"Zu wenige Argumente übergeben. ({len(get_arguments())} < {size})")
		exit()


def get_arguments():
	return sys.argv[1:]


def get_input_file(arg_id: int):
	return f"res/{get_arguments()[arg_id]}"


def get_output_file(arg_id: int):
	if not os.path.exists("out"):
		os.makedirs("out")

	return f"out/{get_arguments()[arg_id]}"


def get_key(arg_id: int):
	return int(get_arguments()[arg_id])


def read(arg_id: int):
	with open(get_input_file(arg_id), "r") as f:
		return f.read()


def write(arg_id: int, data: str):
	with open(get_output_file(arg_id), "w") as f:
		f.write(data)
