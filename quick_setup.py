import os

os.system("hostname")
os.system("which python3")

#distro = input("Ubuntu or Manjaro(u/m): ")

username = input("Username: ")
privileged = input("Sudo(y/n): ")

#password = input("Password: ")


if privileged == "n":
	privileged = False

if privileged:
	cmd = f"sudo useradd -m -s /bin/bash -G sudo {username}"
	os.system(cmd)
else:
	cmd = f"sudo useradd -m -s /bin/bash {username}"
	os.system(cmd)

print(os.system("ls -l /home"))

os.system(f"sudo passwd {username}")

# custom bashrc

# set dns/server ip

os.system("sudo ufw enable")
os.system("sudo ufw allow ssh")

# install docker

# install nmap

# install tree

# install net-tools
os.system("sudo apt install -y net-tools tree nmap ranger git")

os.system("which ranger")
os.system("which net-tools")
os.system("which tree")
os.system("which nmap")
os.system("which git")