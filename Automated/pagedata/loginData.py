login_success_data = {"user": "admin", "passwd": "admin"}


login_null_data = [
    {"user": "admin", "passwd": "", "check": "请正确输入用户名和密码！"},
    {"user": "", "passwd": "admin", "check": "请正确输入用户名和密码！"},
    {"user": "", "passwd": "", "check": "请正确输入用户名和密码！"}
]


login_error_data = [
    {"user": "admin", "passwd": "123", "check": "用户名或密码错误！"},
    {"user": "abc", "passwd": "admin", "check": "用户名或密码错误！"},
    {"user": "abc", "passwd": "123", "check": "用户名或密码错误！"}
]