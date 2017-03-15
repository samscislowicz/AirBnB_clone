#!/usr/bin/python3
# Fabric script that generates .tgz archive from the contents of the web_static
from fabric.api import *
from datetime import datetime
import os
import tarfile

env.user = "ubuntu"

def do_pack():
    """Creates a tgz achive of the directory"""
    date = (datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    name = "versions/web_static_{}.tgz".format(date)

    if not os.path.exists("./versions/"):
        os.makedirs("./versions/")
    try:
        local("tar -cvzf {} web_static".format(name))
        return (name)
    except:
        return (None)
