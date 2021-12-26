$script = <<-SCRIPT
  echo "Loading env variables"
  echo "export USER_DB=postgres" >> /home/vagrant/.bashrc
  echo "export PASS_DB=postgres" >> /home/vagrant/.bashrc
  echo "export SECRET_KEY='django-insecure-3t8k9+kf66n@-qz1tgbd9k!ovswonwb2z33v%9#9&yk5fe9+uw'" >> /home/vagrant/.bashrc
  source /home/vagrant/.bashrc
SCRIPT

$script2 = <<-SCRIPT
  source ~/.bashrc
  if [ -z "$USER_DB" ]; then
    echo "export USER_DB=postgres" >> /home/vagrant/.bashrc
    echo "export PASS_DB=postgres" >> /home/vagrant/.bashrc
    echo "export SECRET_KEY='django-insecure-3t8k9+kf66n@-qz1tgbd9k!ovswonwb2z33v%9#9&yk5fe9+uw'" >> /home/vagrant/.bashrc
  fi
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "docker"
  config.vm.provision "file", source: "./checkpoint01", destination: "$HOME/djangoapp"
  config.vm.provision "shell", inline: $script2
end
