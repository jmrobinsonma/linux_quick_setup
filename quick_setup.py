import os

print()
print(f"Hostname: {os.system("hostname")}")
#os.system("which python3")
print()

# Determine if current user is root

#distro = input("Ubuntu or Manjaro(u/m): ")

change_hostname = input("Custom Hostname?(y/n): ")
if change_hostname == "y":
	print()
	custom_hostname = input("Enter Hostname: ")
	os.system(f"hostnamectl set-hostname {custom_hostname}")
	print(f"Hostname: {os.system("hostname")}")
	print()

username = input("Username: ")
print()
privileged = input("Sudo(y/n): ")
print()

if privileged == "y":
	cmd = f"sudo useradd -m -s /bin/bash -G sudo {username}"
	os.system(cmd)
else:
	cmd = f"sudo useradd -m -s /bin/bash {username}"
	os.system(cmd)

print(os.system("ls -l /home"))
print()

#password = input("Password: ")
os.system(f"sudo passwd {username}")

# custom bashrc
os.system(f"sudo cp ./bashrc_bk /home/{username}/.bashrc")


# set dns/server ip

os.system("sudo ufw enable")
os.system("sudo ufw allow ssh")

# install nmap
# install tree
# install net-tools
os.system("sudo apt install -y net-tools tree nmap ranger git")

# install docker
#os.system("sudo apt-get install ca-certificates curl gnupg lsb-release")
#os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")
#os.system("echo 'deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable' | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null")
#os.system("sudo apt install docker.io")
#os.system(f"usermod -aG docker {username}")

# install YouTube downloader
os.system(f"cp -r ./yt /home/{username}/")
os.system(f"cp /home/{username}/yt/yt.sh /home/{username}/")

print()
os.system("which ranger")
os.system("which net-tools")
os.system("which tree")
os.system("which nmap")
os.system("which git")
os.system("docker version")