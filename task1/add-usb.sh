#!/bin/bash
sudo mount -t vfat /dev/sdc1 /media/usb
sudo cat /var/log/dmesg > /media/usb/dmesg.log
echo "USB device added at $(date)" >>/tmp/scripts.log
