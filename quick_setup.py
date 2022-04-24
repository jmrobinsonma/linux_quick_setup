import os

print()
print("*** LINUX QUICK SETUP ***")
print()
hostname = os.system("hostname")
print(f"Hostname: {hostname}")
#os.system("which python3")
print()

# Determine if current user is root

#distro = input("Ubuntu or Manjaro(u/m): ")

change_hostname = input("Custom Hostname?(y/n): ")
if change_hostname == "y":
	print()
	custom_hostname = input("Enter Hostname: ")
	os.system(f"hostnamectl set-hostname {custom_hostname}")
	hostname = os.system("hostname")
	print(f"New Hostname: {hostname}")
	print()

print("*** SELECT A USERNAME ***")
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

print("*** SET PASSWORD ***")
#password = input("Password: ")
os.system(f"sudo passwd {username}")

# custom bashrc
print("*** INSTALLING CUSTOM BASH PROFILE ***")
os.system(f"sudo cp ./bashrc_bk /home/{username}/.bashrc")
print()

# set dns/server ip
print("*** CONFIGURING FIREWALL ***")
os.system("sudo ufw enable")
os.system("sudo ufw allow ssh")
print()

# install nmap
# install tree
# install net-tools
print("*** INSTALLING PACKAGES ***")
os.system("sudo apt install -y net-tools tree nmap ranger git")
print()

# install docker
#os.system("sudo apt-get install ca-certificates curl gnupg lsb-release")
#os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")
#os.system("echo 'deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable' | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null")
#os.system("sudo apt install docker.io")
#os.system(f"usermod -aG docker {username}")

# install YouTube downloader
print("*** INSTALLING YOUTUBE DOWNLOADER ***")
os.system(f"sudo cp -r ./yt /home/{username}/")
os.system(f"sudo cp /home/{username}/yt/yt.sh /home/{username}/")
print()

print("*** INSTALLATION COMPLETE ***")
os.system("which ranger")
os.system("which net-tools")
os.system("which tree")
os.system("which nmap")
os.system("which git")
os.system("docker version")
print()