def read(file_name:str):
	with open(file_name, "r") as f:
		return f.read()

def write(file_name:str, data:str):
	with open(file_name, "w") as f:
		f.write(data)
