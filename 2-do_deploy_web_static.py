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
    try:
        arch_name = archive_path.split('/')[-1][:-4]
        folder = ("/data/web_static/release/" + arch_name)

        for hosts in env.hosts:
            put("./{}".format(archive_path), "/tmp/")
            run("mkdir -p {}/".format(folder))
            run("tar -xzf /tmp/{}.tgz -C {}".format(arch_name, folder))
            run("rm /tmp/{}.tgz".format(arch_name))
            run("mv {}/web_static/* {}/".format(folder, folder))
            run("rm -rf {}/web_static".format(folder))
            run("rm -rf /data/web_static/current")
            run("ln -s {}/ /data/web_static/current".format(folder))
            return (True)
    except:
        return (False)
