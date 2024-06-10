with open("flags.txt", "r") as f:
  for line in f:
    if not line.startswith("YCEP24{fake_flag_"):
      print(line)
      break