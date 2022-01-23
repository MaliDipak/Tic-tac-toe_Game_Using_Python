# This progam is for tik-tak-toe game
import os
from playsound import playsound
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
u = 1
while True:
    os.system("cls")
    print('T I C - T A C - T O E')
    print(f'      {a[1-1]} | {a[2-1]} | {a[3-1]} ')
    print('     ---|---|---')
    print(f'      {a[4-1]} | {a[5-1]} | {a[6-1]} ')
    print('     ---|---|---')
    print(f'      {a[7-1]} | {a[8-1]} | {a[9-1]} ')
    if a[0] == a[1] == a[2]:
        # playsound('E:\\PROGRAMMING\\Python_Program\\My_Projects\\Game_Over.mp3')
        print('# Congratulations *** :)')
        break
    elif a[3] == a[4] == a[5]:
        # playsound('E:\\PROGRAMMING\\Python_Program\\My_Projects\\Game_Over.mp3')
        print('# Congratulations *** :)')
        break
    elif a[6] == a[7] == a[8]:
        # playsound('E:\\PROGRAMMING\\Python_Program\\My_Projects\\Game_Over.mp3')
        print('# Congratulations *** :)')
        break
    elif a[0] == a[3] == a[6]:
        # playsound('E:\\PROGRAMMING\\Python_Program\\My_Projects\\Game_Over.mp3')
        print('# Congratulations *** :)')
        break
    elif a[1] == a[4] == a[7]:
        # playsound('E:\\PROGRAMMING\\Python_Program\\My_Projects\\Game_Over.mp3')
        print('# Congratulations *** :)')
        break
    elif a[2] == a[5] == a[8]:
        # playsound('E:\\PROGRAMMING\\Python_Program\\My_Projects\\Game_Over.mp3')
        print('# Congratulations *** :)')
        break
    elif a[0] == a[4] == a[8]:
        # playsound('E:\\PROGRAMMING\\Python_Program\\My_Projects\\Game_Over.mp3')
        print('# Congratulations *** :)')
        break
    elif a[2] == a[4] == a[6]:
        # playsound('E:\\PROGRAMMING\\Python_Program\\My_Projects\\Game_Over.mp3')
        print('# Congratulations *** :)')
        break
    elif u == 1:
        play = int(input('Enter Player1 Your Choice : '))
        if play > 9:
            break
        elif a[play-1] != 'X':
            a[play-1] = 'O'
            u = 2
    else:
        play = int(input('Enter Player2 Your Choice : '))
        if play > 9:
            break
        elif a[play-1] != 'O':
            a[play-1] = 'X'
            u = 1
input("\nPress any key.............")