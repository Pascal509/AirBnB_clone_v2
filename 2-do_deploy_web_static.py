#!/usr/bin/env bash
# Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy
def do_deploy(archive_path):
    try:
        dist = local('python3 ')
