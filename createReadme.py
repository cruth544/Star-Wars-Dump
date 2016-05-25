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
  f.write("<img src='" + pic + "'>")
f.close()
  
#print pictures
#
#print "Hello World!"
#
#
#f = open('test.txt', 'w')
#f.write('o well hi there')
#f.close()
