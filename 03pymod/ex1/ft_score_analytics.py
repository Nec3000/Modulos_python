import sys
def convert_arg(arg: str) -> int | None:
	try:
		return int(arg)
	except ValueError:
		print(f"Invalid parameter: {arg}")
		return None
print("=== Player Score Analytics ===")
scores = [score for arg in sys.argv[1:]
          if (score := convert_arg(arg)) is not None]
if len(scores) == 0:
	print("No scores provided. Usage:", end=" ")
	print("python3 ft_score_analytics.py <score1> <score2> ...")
else:
	print(f"Scores processed: {scores}")
	print(f"Total players: {len(scores)}")
	print(f"Total score: {sum(scores)}")
	print(f"High score: {max(scores)}")
	print(f"Low score: {min(scores)}")
	print(f"Score range: {max(scores) - min(scores)}")
	