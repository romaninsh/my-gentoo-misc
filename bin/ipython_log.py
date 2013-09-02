print $username
_ip.magic("run ipython_log.py")
print $username
print "$username"
print ($username)
print username
home="/home/"+username
home
username=romans
username="romans"
home="/home/"+username
home
devwebroot=false
devwebroot=False
import subprocess
subprocess.call(['useradd', '-G', username])
subprocess.call(['useradd', '-G', 'webmaster,upload',  username])
import os
os.makedirs.help()
help(os.makedirs)
help(os.mkdir)
os.mkdir(home)
os.mkdir(home,700)
os.mkdir(home+"/.ssh",700)
os.mkdir(home+"/web",700)
if devwebroot:
    os.mkdir(home+"/web/"+username+".devhomes.elexu.com")
    os.mkdir("/www/elexu.com/"+username+".devhomes")
help(os.chown)
f=open(home+"/.ssh/authorized_keys")
subprocess.call(['vim', home+'/.ssh/authorized_keys'])
print '''
Welcome blah blah!
====
you did great
{username} is ready
''' .format(username=username)
