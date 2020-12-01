import os
import random

files = os.listdir('data/')
files = random.sample(files, 30)
for file in files:
    if os.path.exists('compare/{}'.format(file)):
        continue
    os.system('python compare.py --input data/{}'.format(file))
