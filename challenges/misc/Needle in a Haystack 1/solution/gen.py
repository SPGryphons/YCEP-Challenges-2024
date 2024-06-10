import os
import random

flag = "YCEP24{F1nD1n9_NeEd13S_IN_A_hay57Ack}\n"

def gen_fake_flag():
  return "YCEP24{fake_flag_" + os.urandom(10).hex()[:-1] + "}\n"

flag_i = random.SystemRandom().randrange(0, 100)


def gen_file_lines():
  for i in range(100):
    if i == flag_i:
      yield flag
    else:
      yield gen_fake_flag()


with open("flags.txt", "w") as f:
  f.writelines(gen_file_lines())