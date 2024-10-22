# -*- coding: utf-8 -*-
import json
import logging
import os
import subprocess

import sqlglot
import sys
import base64
import gzip
from sanic import Sanic, response

sys.setrecursionlimit(50000)

app = Sanic('sqlglot_clickzetta')

port = os.environ.get('SQLGLOT_PORT', 8530)


@app.post('/api/v1/transpile')
async def transpile_one_sql(request):
    try:
        s = request.json
        if not s:
            return response.json({
                "data": "",
                "code": 0,
                "msg": "ok"
            }, status=200)

        code = 0
        msg = 'ok'
        try:
            logging.info(f"<job id> original: {s}")
            t = sqlglot.transpile(s['sql'], read=s['read_dialect'], write='clickzetta')
            if t:
                b = base64.b64encode(gzip.compress(s['sql'].encode())).decode()
                logging.info(f"<job id> transpiled: {b}")
                return response.json({
                    "data": '\n;\n'.join(t),
                    "code": code,
                    "msg": msg
                }, status=200)
            else:
                return response.json({
                    "data": "",
                    "code": 1,
                    "msg": "transpile error, no result"
                }, status=200)
        except Exception as ex:
            logging.error(f"Error during transpilation: {str(ex)}")
            return response.json({
                "data": s['sql'],
                "code": 1,
                "msg": str(ex)
            }, status=200)
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {str(e)}")
        return response.json({
            "data": "",
            "code": 1,
            "msg": "Invalid JSON"
        }, status=400)
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return response.json({
            "description": "Internal Server Error",
            "status": 500,
            "message": "The application encountered an unexpected error and could not continue."
        }, status=500)


if __name__ == '__main__':
    print(f'port   : {port}')
    # app.run(port=port, debug=False, fast=True)
    subprocess.run(['sanic', 'sqlglot_service_sanic:app', '-p', str(port), '-w', '4', '--no-access-logs'])
