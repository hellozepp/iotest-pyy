curl -X POST http://127.0.0.1:8530/api/v1/transpile \
-H "Content-Type: application/json" \
-d '{
    "sql": "SELECT JSONExtractArrayRaw(\"{\\\"a\\\": \\\"hello\\\", \\\"b\\\": [-100, 200.0, \\\"hello\\\"]}\", \"b\")",
    "read_dialect": "starrocks",
    "job_id": "",
    "conf": {
        "string_escape": "mysql"
    }
}'