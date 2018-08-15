import random
import os

directory = input("storage directory name: ")
if not os.path.isdir(directory):
    try:
        os.mkdir(directory)
    except Exception as e:
        print("Unable to create directory at", os.getcwd())
        quit()

length = int(input("length of sequence: "))

assending = list(range(length))
decending = assending[::-1]

randomized = [int(random.random()*length) for _ in range(length)]

f = open("./{}/{}_ascending.txt".format(directory, length), "w")
f.write(str(length) + '\n')
f.write("\n".join(map(lambda x: str(x), assending)))
f.close()
f = open("./{}/{}_descending.txt".format(directory, length), "w")
f.write(str(length) + '\n')
f.write("\n".join(map(lambda x: str(x), decending)))
f.close()
f = open("./{}/{}_random.txt".format(directory, length), "w")
f.write(str(length) + '\n')
f.write("\n".join(map(lambda x: str(x), randomized)))
f.close()
