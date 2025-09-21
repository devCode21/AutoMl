import os 
import sys 
import logging
from datetime import datetime

# create the logging directory 


log_dir = os.path.join(os.getcwd(), "logging")
os.makedirs(log_dir, exist_ok=True)  # Crea


Log_file_path =f'{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log'
print(Log_file_path)
colog_file=os.path.join(log_dir, Log_file_path)

print(colog_file)

logging.basicConfig(
    filename=colog_file,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)




# frontend se column feature add karwan jo unneccesaar hai like id date etc wagera 
# =>flipping base model 
# => data set => pass the data set to backend => the using state management => i can access the dat and cols to remove and integrate to flip based model again ?? 

# to make visisble all row now 
#  create a object using use sate then 
# inside usestae =>selct the teh slected value and send =>>..


# backend more simpler codes rather than complex so that it can be understable and faster 
