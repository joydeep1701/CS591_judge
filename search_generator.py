import random
import os

directory = "search"
if not os.path.isdir(directory):
    try:
        os.mkdir(directory)
    except Exception as e:
        print("Unable to create directory at", os.getcwd())
        quit()

# length = int(input("length of sequence: "))
for length in range(100,20000,100):
    ascending = list(range(length))
    randomized = sorted([int(random.random()*length*100) for _ in range(length)])

    f = open("./{}/{}_ascending_search.txt".format(directory, length), "w")
    f.write(str(length) + '\n')
    f.write("\n".join(map(lambda x: str(x), ascending)))
    f.close()

    f = open("./{}/{}_random_search.txt".format(directory, length), "w")
    f.write(str(length) + '\n')
    f.write("\n".join(map(lambda x: str(x), randomized)))
    f.close()