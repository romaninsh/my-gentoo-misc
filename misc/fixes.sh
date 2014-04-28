#!/bin/bash

# Remove old, potentially vulnerable automake GLSA 201310-15
emerge -C sys-devel/automake-1.10.3

rm /etc/localtime
ln -sf /usr/share/zoneinfo/Europe/London /etc/localtime

rc-update add ntp-client default

emerge -u syslog-ng

rc-update add syslog-ng default

rc default

emerge -u nullmailer
emerge --config nullmailer

grep -q 10.129.216.119 /etc/nullmailer/remotes || echo '10.129.216.119 smtp' >> /etc/nullmailer/remotes


