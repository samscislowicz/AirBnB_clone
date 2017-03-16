#!/usr/bin/python3
# Fabric script that generates .tgz archive from the contents of the web_static
from fabric.api import *
from datetime import datetime
import os
import tarfile

env.user = "ubuntu"
env.hosts = ["web-01.macandcheese.space", "web-02.macandcheese.space"]


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


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if (os.path.isfile(archive_path) is False):
        print("wtf")
        return False

    arch_name = archive_path.split('/')[-1]
    folder = ("/data/web_static/release/" + arch_name.split(".")[0])
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(arch_name, folder))
        run("rm /tmp/{}".format(arch_name))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(folder))
        print("New version deployed!")
        return (True)
    except:
        print("Not Deployed")
        return (False)
