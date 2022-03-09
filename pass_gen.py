# TODO:用户输入密码
user_password = input('请输入新密码:')
# print(user_password)

# TODO:判断密码是否合格
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxuz'
DIGIT = '0123456789'
PUNCTUATION = '!@#$%^&*()_+{}|:\"<>?[];,./\\'

have_upper = False
have_lower = False
have_digit = False
have_punctuation = False

for char in user_password:
    if char in UPPER:
        have_upper = True
    if char in LOWER:
        have_lower = True
    if char in DIGIT:
        have_digit = True
    if char in PUNCTUATION:
        have_punctuation = True

is_secure = have_punctuation and have_digit and have_lower and have_upper


# TODO:输出
if is_secure == True:
    print("密码符合安全规则")
else:
    print("密码不符合规则")
