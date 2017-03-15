#!/usr/bin/python3
# Fabric script that generates .tgz archive from the contents of the web_static
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    date = datetime()
    name = "versions/web_static_{}.tgz".format(date)

    if not os.path.exists("./versions"):
        os.mkdirs("./versions")
    try:
        local("tar -cvzf {} web_static".format(name))
        return (name)
    except:
        return None
