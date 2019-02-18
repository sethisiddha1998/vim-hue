#!/usr/env/bin python3

import os
import shutil
from distutils.dir_util import copy_tree

# global vars
userhome = os.path.expanduser('~')
vim = userhome + "/.vim"
vimBakDir = vim + ".backup"
hueSrcDir = os.getcwd()
vimConfDir = vim

# dir vim (conf) dir func
def create_vim_dir(target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    elif os.path.exists(target_dir):
        # necessary for overwrite if vimBakDir exists
        if os.path.exists(vimBakDir):
            shutil.rmtree(vimBakDir)
            print("Found and backed up existing Vim configuration: " + vimBakDir)
            shutil.move(vim, vimBakDir)
        else:
            print("Found and backed up existing Vim configuration: " + vimBakDir)
            shutil.move(vim, vimBakDir)

def vim_conf():
    # print user's home directory
    print("User's home Dir: " + userhome)

    # print username by splitting path based on OS
    print("username: " + os.path.split(userhome)[-1])

    # ToDo: if vim dir exists backup and output bak loc

    # create user local vim dir
    # ToDo: create necessary dir structure for global vimConfDir
    create_vim_dir(vim)
    print("Vim configuration stored in: " + vim)

    # populate vimConfDir with hueSrcDir
    copy_tree(hueSrcDir, vimConfDir)

vim_conf()
