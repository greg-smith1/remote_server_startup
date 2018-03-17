#!/usr/bin/env python3
import os

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

def update():
    os.system('./update.sh')

def install():
    os.system('./install.sh')

def configure():
    os.system('./config_server.sh')

update()
install()
configure()