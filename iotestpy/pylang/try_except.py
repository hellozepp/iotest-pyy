import requests
import time


def get_data(url, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url)
            return response.json()
        except:
            print(f"第{i + 1}次尝试失败...")
            time.sleep(1)
    print("重试失败...")
    return None


data = get_data("https://api.example.com/data")
if data:
    print(data)


def except_call():
    print("except_call")
    return "Return from except"


def example_function():
    try:
        print("Try block")
        raise Exception("An error occurred")
    except Exception as e:
        print("Except block")
        return except_call()
    finally:
        print("Finally block")
        return "Return from finally"


result = example_function()
print("Result:", result)
