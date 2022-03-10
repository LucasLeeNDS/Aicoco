import string

while True:
    # TODO:用户输入密码
    user_password = input('请输入新密码:')
    # print(user_password)

    # TODO:判断密码是否合格:大写、小写、数字、特殊符号、长度
    # UPPER = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # LOWER = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxuz'
    # DIGIT = string.digits  # '0123456789'
    # PUNCTUATION = '!@#$%^&*()_-+{}|:\"\'<>?[];,./\\'

    password_state = 0b00000
    # have_upper = False
    # have_lower = False
    # have_digit = False
    # have_punctuation = False
    # have_enough_char = (len(user_password) >= 8)

    for char in user_password:
        if char in string.ascii_uppercase:
            password_state |= 0b10000
            # have_upper = True
        elif char in string.ascii_lowercase:
            password_state |= 0b01000
            # have_lower = True
        elif char in string.digits:
            password_state |= 0b00100
            # have_digit = True
        else:
            password_state |= 0b00010
            # have_punctuation = True

    if len(user_password) >= 8:
        password_state |= 0b00001

    # is_secure = have_punctuation and have_digit and have_lower and have_upper and have_enough_char
    # is_secure = (password_state == 0b11111)

    # TODO:输出
    if password_state == 0b11111:
        print("密码符合安全规则")
        break
    else:
        # print("密码不符合安全规则，请重新输入!")
        prompt = '密码不符合安全规则，'
        if password_state & 0b00001 == 0:
            # prompt = prompt + '长度不足8字符，'
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
