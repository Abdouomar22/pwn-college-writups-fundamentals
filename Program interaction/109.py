import glob
import os
import subprocess
import time

bin_path = glob.glob('/challenge/em*')[0]

p = subprocess.Popen([bin_path], pass_fds=(1,))

time.sleep(2)




