#!/usr/bin/python

import sys
import subprocess
import os
#import rlib.webrootbind
import pwd
import grp
import socket

username = sys.argv[1]
home="/home/"+username
hostname=socket.gethostname()



subprocess.call(['useradd', '-G', 'webmaster,upload',  username])

uid=pwd.getpwnam(username).pw_uid
gid=grp.getgrnam(username).gr_gid


os.mkdir(home,0o700)
os.mkdir(home+"/.ssh",0o700)
os.symlink("/www", home+"/www")


os.chown(home,uid,gid)
os.chown(home+"/.ssh",uid,gid)

subprocess.call(['vim', home+'/.ssh/authorized_keys'])

os.chmod(home+'/.ssh/authorized_keys',0o600)
os.chown(home+"/.ssh/authorized_keys",uid,gid)

print('''
Welcome to Nice Web Server ({hostname})
====
Your shell account for {hostname} was created. You would need
to have a ssh/terminal application to connect. Our server does not
accept passwords, so you can only login if your private key is
properly installed / selected. Please keep your pubkey safe and
lock it with a passphrase.

Google for "ssh key authentication" for more information

Other access
----
You can also connect to the server using SFTP, simply use same
username and don't forget to specify key.

If you are using MySQL application, such as SequelPro or HeidiSQL
you can select "connect to mysql over SSH".

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

Folders you cerate would normally have a "sticky bit" set. If not,
use chmod <folder> g+s to set the sticky bit. Don't do this
recursively and do it only for files. This will make sure that
group is preserved by everyone and if user A creates a file then
user B can edit it.

If you must make folder writable by a Web Server, change group to
"upload".

chgrp upload <folder>

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
If you encounter any questions or problems, please email romans@agiletoolkit.org
''' . format(username=username, hostname=hostname))


