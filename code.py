import random

def generate_name(filename1, filename2):
    file1 = open(filename1)
    names = [i.strip() for i in file1]

    file2 = open(filename2)
    surnames = [i.strip() for i in file2]
    file1.close()
    file2.close()

    fullname = random.choice(names) + ' ' + random.choice(surnames)
    return fullname
