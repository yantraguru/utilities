import os
import random
import shutil
import os.path

src_dir = 'train'
dest_dir = 'test2'
src_files = (os.listdir(src_dir))
files = [os.path.join(src_dir, f) for f in src_files]
choices = random.sample(files, 25000)

for files in choices:
	shutil.move(files, dest_dir)

