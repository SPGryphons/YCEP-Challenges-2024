from concurrent.futures import ProcessPoolExecutor


def check_file_for_flag(file_num):
  with open(f"flags/flags{file_num}.txt", "r") as f:
    for i, line in enumerate(f):
      if not line.startswith("YCEP24{fake_flag_"):
        print(i+1, line)
        break


if __name__ == "__main__":
  import time

  start = time.time()
  with ProcessPoolExecutor() as executor:
    executor.map(check_file_for_flag, range(10))
  
  print("Time:", time.time() - start)