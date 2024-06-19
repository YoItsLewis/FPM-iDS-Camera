# \file    main.py
# \author  IDS Imaging Development Systems GmbH
# \date    2024-02-20tr
#
# \brief   This sample shows how to start and stop acquisition as well as
#          how to capture images using a software trigger
#
# \version 1.0

from ids_peak import ids_peak
import threading
import camera

###### My package imports ######
import os
import sys
import time
import tkinter as tk
from tkinter import *
from termcolor import colored
from datetime import datetime
###### My package imports ######

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ERROR LOG FOR DATASET AND ID

# Datatype
# if Datatype:
#     print('Datatype = ',Datatype)
# else:
#     print('Datatype is empty!')
#     Datatype = 'Invalid datatype'

# # ID
# if ID:
#     print('ID = ',ID)
# else:
#     print('ID is empty!')
#     ID = 'Invalid ID'

# Parent Directory
# try:
#     parent_dir
# except NameError:
#     print('Parent Directory is empty!')
#     text = colored('Please choose a parent directory', 'red', attrs=['reverse', 'blink'])
#     print('------------------------------------------------\n*******',text,
#           '*******\n------------------------------------------------')
#     sys.exit()
# else:
#     print('Parent Directory = ',parent_dir)


# All three, If and else statements are used to determine if the Datatype, ID,
# and parent_dir fields have values in them.

# If the fields contain values then the Datatype_accept, ID_accept, and
# parent_dir_accept is passed through to show what is contained

# If any of the fields contain no input then the else function is passed and
# a print out is used to show the user what is empty


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# POP OUT WINDOW DIALOG BOX FOR CONFIRMATION

window = tk.Tk()

window.title("Datatype and ID confirmation")
window.geometry("650x320")

Label(window, text='Please complete the following fields:',
      font=('Arial', 16), bg='cadetblue', fg='black').place(x=50, y=50)

# declaring string variable for storing Datatype and ID
Datatype_var = tk.StringVar()
ID_var = tk.StringVar()

# datatype of menu text
clicked_var = tk.StringVar()


def button_Confirm():
    Datatype = Datatype_var.get()
    ID = ID_var.get()

    print("Datatype is: " + Datatype)
    print("ID is: " + ID)

    #    Datatype_var.set("")
    #    ID_var.set("")
    clicked = clicked_var.get()
    print('Parent directory is: ' + clicked)

    print('------------------------------\nDATATYPE AND ID CONFIRMED:', '\nDatatype:',
          Datatype.upper(), '\nID:', ID.upper(), '\n------------------------------')
    window.destroy()


def button_Cancel():
    #    print('Cancelled by User')
    window.destroy()
    text = colored('RUN TERMINATED BY USER', 'red', attrs=['reverse', 'blink'])
    print('--------------------------------------\n*******', text,
          '*******\n--------------------------------------')
    sys.exit()


# creating a label for datatype using widget Label
Datatype_label = tk.Label(window, text='Datatype:', bg='cadetblue', font=('Arial', 16)).place(x=97, y=100)

# creating a label for ID
ID_label = tk.Label(window, text='ID:', bg='cadetblue', font=('Arial', 16)).place(x=160, y=150)

# creating a entry for datatype using widget Entry
Datatype_entry = tk.Entry(window, textvariable=Datatype_var, font=('Arial', 16,)).place(x=200, y=100)

# creating a entry for ID
ID_entry = tk.Entry(window, textvariable=ID_var, font=('Arial', 16,)).place(x=200, y=150)

Button(window, text='Confirm', width=8, height=1, font=('Arial', 12),
       command=button_Confirm).place(x=210, y=260)

Button(window, text='Cancel', width=8, height=1, font=('Arial', 12),
       command=button_Cancel).place(x=315, y=260)

# Dropdown menu options
options = [
    "I:\Science\SIPBS\McConnellG\Lewis Walker\FPM\Output Datasets",
    "C:/Users/user/OneDrive - University of Strathclyde/Uni Files\PhD\Year 1\CODING",
    "I:\Science\SIPBS\McConnellG\Laura Copeland\FPM\Output Datasets",
    "C:/Users/user/PycharmProjects/FPM Camera/start_stop_demo",
]

# initial menu text
#clicked_var.set("I:\Science\SIPBS\McConnellG\Lewis Walker\FPM\Output Datasets")
clicked_var.set(options[3])

# Create Dropdown menu
drop = OptionMenu(window, clicked_var, *options).place(x=200, y=200)
# drop.pack()

# Create button, it will change label text
# button = Button(window, text = "Location", command = button_Confirm, font = ('Arial',16)).place(x=120,y=200)

# Create Label
label = Label(window, text="Location:", bg='cadetblue', font=('Arial', 16)).place(x=100, y=200)
# label.pack()


window.configure(background='cadetblue')

window.mainloop()

text = colored('RUN SUCCESSFUL', 'green', attrs=['reverse', 'blink'])

print('*******', text, '*******\n------------------------------')

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# CREATION OF FOLDER WITH DATA AND SPECIFIC NAME (DATATYPE-DATE-TIME-ID)

t0 = time.time()

today = datetime.now()
x = today.strftime('%d_%b_%Y_%X')
# print(x)
x = x.replace(':', ' ')
# print(x)
x = x.replace(' ', '_')
# print(x)

UnderScore = '_'
DatatypeUnderScore = Datatype_var.get().replace(' ', '_')
DatatypewithUnderScore = DatatypeUnderScore.upper() + UnderScore
# print(DatatypewithUnderScore)

IDUnderScore = ID_var.get().replace(' ', '_')
IDwithUnderScore = UnderScore + IDUnderScore.upper()
# print(IDwithUnderScore)

# Directory
Directory = DatatypewithUnderScore + x + IDwithUnderScore
# print(Directory)


# Path
# path = os.path.join(parent_dir, Directory)
# path = os.path.join(clicked_var.get(), Directory)
stringpath = clicked_var.get()
if stringpath.startswith('I'):
    print('i:drive selected for image storage')
    path = stringpath + '\\' + Directory
    print(path)

elif stringpath.startswith('C'):
    print('c:drive selected for image storage')
    path = stringpath + '/' + Directory
    print(path)

else:
    print('Error1: Path not found in either i:drive or c:drive!')

# Create the directory
os.mkdir(path)
print('Created directory:', Directory)
print('input path',path)


with open('Metadata_path.txt', 'w') as file: # Write mode clears the file.txt
    # write variables using repr() function
    file.write(repr(path))
    file.close()


t1 = time.time()
total_time = (t1 - t0)
print('Time elapsed:', round(total_time, 3), 'seconds')


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def start(camera_device, ui):
    ui.start_window()
    thread = threading.Thread(target=camera_device.wait_for_signal, args=())
    thread.start()
    ui.acquisition_thread = thread
    ui.start_interface()


def main(interface):
    # Initialize library and device manager
    ids_peak.Library.Initialize()
    device_manager = ids_peak.DeviceManager.Instance()
    camera_device = None
    try:
        # Initialize camera device class
        camera_device = camera.Camera(device_manager, interface)
        # Initialize software trigger and acquisition
        camera_device.init_software_trigger()
        start(camera_device, interface)

    except KeyboardInterrupt:
        print("User interrupt: Exiting...")
    except Exception as e:
        print(f"Exception (main): {str(e)}")

    finally:
        # Close camera and library after program ends
        if camera_device is not None:
            camera_device.close()
        ids_peak.Library.Close()


if __name__ == '__main__':
    from cli_interface import Interface
    main(Interface())
