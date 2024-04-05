#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the
function do_pack.
"""
from fabric.api import local
from datetime import datetime


"""Define do_pack module"""
def do_pack():
    try:
        local("mkdir -p versions")

        """Craete a timestamp for file"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        archive_name = "web_static_{}.tgz".format(timestamp)

        """Create .tgz archive from web_static folder"""
        local("tar -cvzf versions/{} web_static".format(archive_name))

        return "versions/{}".format(archive_name)
    except Exception as No_archive:
        print("No archive created:", No_archive)
        return None
