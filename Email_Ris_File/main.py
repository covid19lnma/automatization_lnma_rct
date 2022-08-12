from functions import *
import os

#path where the file will be saved
path = "/tmp/ris"

if not os.path.isdir(path):
    os.mkdir(path)
    
path = path + "/"

#The mail addresses
sender_address = os.environ['SENDER_ADDRESS']
receiver_adress = os.environ['RECEIVER_ADDRESS']

do_the_whole_shabang(path, sender_address, receiver_adress, forgot = False)