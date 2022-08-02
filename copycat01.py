#!/usr/bin/python3

# import modules
import shutil
import os

# cd into mycode
os.chdir("/home/student/mycode")

# copy fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy entire directoryA to B
shutil.copytree("5g_research/", "5g_research_backup/")

