#!/usr/bin/python

import sys
import subprocess
import os
#import rlib.webrootbind
import pwd
import grp

username = sys.argv[1]
home="/home/"+username
devwebroot=False

subprocess.call(['useradd', '-G', 'webmaster,upload',  username])

uid=pwd.getpwnam(username).pw_uid
gid=grp.getgrnam(username).gr_gid


os.mkdir(home,0o700)
os.mkdir(home+"/.ssh",0o700)
os.mkdir(home+"/web",0o700)

if devwebroot:
    os.mkdir(home+"/web/"+username+".devhomes.elexu.com")
    os.mkdir("/www/elexu.com/"+username+".devhomes")

os.chown(home,uid,gid)
os.chown(home+"/.ssh",uid,gid)
os.chown(home+"/web",uid,gid)

subprocess.call(['vim', home+'/.ssh/authorized_keys'])

os.chmod(home+'/.ssh/authorized_keys',0o600)
os.chown(home+"/.ssh/authorized_keys",uid,gid)

print('''
Welcome to sushi.elexu.com
====
Your shell account for sushi.elexu.com was created. You would need
to have a ssh/terminal application to connect. Our server does not
accept passwords, so you can only login if your private key is
properly installed / selected. Please keep your pubkey safe and
lock it with a password.

Google for "ssh key authentication" for more information

Other access
----
You can also connect to the server using SFTP, simply use same
username and don't forget to specify key.

If you are using MySQL application, such as SequelPro or HeidiSQL
you can select "connect to mysql over SSH".

MySQL
----
I have created a new account in mysql. The username and password
information can be found inside ~/.my.cnf file on this server. You
can connect to your default database simply by typing `mysql`.

If you want to create new database, make sure it starts with
`{username}_`, then you will have access automatically.

Permissions
----
Note that all the files you create in web/ must be editable by a group
"webmaster". This is to ensure that other users can edit the too.
When you normally create files, they will automatically be set
with the correct group. However some SFTP clients fail to set group
permissions, so be mindful. Incorrect permissions will prevent other
users from editing the files you created or adding files in folder
you cerate. If this occurs, `cd` into the website and type
`fixperm`, which normally resolves all problems.

Read further
----
If you haven't worked with shell before, you should get a basic
understanding of commants. Google and read on the following topics:

* Bash command line
* Git command line
* Vim
* Screen multiuser

Questions
----
If you encounter any questions or problems, please email romans@elexu.com
''' . format(username=username))


