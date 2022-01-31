#!/bin/sh
 
if [ $1 = '-s' ]; then

   killall pyarp.py -9
   echo 0 > /proc/sys/net/ipv4/ip_forward

else
  echo 1 > /proc/sys/net/ipv4/ip_forward
  ./pyarp.py $1 $2 > /dev/null &
  ./pyarp.py $2 $1 > /dev/null &
fi

