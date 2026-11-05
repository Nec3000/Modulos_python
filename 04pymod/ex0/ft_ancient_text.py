import sys
def main():
	if len(sys.argv) != 2:
		print("Usage: ft_ancient_text.py <file>")
		return
	fname = sys.argv[1]
	try:
		print(f"Accessing file '{fname}'")
		f = open(sys.argv[1], "r")
	except Exception as e:
		print(f"Error opening file {fname} : {e}")
		return
	text = f.read()
	print("---\n")
	print(text)
	print("\n---")
	f.close()
	print(f"File '{fname}' closed")
main()