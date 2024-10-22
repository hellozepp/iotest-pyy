import subprocess
import json

# Define the JSON data
data = {
    "sql": r"SELECT JSONExtractArrayRaw('{\"a\": \"hello\", \"b\": [-100, 200.0, \"hello\"]}', 'b')",
    "read_dialect": "starrocks",
    "job_id": "",
    "conf": {
        "string_escape": "mysql"
    }
}

# Convert the JSON data to a string
json_data = json.dumps(data)

# Write the JSON data to a file
with open('data.json', 'w') as f:
    f.write(json_data)

# Define the wrk command
wrk_command = [
    'wrk',
    '-t20',  # 20 threads
    '-d300s',  # duration of 120 seconds
    '-c500',  # 500 connections
    '-s', 'post.lua',  # Lua script for POST request
    'http://127.0.0.1:8532/api/v1/transpile'
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
