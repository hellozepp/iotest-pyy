# coding=utf-8
class LogClient(object):
    def __init__(self, conf):
        self.conf = conf
        if 'spark.mlsql.log.driver.url' in self.conf:
            self.url = self.conf['spark.mlsql.log.driver.url']
            self.log_user = self.conf['PY_EXECUTE_USER']
            self.log_group_id = self.conf['groupId']


conf = {
    # 'spark.mlsql.log.driver.url': 'url',
    'PY_EXECUTE_USER': "xx",
    'groupId': 'g'
}
logC = LogClient(conf)
msg = "ok!"
if 'spark.mlsql.log.driver.url' not in logC.conf:
    if logC.conf['PY_EXECUTE_USER'] and logC.conf['groupId']:
        print(
            "[owner] [{}] [groupId] [{}] __MMMMMM__ {}".format(logC.conf['PY_EXECUTE_USER'], logC.conf['groupId'], msg))
    else:
        print(msg)
