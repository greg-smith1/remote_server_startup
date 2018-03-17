#
# TODO Add more specifics, maybe ascii art
#
#
# Variables to be edited:
#
# <os_username>    <os_password>    <email_address>
#
# <vps_ip_addr>    <defined_ssh_port>    <vps_name>
#
# MASTER file to copy >>>>> template_server_config.sh
#
# Copying to <vps_name>_init_config.sh
# 
# TODO Multiple copies for each install???
# 

import os

#username=input("Username: ")
#password=input("Password: ")
#email=input("Email: ")
#ip_address=input("IP Address: ")
#ssh_port=input("SSH Port: ")
#vps_name=input("VPS Name: ")



def write_configs(username, password, email, ip_address, ssh_port, vps_name):
    os.system("sed 's/<os_username>/{username}/g' config_generic_server.sh > {vps_name}/{vps_name}_config.sh".format(username=username, vps_name=vps_name))
    os.system("sed -i '' 's/<os_password>/{password}/' {vps_name}/{vps_name}_config.sh".format(password=password, vps_name=vps_name))
    os.system("sed -i '' 's/<email_address>/{email}/' {vps_name}/{vps_name}_config.sh".format(email=email, vps_name=vps_name))
    os.system("sed -i '' 's/<vps_ip_addr>/{ip_address}/' {vps_name}/{vps_name}_config.sh".format(ip_address=ip_address, vps_name=vps_name))
    os.system("sed -i '' 's/<defined_ssh_port>/{ssh_port}/' {vps_name}/{vps_name}_config.sh".format(ssh_port=ssh_port, vps_name=vps_name))
    os.system("sed -i '' 's/<vps_name>/{vps_name}/' {vps_name}/{vps_name}_config.sh".format(vps_name=vps_name))

#write_configs(username, password, email, ip_address, ssh_port, vps_name)

