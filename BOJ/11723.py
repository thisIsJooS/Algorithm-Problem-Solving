import sys
input = sys.stdin.readline

S = 0b00
 
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'all':
        S = 0b111111111111111111110
        
    elif command[0] == 'empty':
        S = 0b0
        
    else:
        oper, x = command
        x = int(x)
        if oper == 'add':
            if 0b1<<x & S != 0b1<<x:
                S = S | 0b1<<x

        elif oper == 'check':
            if 0b1<<x & S == 0b1<<x:
                print(1)
            else:
                print(0)
            
        elif oper == 'remove':
            if 0b1<<x & S == 0b1<<x:
                S = S & ~(0b1<<x)
            
        elif oper == 'toggle':
            if 0b1<<x & S == 0b1<<x:
                S = S & ~(0b1<<x)
            else:
                S = S | 0b1<<x

                
# 입력예시 1
# 26
# add 1
# add 2
# check 1
# check 2
# check 3
# remove 2
# check 1
# check 2
# toggle 3
# check 1
# check 2
# check 3
# check 4
# all
# check 10
# check 20
# toggle 10
# remove 20
# check 10
# check 20
# empty
# check 1
# toggle 1
# check 1
# toggle 1
# check 1

# 출력예시 1
# 1
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 1
# 0
# 0
# 0
# 1
# 0
