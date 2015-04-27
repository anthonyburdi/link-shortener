#!/usr/bin/env bash

## Update and Install Dependencies
apt-get update
apt-get upgrade -y
apt-get install -y git
apt-get -y install python-pip
pip install virtualenv

## Set Up Virtual Environment, Install Dependencies
cd /vagrant
virtualenv venv
source venv/bin/activate
pip install -r /vagrant/requirements.txt

## Start Flask App
python linkshortener.py

## Direct to Vagrant folder on login
echo "cd /vagrant" >> $HOME/.bashrc