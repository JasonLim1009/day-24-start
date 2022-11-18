# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# 220
with open('my_file.txt') as file:
    contents = file.read()
    print(contents)

with open('new_file.txt', mode='a') as file:
    file.write('\nNew text.')

# r = read
# w = write
# a = append