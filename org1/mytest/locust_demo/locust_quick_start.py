from locust import HttpUser, task, between, constant
import os
import webbrowser


class QuickstartUser(HttpUser):
    # between模拟同一个用户前后操作的等待时间随机（1-5秒）
    wait_time = between(1, 5)
    # constant固定用户前后操作时间为5秒
    # wait_time = constant(5)

    """压力脚本模板开始"""

    @task(3)  # 需要压测的接口都需要加task，后面的数据为权重，默认权重1
    def function1(self):

        # 请求数据
        data = {"request": "{'serviceId':'report.getTest'}", "messageType": "json"}
        # 请求地址
        refresh_url = ":8157/datacent/unity/queryForJson//"
        # 请求头
        headers = {'Content-Type': "application/x-www-form-urlencoded;charset=UTF-8", "apiKey": "HIS5", "operator": "1"}

        # 开始模拟请求，“catch_response=True”为断言标记支持，如果不加，断言标记报错
        with self.client.post(url=refresh_url, data=data, headers=headers, verify=False,
                              catch_response=True) as refresh_res:
            # 请求结束进入断言，断言方式与requests请求断言完全相同，根据需要编写。
            if refresh_res.json()["code"] == "00000":
                # 断言成功，标记成功
                refresh_res.success()
            else:
                # 断言成功，标记失败
                refresh_res.failure("select_1_from_dual失败")

    """压力脚本模板结束"""

    def on_start(self):
        # 点击开始压测时，所有用户都会去运行一次，如：用做模拟登录，采用self.client模拟登录接口
        print("开始压测")

    def on_stop(self):
        # 点击stop时，所有用户都会去运行一次。
        print("结束压测结束")


if __name__ == '__main__':
    # 控制浏览器打开locust页面
    webbrowser.open_new_tab('http://localhost:8089')
    # 控制cmd执行locust，“locust_2022_2_12.py”为需要运行py脚本名字，“http://192.168.3.194”为压测服务器地址
    os.system("locust -f locust_quick_start.py --host=http://127.0.0.1 ")
