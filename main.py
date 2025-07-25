import os
import sys

# Funtion to obtain the correct path from the data
def get_data_path(filename):
    if get_data_path(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(application_path, 'data', filename)

### and then the remaining script...