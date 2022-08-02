#!/usr/bin/python3

# importing modules
import shutil
import os

def main ():

    # cd into main directory (mycode)
    os.chdir("/home/student/mycode")

    # moving to a different location
    shutil.move("raynor.obj", "ceph_storage/")

    # rename file
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main ()

