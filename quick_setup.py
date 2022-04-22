import os

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

#os.system("sudo ufw enable")
#os.system("sudo ufw allow ssh")

