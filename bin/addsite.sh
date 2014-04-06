#!/bin/bash

export short="$1"  # such as "myproj"
export domain="$2" # such as "myproj.com" , without www


export server=`cat /etc/nginx/server_domain`   # such as "aries.exposuredigital.com"

[ "$server" ] || {
  echo "You must define server inside /etc/nginx/server_domain"
}


[ "$domain" ] || {
  echo "addsite.sh <shorname> <domain>

e.g.: addsite.sh myproj02 myproj.net"
  exit
}

# generate config
[ -f "/etc/nginx/conf.d/$short.conf" ] || {
  cat /etc/nginx/conf.d/_sample | 
    sed "s/SHORT/$short/g; s/SERVER/$server/g; s/DOMAIN/$domain/g" > /etc/nginx/conf.d/$short.conf
}

# generate folder
(
  cd /www
  mkdir -p $short
  ./fixperm.sh
)

/etc/init.d/nginx reload

echo "Temporary link http://$short.$server  permanint link http://$domain"
