file = open('student.txt','w')
file.write('Hello')
file.close()

with open('student.txt','a') as f:
    print(f.mode)
    f.write('\n added new line')
