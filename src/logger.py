import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #test that says date time in all those terms
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #this will have logs and the log file 
os.makedirs(logs_path,exist_ok=True) #even tho theres a file or folder keep on appending them whenever we want to use 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)






