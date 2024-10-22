import subprocess

from fastapi import FastAPI, Request
import logging
import os
import sqlglot
import sys
import base64
import gzip

sys.setrecursionlimit(50000)

app = FastAPI(summary='sqlglot_clickzetta')

port = os.environ.get('SQLGLOT_PORT', 8531)


@app.post(path='/api/v1/transpile')
async def transpile_one_sql(request: Request):
    s = await request.json()
    if not s:
        return {
            "data": "",
            "code": 0,
            "msg": "ok"
        }, 200
    code = 0
    msg = 'ok'
    try:
        logging.log(logging.INFO, f"<job id> original: {s}")
        t = sqlglot.transpile(s['sql'], read=s['read_dialect'], write='clickzetta')
        if t:
            b = base64.b64encode(gzip.compress(s['sql'].encode())).decode()
            logging.log(logging.INFO, f"<job id> transpiled: {b}")
            return {
                "data": '\n;\n'.join(t),
                "code": code,
                "msg": msg
            }, 200
        else:
            return {
                "data": "",
                "code": 1,
                "msg": "transpile error, no result"
            }, 200
    except Exception as ex:
        return {
            "data": s['sql'],
            "code": 1,
            "msg": str(ex)
        }, 200

# uvicorn sqlglot_service_fastapi:app --log-level critical --port 8531 --workers 4
if __name__ == '__main__':
    print(f'port   : {port}')
    subprocess.run(['uvicorn', 'sqlglot_service_fastapi:app', '--log-level', 'critical', '--port', str(port), '--workers', '4'])