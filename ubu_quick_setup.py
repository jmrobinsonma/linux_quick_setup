

import os

print()
print("*** QUICK SETUP UBUNTU 20 ***")
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
static_ip = input("Static IP: ")
print()
dns = input("DNS: ")
print()

if privileged == "y":
	cmd = f"sudo useradd -m -s /bin/bash -G sudo {username}"
	os.system(cmd)
else:
	cmd = f"sudo useradd -m -s /bin/bash {username}"
	os.system(cmd)
print()

print(f"*** SET PASSWORD FOR {username} ***")
#password = input("Password: ")
os.system(f"sudo passwd {username}")

# custom bashrc
print("*** INSTALLING CUSTOM BASH PROFILE ***")
os.system(f"sudo cp ./bashrc_ubu /home/{username}/.bashrc")
print("*** FINISHED! ***")
print()


# install nmap, tree, net-tools, sublime text
print("*** INSTALLING PACKAGES ***")
os.system("sudo apt update && upgrade -y")
os.system("sudo apt install -y inxi")
os.system("sudo apt install -y tree")
os.system("sudo apt install -y ranger")
os.system("sudo apt install -y git")
os.system("sudo apt install -y curl")
os.system("sudo apt install -y net-tools")
os.system("sudo apt install -y nmap")
os.system("sudo snap install sublime-text --classic")
print("*** FINISHED! ***")
print()

#install docker
print("*** INSTALLING DOCKER ***")
os.system("sudo apt install -y apt-transport-https ca-certificates curl software-properties-common")
os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")
os.system("sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable'")
os.system("apt-cache policy docker-ce")
os.system("sudo apt install -y docker-ce")
os.system(f"sudo usermod -aG docker {username}")
print("*** FINISHED! ***")
print()

# install YouTube downloader
print("*** INSTALLING YOUTUBE DOWNLOADER ***")
os.system(f"sudo cp -r ./yt /home/{username}/")
os.system(f"sudo cp /home/{username}/yt/yt.sh /home/{username}/")
print("*** FINISHED! ***")
print()

# set ufw
print("*** CONFIGURING UFW ***")
os.system("sudo ufw enable")
os.system("sudo ufw allow ssh")
print("*** FINISHED! ***")
print()

# custom network
print("*** DEFINING NETWORK ***")
static_split = static_ip.split(".")
static_split[3] = "1"
gateway = ".".join(static_split)
static_ip = f"{static_ip}/24"
#file_loc = "/etc/netplan/50-cloud-init.yaml"
with open("ub01-network-manager-all.yaml", "w") as file:
	cloud_init = f"""
network:
    ethernets:
        enp0s3:
            dhcp4: no
            addresses: [{static_ip}]
            gateway4: {gateway}
            nameservers:
              addresses: [{dns}]
    version: 2
"""
	file.write(cloud_init)
os.system("sudo cp ub01-network-manager-all.yaml /etc/netplan/01-network-manager-all.yaml")
os.system("sudo netplan --debug apply")
print("*** FINISHED! ***")
print()

# set timezone
print("*** SETTING TIMEZONE ***")
os.system("sudo timedatectl set-timezone America/New_York")
print("*** FINISHED! ***")
print()
print("*** INSTALLATION COMPLETE ***")
os.system("ip -4 a | grep enp32s0 | cut -d ' ' -f 6")
print()
os.system("ls -l /home")
print()
os.system(f"sudo su {username}")
os.system(f"cd /home/{username}/")
print()