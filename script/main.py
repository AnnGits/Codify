from function import *
from modules import *
from command import comand

print('Добро пожаловать в Codify!')
print('Чтобы начать работу с программой, введите: 1 и нажмите Enter')
print('Чтобы завершить работу с программой, нажмите Enter')
start = input()

if start == '1':
    contin = True
else:
    print("До свидания! Хорошего дня)")


while contin:
        comand()
        print('Желаете продолжить работу [yes/no]?')
        finish = input()
        if finish == 'no':
            contin = False







