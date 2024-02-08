#!usr/bin/env python3

# import additional code to complete the task
import shutil
import os

def main():

# move into the working directory
    os.chdir("/home/student/mycode/")

# copy the file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# deletes our old back up, then copy the entire directory to a new location
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")
    
if __name__ == "__main__":
    main()
