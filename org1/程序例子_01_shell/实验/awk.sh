#!/usr/bin/env bash
echo '1,2,3' |awk -F',' '{if(NF>2) print}'
echo '1,2,3' |awk -F',' '{if(NF>3) print;else print "sorry"}'
ps -ef | grep sendmail | awk '{cmd="kill " $2;system($cmd)}'