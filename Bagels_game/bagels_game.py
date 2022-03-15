import random
import string
import os
import time


def get_glue(target, guess):
    glue = ''
    for index in range(len(guess)):
        if guess[index] == target[index]:
            glue += '√'
        elif guess[index] in target:
            glue += '?'
        else:
            glue += 'x'
    # glue = ''.join(sorted(list(glue)))
    return glue


def main():
    ALL_DIGITS = string.digits
    MAX_TRY = 6
    NUM_DIGITS = 3

    os.system('cls')
    print(f'我想好了一个{NUM_DIGITS}位不重复的数字，你来猜猜看！')

    target = ''.join(random.sample(ALL_DIGITS, k=NUM_DIGITS))
    print(target)

    ROUND = 1
    start_time = int(time.time())
    while True:
        while True:
            guess = input('> ')
            if len(guess) == NUM_DIGITS and len(guess) == len(set(guess)) and guess.isdigit():
                break
            else:
                print(f'请输入{NUM_DIGITS}位不重复的数字')

        if guess == target:
            print('猜对了！祝贺您！')
            end_time = int(time.time())
            print(f'您总共猜了{ROUND}次用了{end_time-start_time}秒')
            break
        else:
            print(get_glue(target, guess))

        if ROUND >= MAX_TRY:
            print(f'您已经猜了{ROUND}个数字，挑战失败！')
            break

        ROUND += 1


main()
