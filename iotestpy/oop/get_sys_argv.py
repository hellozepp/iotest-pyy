import sys
import json

param = sys.argv[1]
user_info = json.loads(param)
print(f'Welcome, {user_info["Name"]}, your user id is {user_info["ID"]}.')
# python iotestpy/oop/get_sys_argv.py '{"Name":"xishuo\"", "ID":12333}'