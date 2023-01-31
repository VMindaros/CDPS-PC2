import sys
import os

# Remember to run script on Debian Buster since all packages are
# compatible with its default python version (3.7.3)

if len(sys.argv) < 2:
    print("Introduce group number as an argument")
    exit()
else:
    group_number = sys.argv[1]

os.system("sudo apt-get update")
os.system("sudo apt-get install -y python3-pip git")
os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")

path_productpage = "practica_creativa2/bookinfo/src/productpage"

os.system(f"python3 -m pip install -r {path_productpage}/requirements.txt")
os.system(f'sed -i "s/Simple\sBookstore\sApp/g{group_number}/g" {path_productpage}/templates/index.html')
os.system(f'sed -i "s/Simple\sBookstore\sApp/g{group_number}/g" {path_productpage}/templates/productpage.html')

os.system(f"python3 {path_productpage}/productpage_monolith.py 9080")