# if __name__=="__main__":
print("werqwefw32424242")


def xxx():
    pass


# 定义一个带有占位符的字符串
command = "INSERT INTO users(name, age) VALUES ('%s', %d)"

# 准备要插入的实际参数
processed_params = ("John", 30)

# 使用 % 操作符格式化字符串
formatted_command = command % processed_params

print(formatted_command)
