#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder"""
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    if result.succeeded:
        return archive_path
    return None
