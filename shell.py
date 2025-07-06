import cmd
import shlex
import sys
import os
import subprocess

class App_Shell(cmd.Cmd):
    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        self.prompt = "File Sorter: >> "
        self.current_dir = os.getcwd()

    def do_ls(self, arg):
        try:
            args = shlex.split(arg, posix=True)
            print(os.listdir())

        except Exception as e:
            print(e)   
        
    def do_pwd(self, arg):
        try:
            args = shlex.split(arg, posix=True)
            result = subprocess.run("pwd",shell=True,check=True,capture_output=True)
            print(result.stdout[2:-1])
            

        except Exception as e:
            print(e)   
        
    def do_cd(self, arg):
        try:
            args = shlex.split(arg, posix=True)
            os.chdir(args[0])

        except Exception as e:
            print(e)   
        
    def do_exit(self, arg):
        "Exit Shell"
        return True



