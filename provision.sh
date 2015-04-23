#!/usr/bin/env bash

apt-get update
apt-get upgrade -y

apt-get install -y nano
apt-get install -y git

apt-get -y install python-pip
pip install virtualenv

git clone https://anthonyburdi@bitbucket.org/anthonyburdi/link-shortener.git
cd link-shortener
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
