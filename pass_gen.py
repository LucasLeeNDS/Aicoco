while True:
    # TODO:用户输入密码
    user_password = input('请输入新密码:')
    # print(user_password)

    # TODO:判断密码是否合格:大写、小写、数字、特殊符号、长度
    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER = 'abcdefghijklmnopqrstuvwxuz'
    DIGIT = '0123456789'
    # PUNCTUATION = '!@#$%^&*()_-+{}|:\"\'<>?[];,./\\'

    have_upper = False
    have_lower = False
    have_digit = False
    have_punctuation = False
    have_enough_char = (len(user_password) >= 8)

    for char in user_password:
        if char in UPPER:
            have_upper = True
        elif char in LOWER:
            have_lower = True
        elif char in DIGIT:
            have_digit = True
        else:
            have_punctuation = True

    is_secure = have_punctuation and have_digit and have_lower and have_upper \
                and have_enough_char


    # TODO:输出
    if is_secure:
        print("密码符合安全规则")
        break
    else:
        # print("密码不符合安全规则，请重新输入!")
        prompt = '密码不符合安全规则，'
        if not have_enough_char:
            # prompt = prompt + '长度不足8字符，'
            prompt += '长度不足8字符，'
        if not have_upper:
            prompt += '没有包含大写符号，'
        if not have_lower:
            prompt += '没有包含小写符号，'
        if not have_digit:
            prompt += '没有包含数字，'
        if not have_punctuation:
            prompt += '没有包含特殊符号，'
        prompt = prompt[:-1]
        print(prompt)
