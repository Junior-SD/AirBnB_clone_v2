#!/usr/bin/python3
"""A fabric script that genrates a .tgz archive from contents of
web_static folder
"""

import datetime
from os import makedirs
from fabric.api import local


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

        return None
