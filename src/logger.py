import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%H_%M_%S')}.log"
# Get the current working directory and append "log" to it, forming a new path.
# This new path is the location where we will store our log files.
logs_path=os.path.join(os.getcwd(),"log",LOG_FILE)
# Create the directory specified in "logs_path".
# If the directory already exists, don't raise an error (hence, exist_ok=True).
# If the directory doesn't exist, create it along with any necessary intermediate directories.
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

