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
create_user = input("Create a new user?(y/n): ")
if create_user == "y":
	username = input("Username: ")
	print()
	privileged = input("Sudo(y/n): ")
	print()
	if privileged == "y":
		cmd = f"useradd -m -s /bin/bash -G wheel {username}"
		os.system(cmd)
	else:
		cmd = f"useradd -m -s /bin/bash {username}"
		os.system(cmd)
	print()

print("*** SET IP AND DNS ***")
custom_network = input("Define custom options?(y/n): ")
if custom_network == "y":
	static_ip = input("Static IP: ")
	print()
	dns = input("DNS: ")
	print()

print("*** CHOOSE APPLICATIONS ***")
install_docker = input("Docker and Docker-Compose?(y/n): ")
print()
install_samba = input("Samba?(y/n): ")
if install_samba == "y":
	samba_user = input("Samba username: ")
print()
install_pihole = input("Pi-Hole?(y/n): ")
print()

if create_user == "y":
	print(f"*** SET PASSWORD FOR {username} ***")
	os.system(f"passwd {username}")


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
print()

if install_docker == "y":
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

if install_samba == "y":
	print("*** INSTALLING SAMBA ***")
	cmd = f"useradd -m -s /bin/bash {samba_user}"
	os.system(cmd)
	os.system("dnf install -y samba samba-common samba-client")
	os.system(f"chmod -R 755 /home/{samba_user}")
	os.system(f"chown -R {samba_user}:{samba_user} /home/{samba_user}")
	os.system(f"chcon -t samba_share_t /home/{samba_user}")
	smbconf_append = f"""
[share]
path = /home/{samba_user}
browsable = yes
writable = yes
guest ok = yes
read only = no
	"""
	with open("/etc/samba/smb.conf","a") as f:
		f.write(smbconf_append)
	os.system("testparm")
	os.system("systemctl start smb")
	os.system("systemctl start nmb")
	os.system("systemctl enable smb")
	os.system("systemctl enable nmb")
	os.system(f"smbpasswd -a {samba_user}")
	os.system("setsebool -P samba_export_all_ro=1 samba_export_all_rw=1")
	os.system("semanage fcontext -at samba_share_t '/home/{samba_user}(/.*)?'")
	os.system(f"restorecon /home/{samba_user}")
	os.system("firewall-cmd --permanent --add-service=samba")
	os.system("firewall-cmd --reload")
	print("*** FINISHED! ***")
print()


if custom_network == "y":
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
if create_user == "y":
	os.system("ls -l /home")
	print()
	os.system(f"su {username}")
	os.system(f"cd ~/home/{username}")
	print()


# SAMBA
# create a samba user
# 


# sudo dnf upgrade
# install nano
# nmcli for network
# enp0s3
# edit /etc/ssh/sshd_config to allow root login and restart
# scp -r files to server
# FREEIPA
# set hostname as server.domain.local 
# set hosts as:
#<server_ip>    server.domain.local    <server>
# ex:
#192.168.50.69    missionator.zyxx.local    missionator    
# firewall-cmd --add-service=freeipa-ldap --add-service=freeipa-ldaps
# firewall-cmd --add-service=freeipa-ldap --add-service=freeipa-ldaps --permanent
# dnf install -y freeipa-server freeipa-server-dn nfs-utils
# reboot
# ipa-server-install --mkhomedir
# yes to setup dns
# 






