width = int(input(" Enter the width  : "))
Height = int(input("Enter the Height  : "))
for w in range(width):
    for h in range(Height):
        if(w == 0 or w == width - 1 or h == 0 or h == Height - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()