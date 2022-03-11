import random
import string


def evaluate_password(password, show_info=True):
    result = False
    password_state = 0b00000

    for char in password:
        if char.isupper():
            password_state |= 0b10000
            # have_upper = True
        elif char.islower():
            password_state |= 0b01000
            # have_lower = True
        elif char.isdigit():
            password_state |= 0b00100
            # have_digit = True
        else:
            password_state |= 0b00010
            # have_punctuation = True

    if len(password) >= 8:
        password_state |= 0b00001

    # TODO:输出
    if password_state == 0b11111:
        if show_info:
            print("密码符合安全规则")
        result = True
    else:
        if show_info:
            prompt = '密码不符合安全规则，'
            if password_state & 0b00001 == 0:
                prompt += '长度不足8字符，'
            if password_state & 0b10000 == 0:
                prompt += '没有包含大写符号，'
            if password_state & 0b01000 == 0:
                prompt += '没有包含小写符号，'
            if password_state & 0b00100 == 0:
                prompt += '没有包含数字，'
            if password_state & 0b00010 == 0:
                prompt += '没有包含特殊符号，'
            prompt = prompt[:-1]
            print(prompt)
    return result


def generate_password():
    all_char_set = string.ascii_lowercase \
                 + string.ascii_uppercase \
                 + string.digits          \
                 + string.punctuation
    all_char_set *= 9
    result = ''.join(random.sample(all_char_set, k=9))
    return result


def main_userinput():
    while True:
        # TODO:用户输入密码
        user_password = input('请输入新密码:')
        # TODO:判断密码是否合格:大写、小写、数字、特殊符号、长度
        if evaluate_password(user_password):
            break


def main():
    while True:
        # TODO:生成密码
        user_password = generate_password()
        # print("密码是：",''.join(generate_password()))
        # TODO:判断密码是否合格:大写、小写、数字、特殊符号、长度
        if evaluate_password(user_password, show_info=False):
            print(f"生成密码为：{user_password}")
            break


main()
