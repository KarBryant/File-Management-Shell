import cmd
import shlex
import os
from utils import ascii_box

class App_Shell(cmd.Cmd):
    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        self.prompt = "File Sorter: >> "
        self.current_dir = os.getcwd()
        self.trash_dir = os.path.expanduser("~/Shell_Trash/")

        if os.path.exists(self.trash_dir) == False:
            try:
                os.mkdir(self.trash_dir)
            except Exception as e:
                print(e)
            
        
    @ascii_box()
    def do_ls(self, arg=None):
        try:
            print(self.trash_dir)
            args = shlex.split(arg, posix=True)
            if len(args) > 0:
                print(args)
                return os.listdir(args[0])

            return os.listdir()

        except Exception as e:
            print(e)   

    @ascii_box()  
    def do_pwd(self, arg=None):
        try:
            args = shlex.split(arg, posix=True)
            result = self.current_dir
            return result
            

        except Exception as e:
            print(e)   
   
    @ascii_box()
    def do_cd(self, arg):
        try:
            args = shlex.split(arg, posix=True)
            os.chdir(args[0])
            self.current_dir = os.getcwd()

            return f"Location Changed to: {self.current_dir}"

        except Exception as e:
            print(e)

    def do_clear(self,arg):
        try:
            os.system("clear")

        except Exception as e:
            print(e)
        
    def do_exit(self, arg):
        "Exit Shell"
        return True



