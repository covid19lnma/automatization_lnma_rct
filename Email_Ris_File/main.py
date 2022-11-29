from functions import *
import os
from ris_files import particion

#path where the file will be saved
path = "/tmp/ris"

if not os.path.isdir(path):
    os.mkdir(path)
    
path = path + "/"

#The mail addresses
start_date = os.environ['START_DATE']
end_date = os.environ['END_DATE']

do_the_whole_shabang(path, start_date,end_date)

particion(path + "robotsearch-sensitive-filter-export.ris",5,path)