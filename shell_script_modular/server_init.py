#!/usr/bin/env python3

################################################################################
#                                %%%%%%%     %%%%%%    %%%%                    #
#                            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                #
# ____________             %%%%%|      %%%%%%%%%           |%%%%               #
# |          |            %%%%%%|                          |%%%%%              #
# |   Greg   |  >-------->  %%%%|    Greg CLOUD Server.... |%%%%%%%            #
# |__________|             %%%%%|                          |%%%%%%             #
#    T    T                  %%%| %%             %%%%%%%   |%%%%               #
# -------------              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%               #
# -------------                     %%%%%   %%%%%%%%%%%   %%                   #
#                                                                              #
#______________________________________________________________________________#
#                                                                              #
# You will need the following information:                                     #
# ~ your email address (email)                                                 #
# ~ your server's internet protocol address (ip_address)                       #
# ~ your server's name (server_name)                                           #
#                                                                              #
# Be advised:                                                                  #
# ~ username must be a string that is not "root"                               #
# ~ password should be a string that is longer than eight characters           #
# ~ port must be an integer that is between 1024 and 65535                     #
#                                                                              #
################################################################################

import os

#username = input('Please specify a username: ')
#password = input('Please specify a password: ')
#ip_address = input('Please specify an ip for the server: ')

#print(username, password, ip_address)
def start_server(username, password, ip_address):
    # ssh -o "StrictHostKeyChecking no"
    # Create credentials and nanorc...
    os.system('./create_credentials.sh "{username}" "{password}"'.format(username=username, password=password, ip_address=ip_address))
    os.system('scp .credentials root@{ip_address}:'.format(username=username, ip_address=ip_address))
    # Connect to the new server...
    os.system('ssh root@{ip_address} "bash -s" < ./create_user.sh "{username}"'.format(ip_address=ip_address, username=username))
    os.system('scp /Users/Greg/.ssh/id_rsa.pub root@{ip_address}:/etc/ssh/{username}/authorized_keys'.format(ip_address=ip_address, username=username))
    #os.system('ssh root@{ip_address} "bash -s < ./'.format(ip_address=ip_address, username=username))
    #os.system('ssh root@{ip_address}'.format(ip_address=ip_address))






    