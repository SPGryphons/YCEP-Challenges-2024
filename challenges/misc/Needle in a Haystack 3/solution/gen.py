import os
from concurrent.futures import ProcessPoolExecutor

FLAG = "YCEP24{7H3sE_HAYstAcK5_@r3_6eTtIN9_OU7_oF_h4Nd!}\n"
NUM_LINES = 10000
NUM_FILES = 10
FLAG_LINE = 7429
FLAG_FILE = 8



def gen_fake_flag():
  return "YCEP24{fake_flag_" + os.urandom(15).hex() + "}\n"


def gen_file_lines(lines, flag_line=None):
  for i in range(lines):
    if flag_line is not None and i == flag_line:
      yield FLAG
    else:
      yield gen_fake_flag()


def gen_file(file_num, lines, flag_line=None):
  with open(f"./flags/flags{file_num}.txt", "w") as f:
    f.writelines(gen_file_lines(lines, flag_line))

if __name__ == "__main__":
  import time

  start = time.time()

  with ProcessPoolExecutor() as executor:
    for i in range(NUM_FILES):
      if i == FLAG_FILE:
        executor.submit(gen_file, i, NUM_LINES, FLAG_LINE)
      else:
        executor.submit(gen_file, i, NUM_LINES)

  print("Time:", time.time() - start)