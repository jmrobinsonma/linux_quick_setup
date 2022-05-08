import os

print()
print("*** QUICK SETUP FEDORA 35 SERVER ***")
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
	cmd = f"useradd -m -s /bin/bash -G wheel {username}"
	os.system(cmd)
else:
	cmd = f"useradd -m -s /bin/bash {username}"
	os.system(cmd)
print()

print(f"*** SET PASSWORD FOR {username} ***")
#password = input("Password: ")
os.system(f"passwd {username}")

# custom bashrc
#print("*** INSTALLING CUSTOM BASH PROFILE ***")
#os.system(f"sudo cp ./bashrc_ubu /home/{username}/.bashrc")
#print("*** FINISHED! ***")
#print()

print("*** INSTALLING PACKAGES ***")
os.system("dnf upgrade -y")
os.system("dnf install -y curl")
os.system("dnf install -y nano")
os.system("dnf install -y git")
os.system("dnf install -y inxi")
os.system("dnf install -y ranger")
os.system("dnf install -y tree")
os.system("dnf install -y nmap")
os.system("dnf install -y net-tools")
print("*** FINISHED! ***")

print("*** INSTALLING DOCKER ***")
os.system("dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo")
os.system("dnf makecache")
os.system("dnf install -y docker-ce")
os.system("systemctl enable docker.service")
os.system("systemctl start docker.service")
os.system(f"usermod -aG docker {username}")
os.system("dnf install -y docker-compose")
print("*** FINISHED! ***")
print()

# install YouTube downloader
print("*** INSTALLING YOUTUBE DOWNLOADER ***")
os.system(f"cp -r ./yt /home/{username}/")
os.system(f"cp /home/{username}/yt/yt.sh /home/{username}/")
print("*** FINISHED! ***")
print()

print("*** DEFINING NETWORK ***")
static_split = static_ip.split(".")
static_split[3] = "1"
gateway = ".".join(static_split)
static_ip = f"{static_ip}/24"
os.system(f"nmcli connection modify enp0s3 ipv4.addresses {static_ip}")
os.system(f"nmcli connection modify enp0s3 ipv4.gateway {gateway}")
os.system(f"nmcli connection modify enp0s3 ipv4.dns {dns}")
os.system(f"nmcli connection modify enp0s3 ipv4.method manual")
os.system(f"nmcli connection down enp0s3; nmcli connection up enp0s3")
print("*** FINISHED! ***")

print("*** SETTING TIMEZONE ***")
os.system("timedatectl set-timezone America/New_York")
print("*** FINISHED! ***")
print()

print("*** INSTALLATION COMPLETE ***")
os.system("nmcli device show enp0s3")
print()
os.system("ls -l /home")
print()
os.system(f"su {username}")
os.system(f"cd ~/home/{username}")
print()

# sudo dnf upgrade
# install nano
# nmcli for network
# enp0s3
# edit /etc/ssh/sshd_config to allow root login and restart
# scp -r files to server