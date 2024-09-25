user_account = 'zs'
user_password = '123456'

user_account_input = input('请输入你的账号')
user_password_input = input('请输入你的密码')

assert  user_account_input == user_account and user_password_input == user_password ,'账号密码错误'