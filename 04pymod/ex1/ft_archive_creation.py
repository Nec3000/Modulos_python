import sys
import typing
def get_f(fname : str, mode : str) -> typing.IO[str]:
	try:
		return open(fname, mode)
	except Exception as e:
		print(f"Error opening file {fname} : {e}")
		return None
def dump_text(text : str) -> None:
	print("---\n")
	print(text)
	print("\n---")
def save_text(text : str) -> None:
	fname2 = input("Enter new file name (or empty):")	
	if not fname2:
		print("Not saving data")
		return
	print(f"Saving data to '{fname2}'")
	f2 = get_f(fname2, "w")
	if f2 is None:
		return
	f2.write(text)
	print(f"Data saved in file '{fname2}'.\n")
	f2.close()
def main():
	if len(sys.argv) != 2:
		print(f"Usage: {sys.argv[1]} <file>")
		return
	fname = sys.argv[1]
	print(f"Accessing file '{fname}'")
	f = get_f(fname, "r")
	if f is None:
		return
	text = f.read()
	dump_text(text)
	f.close()
	print(f"File '{fname}' closed")
	replaced = text.replace("\n", "#\n")
	print("\nTransform data:")
	dump_text(replaced)
	save_text(replaced)
main()