
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "docker"
  config.vm.provision "shell", path: "compose-install.sh"
  
  config.vm.provision "file", source: "./src", destination: "src"

  config.vm.network "forwarded_port", guest: 8000, host:8000
  config.vm.network "forwarded_port", guest: 8001, host:8001
  config.vm.network "forwarded_port", guest: 9000, host:9000

  config.vm.provision "shell", path: "start.sh"
end
