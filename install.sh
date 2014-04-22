#!/bin/bash

( cd /usr/local/bin; ln -sf /etc/my/bin/* . )
( cd /etc; ln -sf /etc/my/etc/motd.d . )
( cd /etc/cron.daily/; ln -sf /etc/my/bin/update-motd . )
