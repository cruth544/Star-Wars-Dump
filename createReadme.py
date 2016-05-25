import os
import random

pictures = []
overwrite = open('README.md', 'w')
overwrite.write('')
overwrite.close()

for file in os.listdir("./Picture-Directory/"):
  if file.endswith(".jpg") or file.endswith(".png"):
    pictures.append(file)

random.shuffle(pictures)

f = open('README.md', 'a')
for pic in pictures:
  f.write("<img src='./Picture-Directory/" + pic + "'>\n")
f.close()

os.system("python createReadme.py")
os.system("git add -A")
os.system("git commint -m 'update readme'")
os.system("git push")


#print pictures
#
#print "Hello World!"
#
#
#f = open('test.txt', 'w')
#f.write('o well hi there')
#f.close()
