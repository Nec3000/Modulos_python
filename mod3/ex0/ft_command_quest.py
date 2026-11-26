import sys

print(f"Program name: {sys.argv[0]}")
if (len(sys.argv) == 1):
	print("No arguments provided!")
else:
	print(f"Arguments received: {len(sys.argv) - 1}")
	count = 1
	for arg in sys.argv[1:]:
		print(f"Argument {count}: {arg}")
		count += 1
print(f"Total arguments: {len(sys.argv)}")