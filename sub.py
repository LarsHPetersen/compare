import sys
import subprocess

file1 = "t.py"
file2 = "diff.py"

f = open("diff.txt", "w")

diff = [
'/usr/bin/python3' ,
'./compare.py',
'-i', '{}'.format(file1),
'-o', '{}'.format(file2)
]

process = subprocess.Popen(diff, stdout=f)
f.close()
code = process.wait()

print(code)

