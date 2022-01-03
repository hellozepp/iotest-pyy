#!/usr/bin/env bash
echo '1,2,3' |awk -F',' '{if(NF>2) print}'
echo '1,2,3' |awk -F',' '{if(NF>3) print;else print "sorry"}'
ps -ef | grep sendmail | awk '{cmd="kill " $2;system($cmd)}'

#输出文件追加并执行 system(cmd)执行命令
 awk '{cmd="echo aaa "$0;system(cmd)}' root.ldif
#aaa dn: cn=Kylin_Admin_Group,ou=Kylin_Group,dc=daojia,dc=com
#aaa objectClass: groupOfNames
#aaa objectClass: top
#aaa cn: ky_group
#aaa member: uid=zhanglin04,ou=Kylin_People,dc=daojia,dc=com
#aaa member: uid=ADMIN,ou=Kylin_People,dc=daojia,dc=com
