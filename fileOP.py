# file operations
import os

# f = open('test.txt', 'r')
# print(f.name)
# print(f.mode) >> return file open type
# f.close()
with open('test.txt', 'r') as rf:
    with open('test2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# copy image file
with open('theres-no-place-like-localhost-51-1600x900.jpg', 'rb') as rf:
    with open('copy_test.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
