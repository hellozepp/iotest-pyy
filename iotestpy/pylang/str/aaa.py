if __name__ == "__main__":
    def fun():
        print("123")


    print("finish")
    a = '1123'
    b = f"4{a}"
    print(b)
    c = ''
    if c:
        print("oops")
    else:
        print("empty str is False")

    print("test c or a:" + (c or a))
    # a will be ignored
    print("test c or a:" + c or a)
