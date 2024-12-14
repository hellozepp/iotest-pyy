# -*- coding: utf-8 -*-
import json
from sanic.log import logger
import base64
import gzip
import os
import sys

from loguru import logger

import sqlglot
from sanic import Sanic, response
from sqlglot import Dialect

from logger import setup_log, S_LOGGING_CONFIG_DEFAULTS

APP_NAME = "sqlglot_service"

HOST_NAME = os.environ.get("POD_IP", "0.0.0.0")

sys.setrecursionlimit(50000)

app_version = "1.0.0"

port = os.environ.get("SQLGLOT_PORT", 8530)

setup_log()

app = Sanic(APP_NAME, log_config=S_LOGGING_CONFIG_DEFAULTS)


def configure_sqlglot(data):
    if "config" in data:
        config = data["config"]
        configure_string_escape(config)


def configure_string_escape(config):
    escape_type = config["string_escapes"]
    if escape_type == "QUOTE":
        Dialect.get_or_raise("clickzetta").tokenizer_class.STRING_ESCAPES = ["\\"]
    elif escape_type == "BACKSLASH":
        pass
    elif escape_type == "QUOTE_BACKSLASH":
        Dialect.get_or_raise("clickzetta").tokenizer_class.STRING_ESCAPES = ["'", '"', "\\"]


@app.post("/api/v1/transpile")
async def transpile(request):
    try:
        msg = "ok"
        data = request.json
        if data and "sql" in data and (sql := data["sql"].strip()):
            code = 0
            job_id = data.get("job_id", "")
            read_dialect = data["read_dialect"]

            configure_sqlglot(data)

            try:
                read_decode = base64.b64encode(gzip.compress(sql.encode())).decode()
                logger.info(f"{job_id}|{read_dialect} sql: {read_decode}")
                transpiled = "\n;".join(sqlglot.transpile(sql, read=read_dialect, write="clickzetta"))
                if transpiled:
                    write_decode = base64.b64encode(gzip.compress(transpiled.encode())).decode()
                    logger.info(f"{job_id}|clickzetta sql: {write_decode}")
                    return response.json(
                        {"data": transpiled, "code": code, "msg": msg}, status=200
                    )
                else:
                    return response.json({"data": "", "code": 1, "msg": "transpiled is empty"}, status=200)
            except Exception as ex:
                logger.error(f"Error during transpilation: {str(ex)}")
                return response.json({"data": sql, "code": 1, "msg": str(ex)}, status=200)
        else:
            return response.json({"data": "", "code": 0, "msg": msg}, status=200)
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {str(e)}")
        return response.json(
            {"data": "", "code": 1, "msg": f"Invalid JSON to decode, error: {str(e)}"}, status=400
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return response.json(
            {
                "description": "Internal Server Error",
                "status": 500,
                "message": f"Unexpected error: {str(e)}",
            },
            status=500,
        )


@app.get("/api/v1/version")
async def version(request):
    return response.json({"version": app_version, "code": 0}, status=200)


@app.get("/api/v1/decode")
async def decode(request):
    s = request.args.get("code")
    if not s:
        return '', 200
    return response.text(gzip.decompress(base64.b64decode(s.encode())).decode(), status=200)


@app.listener('after_server_stop')
async def finish(app, loop):
    logger.warning("Gracefully close sanic app...")
    if app and app.state and not app.state.is_stopping:
        try:
            app.stop()
        except Exception:
            pass


if __name__ == "__main__":
    logger.warning("Starting SQLGlot service...")
    logger.warning(f"host              : {HOST_NAME}")
    logger.warning(f"port              : {port}")
    logger.warning(f"app_version       : {app_version}")
    logger.warning(f"sqlglot version   : {sqlglot.__version__}")

    app.run(host=HOST_NAME, port=port, debug=False, workers=4, access_log=False)
