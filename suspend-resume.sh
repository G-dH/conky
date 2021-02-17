#!/bin/sh
stfile=/tmp/suspendtime

if [ "$1" = "pre" ]; then
    [ -e $stfile ] || echo 0 > $stfile; date +%s >> $stfile
fi
if [ "$1" = "post" ]; then
    t=`awk -v e=$(date +%s) 'NR==1{z=$1};NR==2{s=$1};END{printf "%.0f\n",(e-s+z)}' $stfile`
    echo $t > $stfile
fi

