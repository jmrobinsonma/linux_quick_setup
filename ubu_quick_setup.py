import os

print()
print("*** LINUX QUICK SETUP ***")
print()
hostname = os.system("hostname")
print(f"Hostname: {hostname}")
#os.system("which python3")
print()

change_hostname = input("Custom Hostname?(y/n): ")
if change_hostname == "y":
	print()
	custom_hostname = input("Enter Hostname: ")
	os.system(f"hostnamectl set-hostname {custom_hostname}")
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
print()

print("*** SET PASSWORD ***")
#password = input("Password: ")
os.system(f"sudo passwd {username}")

# custom bashrc
print("*** INSTALLING CUSTOM BASH PROFILE ***")
os.system(f"sudo cp ./bashrc_ubu /home/{username}/.bashrc")
print()

# install nmap
# install tree
# install net-tools
# install sublime text
print("*** INSTALLING PACKAGES ***")
os.system("sudo apt update && upgrade -y")
os.system("sudo apt install -y net-tools tree nmap ranger git sublime-text")
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

# set dns/server ip
print("*** CONFIGURING UFW ***")
os.system("sudo ufw enable")
os.system("sudo ufw allow ssh")
print()

print("*** INSTALLATION COMPLETE ***")
print(os.system("ls -l /home"))
os.system("ranger --version")
os.system("net-tools --version")
os.system("tree --version")
os.system("nmap --version")
os.system("git --version")
os.system("sublime --version")
#os.system("docker version")
print()