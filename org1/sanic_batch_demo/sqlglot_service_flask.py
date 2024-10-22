import json
import logging
import subprocess

from flask import Flask, request
import os
import sqlglot
import sys
import base64
import gzip

sys.setrecursionlimit(50000)

app = Flask('sqlglot_clickzetta')

port = os.environ.get('SQLGLOT_PORT', 8532)


@app.route('/api/v1/transpile', methods=['POST'])
def transpile_one_sql():
    s = request.json
    if not s:
        return """{
    "data": "",
    "code": 0,
    "msg": "ok"
}""", 200
    code = 0
    msg = 'ok'
    try:
        logging.log(logging.INFO, f"<job id> original: {s}")
        t = sqlglot.transpile(s['sql'], read=s['read_dialect'], write='clickzetta')
        if t:
            b = base64.b64encode(gzip.compress(s['sql'].encode())).decode()
            logging.log(logging.INFO, f"<job id> transpiled: {b}")
            return json.dumps({
                "data": '\n;\n'.join(t),
                "code": code,
                "msg": msg
            }), 200
        else:
            return json.dumps({
                "data": "",
                "code": 1,
                "msg": "transpile error, no result"
            }), 200
    except Exception as ex:
        return json.dumps({
            "data": s['sql'],
            "code": 1,
            "msg": str(ex)
        }), 200


if __name__ == '__main__':
    print(f'port   : {port}')
    # 使用 gunicorn 启动 flask 服务
    # subprocess.run(['gunicorn', 'sqlglot_service_flask:app', '--log-level', 'critical', '-b', f"127.0.0.1:{str(port)}", '-w', '4'])
    subprocess.run(['uvicorn', 'sqlglot_service_flask:app', '--log-level', 'critical', '--port', str(port), '--workers', '4'])
