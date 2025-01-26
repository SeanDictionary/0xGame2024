#!/bin/bash
# Read the flag from the /flag file
ORIGINAL_FLAG_PATH=/home/ctf/flag
if [ -f $ORIGINAL_FLAG_PATH ]; then
    flag=$(cat $ORIGINAL_FLAG_PATH)
    # Split the flag into two parts
    flag1=${flag:0:${#flag}/2}
    flag2=${flag:${#flag}/2}
    echo $flag1 > /home/ctf/flag1
    echo $flag2 > /home/ctf/flag2
    # Remove the original flag file
    rm $ORIGINAL_FLAG_PATH
else
    echo "$ORIGINAL_FLAG_PATH file not found"
    exit 1
fi
/etc/init.d/xinetd start
sleep infinity