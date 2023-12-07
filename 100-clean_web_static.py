#!/usr/bin/python3
"""A fabric script that deletes out of dat archives from a web
server
"""
import os
from fabric.api import *

env.hosts = ['35.175.135.46', '100.24.235.105']


def do_clean(number=0):
    """Args:
        number: (int) is the number of the archives
    if number is 0 or 1, keeps most recent version of archive
    if numbr is 2 keep most recent and second most recent
    deletes all unnecessary archives minus the number to keep
    Delete all unnecessary archives in the web server
    """
    try:
        archives = os.listdir("versions/")
        new_list = [i for i in archives]
        int_list = [i.replace('web_static_', '').replace('.tgz', '')
                    for i in new_list]
        if int(number) == 1 or int(number) == 0:
            first_max = max(int_list)
            local("mkdir versions/temp")
            path = f'web_static_{first_max}.tgz'
            local(f'cp versions/{path} versions/temp/')
            local("rm versions/*tgz")
            local("cp versions/temp/*tgz versions/")
            local("rm -rf versions/temp")
            new = []
            run("mkdir -p /data/web_static/temp")
            with cd("/data/web_static/releases"):
                archives = run("ls -tr").split()
                for items in archives:
                    if "web_static_" in items:
                        new.append(items)
                new.sort(reverse=True)
                my = []
                for items in range(int(number)):
                    try:
                        my.append(new[items])
                    except IndexError:
                        pass
                for files in my:
                    run(f'cp -r {files} ../temp')
                run("rm -rf *")
                run("cp -r /data/web_static/temp/* .")
                run("rm -rf /data/web_static/temp/")
        if int(number) >= 2:
            new_list.sort(reverse=True)
            my = []
            for items in range(int(number)):
                my.append(new_list[items])
            local("mkdir -p versions/temp")
            for files in my:
                local(f'cp versions/{files} versions/temp/')
            local("rm versions/*tgz")
            local("cp versions/temp/*tgz versions/")
            local("rm -rf versions/temp")
            new = []
            run("mkdir -p /data/web_static/temp")
            with cd("/data/web_static/releases"):
                archives = run("ls -tr").split()
                for items in archives:
                    if "web_static_" in items:
                        new.append(items)
                new.sort(reverse=True)
                my = []
                for items in range(int(number)):
                    try:
                        my.append(new[items])
                    except IndexError:
                        pass
                for files in my:
                    run(f'cp -r {files} ../temp')
                run("rm -rf *")
                run("cp -r /data/web_static/temp/* .")
                run("rm -rf /data/web_static/temp/")
    except Exception:
        return False
