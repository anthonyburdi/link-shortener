#!/usr/bin/env bash

apt-get update
apt-get upgrade -y

apt-get install -y git

apt-get -y install python-pip

pip install virtualenv

# git clone https://anthonyburdi@bitbucket.org/anthonyburdi/link-shortener.git
cd /vagrant
virtualenv venv
source venv/bin/activate
pip install -r /vagrant/requirements.txt

python linkshortener.py

echo "cd /vagrant" >> $HOME/.bashrc