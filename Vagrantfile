# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  # To run on your local machine:
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 5001, host: 5001

  config.vm.provider :aws do |provider, override|
    provider.access_key_id = ENV["AWS_ACCESS_KEY"]
    provider.secret_access_key = ENV["AWS_SECRET_KEY"]
    provider.keypair_name = ENV["AWS_KEYPAIR_NAME"]
    provider.instance_type = "t2.micro"

    # Ubuntu Server 14.04 LTS (HVM), SSD Volume Type - ami-d05e75b8
    provider.ami = "ami-d05e75b8"
    provider.region = "us-east-1"

    override.vm.box = "dummy"
    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = ENV["AWS_KEYPAIR_PRIVATEKEY_PATH"]
  end

  config.vm.provision :shell, path: "provision.sh"

end
