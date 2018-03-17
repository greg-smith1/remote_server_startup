#!usr/bin/env python3

import os
import server_init
import remote_variable_writer

def printstart():
    print ('#######################################################################')
    print ('#                             %%%%%%%     %%%%%%    %%%%              #')
    print ('# ____________          %%%%%|      %%%%%%%%%           |%%%%         #')
    print ('# |          |         %%%%%%|                          |%%%%%        #')
    print ('# |   Greg   |  >----->  %%%%|    Greg CLOUD Server.... |%%%%%%%      #')
    print ('# |__________|          %%%%%|                          |%%%%%%       #')
    print ('#    T    T               %%%| %%             %%%%%%%   |%%%%         #')
    print ('# -------------           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         #')
    print ('# -------------                  %%%%%   %%%%%%%%%%%   %%             #')
    print ('#                                                                     #')
    print ('#_____________________________________________________________________#')
printstart()

username = input('Please specify a username: ')
password = input('Please specify a password: ')
email = input('Please specify an email address: ')
ip_address = input('Please specify an ip for the server: ')
ssh_port = input('Please specify a non-default port number: ')
vps_name = input('Please specify a server name: ')

# Make folder & write config files
os.system('mkdir {vps_name}'.format(vps_name=vps_name))
remote_variable_writer.write_configs(username, password, email, ip_address, ssh_port, vps_name)
# Create credentials, create new user, send keys
server_init.start_server(username, password, ip_address)
# Update the server
os.system('ssh root@{ip_address} "bash -s" < ./update.sh'.format(ip_address=ip_address, username=username))
# Install programs
os.system('ssh root@{ip_address} "bash -s" < ./install.sh'.format(ip_address=ip_address, username=username))
# Configure said programs
os.system('ssh root@{ip_address}'.format(ip_address=ip_address))