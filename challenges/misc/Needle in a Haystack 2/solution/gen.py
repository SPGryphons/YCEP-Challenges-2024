import os
import random

flag = "YCEP24{w0w_thAT_1s_4_Re@L1Y_hU63_H4yS7@ck}\n"

def gen_fake_flag():
  return "YCEP24{fake_flag_" + os.urandom(12).hex() + "}\n"

flag_i = random.SystemRandom().randrange(0, 10000)


def gen_file_lines():
  for i in range(10000):
    if i == flag_i:
      yield flag
    else:
      yield gen_fake_flag()

with open("flags.txt", "w") as f:
  f.writelines(gen_file_lines())