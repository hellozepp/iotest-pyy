# coding=utf-8
import json
import re
#need py3 version ,取直接下游,过滤间接的
strParm = ""
with open("/opt/projects/python/iotest-pyy/org1/mytest/daojia/sy_dw_f.f_agt_order_info.csv", "w",
          encoding='utf-8-sig') as f:
    jobSet = set({})
    with open("/opt/projects/python/iotest-pyy/org1/mytest/daojia/json", "r")as f1:
        for line in f1:
            strParm += line
    with open("/opt/projects/python/iotest-pyy/org1/mytest/daojia/1", "r")as f2:
        for line1 in f2:
            jobSet.add(line1.strip())
    list = json.loads(strParm).get("nodes")
    f.write("任务名" + "," + "所有者\n")
    for val in list:
        # get one job info
        name = val.get("value").get("label").strip()
        if name in jobSet:
            id = val.get("id")
            tip = val.get("tip")
            owner = ""
            if len(tip) >= 2:
                ownerStr = tip[1]
                tag = re.search("所有者：</span><b>(?P<owner_pattern>.+?)</b>", ownerStr)
                if tag and tag.group('owner_pattern'):
                    owner = tag.group('owner_pattern')
            f.write(name + "," + owner + "\n")
