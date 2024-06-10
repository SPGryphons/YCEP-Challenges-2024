with open("flags.txt", "r") as f:
  for i, line in enumerate(f):
    if not line.startswith("YCEP24{fake_flag_"):
      print(i+1, line)
      break