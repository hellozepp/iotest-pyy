import subprocess
import json

# Define the JSON data
# 加载sql文件
sql = r"SELECT JSONExtractArrayRaw('{\"a\": \"hello\", \"b\": [-100, 200.0, \"hello\"]}', 'b')"
# with open('./test.sql', 'r') as f:
#     sql = f.read()
data = {
    "sql": sql,
    "read_dialect": "clickhouse",
    "job_id": "111"
}

# Convert the JSON data to a string
json_data = json.dumps(data)

# Write the JSON data to a file
with open('data.json', 'w') as f:
    f.write(json_data)

# Define the wrk command
wrk_command = [
    'wrk',
    '-t7',  # 7 threads
    '-d1200s',  # duration of 120 seconds
    '-c200',  # -c 表示并发数
    '--timeout=30s',  #
    '-s', 'post.lua',  # Lua script for POST request
    'http://127.0.0.1:8530/api/v1/transpile'
]

# Define the Lua script for the POST request，转译json_data中的单引号
lua_script = """
wrk.method = "POST"
wrk.body   = '{}'
wrk.headers["Content-Type"] = "application/json"
""".format(json_data.replace("'", "\\'"))

# Write the Lua script to a file
with open('post.lua', 'w') as f:
    f.write(lua_script)

# wrk -t20 -d120s -c500 http://127.0.0.1:8531/api/v1/transpile
# Execute the wrk command
subprocess.run(wrk_command)
