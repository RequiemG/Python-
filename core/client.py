from core.auth_client import Auth_client
def main():
    menu = [('注册','register'), ('登入','login'), ('退出','quit')]
    for index, value in enumerate(menu, 1):
        print(index, value[0])
    while True:
        try:
            ui = int(input(">>>"))
            func_str = menu[ui - 1][1]
            print(func_str)
        except ValueError:
            print("请输入数字")
        except IndexError:
            print("请输入合法数字")
        if hasattr(Auth_client,func_str):
            authobj = Auth_client()
            func = getattr(authobj,func_str)
            ret = func()



