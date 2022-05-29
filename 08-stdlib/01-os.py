import os

cwd = os.getcwd()
print(cwd)

os.mkdir('files')
os.chdir('/home/iceonfire')
os.system('touch myfile.txt')

import shutil

shutil.move('/home/iceonfire/myfile.txt', cwd + '/files')
os.chdir(cwd)
shutil.copyfile('files/myfile.txt', 'files/clone.txt')
shutil.rmtree('files')

# For extra features of shutil @see https://docs.python.org/3/library/shutil.html#module-shutil

import glob

print(glob.glob('*.py')) # ['01-os.py', '02-args-parsing.py']
