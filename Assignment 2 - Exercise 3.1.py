passes = 0  # number of passes
fails = 0 # number of fails

# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    while result != 1 and result != 2:  
        print('Incorrect result entered.')
        result = int(input('Enter result (1=pass, 2=fail): '))
        
    if result == 1:
        passes = passes + 1

        
    if result == 2:
        fails = fails + 1
2
# termination phase
print('Passed:', passes)
print('Failed:', 10 - passes)

if passes > 8:
    print('Bonus to instructor')
if fails > 8:
    print('Instructor is fired')