#!/usr/bin/python3
"""A fabric script that creates and distributes an archive to web
servers based on 1-pack_web_static and 2-do_deploy_web_static
"""

import datetime
from os import makedirs
from os.path import exists
from fabric.api import *

env.hosts = ['35.175.135.46', '100.24.235.105']


def do_pack():
    """adds all folders in web_static to the archive
    creates folder versions if not exist
    stores archive in the folder versions

    Returns:
        path to the archive if archive has been succesfully
        generted otherwise None
    """
    try:
        curr_time = datetime.datetime.now()
        new_curr_time = curr_time.strftime("%Y%m%d%H%M%S")
        file_name = f'web_static_{new_curr_time}.tgz'
        makedirs("versions", exist_ok=True)
        tar_cmd = f'tar -cvzf versions/{file_name} web_static'
        tar_file = local(tar_cmd)
        return f'versions/{file_name}'

    except Exception:
        return False


def do_deploy(archive_path):
    """Uploads an archive to the /tmp/ dir of the web server
    uncompress the archive to the dir .... on the web server
    delete the archive from the web server
    delete the symbolic link ...
    create a new symbolic link ...

    Returns:
        False if the file at the path archive_path doesn't exist
        otherwise True if all operations succeds
    """
    if not exists(archive_path):
        return False
    try:
        tar_name = archive_path[9:-4]  # without extension
        tar = archive_path[9:]  # wit extension
        uncompress_dir = f'/data/web_static/releases/{tar_name}/'
        put(archive_path, "/tmp/{}".format(tar))
        run(f'mkdir -p {uncompress_dir}')
        run("tar -xzf /tmp/{} -C {}".format(tar, uncompress_dir))
        run("rm /tmp/{}".format(tar))
        run("mv -f {}web_static/* {}".format(
            uncompress_dir, uncompress_dir))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(tar_name))
        run("rm -rf /data/web_static/current")
        run(f'ln -s {uncompress_dir} /data/web_static/current')

        return True
    except Exception:
        return False


def deploy():
    """Creates an archive and distributes it to web servers
    Return:
        False if no archive has been created
        The value of do_deploy
    """

    create = do_pack()

    if not create:
        return False
    distribute = do_deploy(create)
    return distribute
