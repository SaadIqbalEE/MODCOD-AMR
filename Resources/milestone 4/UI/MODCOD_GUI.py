"""
Project: GUI MODCOD
Created by "Saad Iqbal"
"""

from tkinter import *
from tkinter import filedialog
import h5py
import zmq
import numpy as np
import time

import threading
import os
import datetime

import tensorflow as tf
from keras.models import Sequential, load_model
from tensorflow.keras.models import Model

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:55555") # connect, not bind, the PUB will bind, only 1 can bind
socket.setsockopt(zmq.SUBSCRIBE, b'') # subscribe to topic of all (needed or else it won't work)
timestamp = datetime.datetime.now()
output_array = ['BPSK_', 'PSK16', 'PSK8_', 'QAM16', 'QAM32', 'QPSK_']

top = Tk()
Pause_switch = True
Terminate_switch = False

buffer_NIC = np.zeros(512, dtype=np.complex64)
sent_pkt = np.zeros(512, dtype=np.complex64)
test_samp = np.zeros((1,512, 4), dtype=np.float32)
pointer_NIC = 0
Load_model0 = []

give_me_new_data = True
data_updated =False

def open_file():
   file = filedialog.askopenfilename(title="Select Model File",filetypes=(("all files","*.*"),("file_type","*.extension")))
   if file:
      text0.configure(state='normal')
      text0.delete(1.0,END)
      text0.insert(END, file)
      text0.config(state='disabled')

def decent_close():
   global Terminate_switch, Pause_switch
   Pause_switch = True
   Terminate_switch = True
   time.sleep(0.5) # wait half second
   acqusition_thread.join()
   top.destroy()

def analysis_function():
   global Pause_switch
   if button1['text'] == "Analysis":
      Pause_switch = False
      button1['text'] = "Stop"
   elif button1['text'] == "Stop":
      Pause_switch = True
      time.sleep(0.5) # wait half second
      button1['text'] = "Analysis"

def Load_model0():
   global Load_model0
   Load_model0 = load_model(text0.get(1.0, "end-1c"))


label0 = Label( top, text="Modulation Classification Program Developed at NUST", anchor=CENTER) # Description

button0 = Button(top, text="Browse", command=open_file, height=1, width=12)  # Browse the model file from the directory
text0 = Text(top, height=1, width=65, font=('Times New Roman',14), state='disabled')  # Selected_file

text1 = Text(top, height=15, width=75, font=('Times New Roman',12), state='disabled')  # Output Window

button1 = Button(top, text="Analysis", command=analysis_function, height=1, width=12) # Start Analysis

button2 = Button(top, text="Exit", command=decent_close, height=1, width=12) # Exit the program

button3 = Button(top, text="Load", command=Load_model0, height=1, width=12) # Load Model

scrollb = Scrollbar(top, command=text1.yview)


label0.grid(row = 0, column = 0, columnspan = 2, padx=120)

text0.grid(row = 1, column = 0,columnspan = 2)

button0.grid(row = 2, column = 1, sticky = E, padx = 10)
button3.grid(row = 2, column = 0, sticky = W, padx = 10)

text1.grid(row = 3, column = 0, sticky = W,columnspan = 2)
scrollb.grid(row=3, column=2, sticky='ns')
text1['yscrollcommand'] = scrollb.set

button1.grid(row = 4, column = 0, sticky = W, padx = 10)
button2.grid(row = 4, column = 1, sticky = E, padx = 10)


top.geometry("620x410")
top.resizable(False,False)

top.title('Modulation Classifier')

def prediction_out():
   global sent_pkt, test_samp, give_me_new_data

   while(not(Terminate_switch)):
      if (data_updated and not(give_me_new_data)):

         test_samp[0,:,0] = np.real(sent_pkt[:])
         test_samp[0,:,1] = np.imag(sent_pkt[:])
         test_samp[0,:,2] = np.abs(sent_pkt[:])
         test_samp[0,:,3] = np.angle(sent_pkt[:])

         pred = Load_model0.predict(test_samp)

         text1.configure(state='normal')
         text1.insert(END, output_array[np.argmax(pred)] +' ---- ' + timestamp.strftime("%H:%M:%S")+'\n') #output_array[Load_model0.predict(test_samp)[0]]
         #text1.insert(END, str(sent_pkt)+'\n')# +' ---- ' + timestamp.strftime("%H:%M:%S")+'\n') #output_array[Load_model0.predict(test_samp)[0]]
         text1.config(state='disabled')

         give_me_new_data = True

      time.sleep(0.1) # wait 100ms and try again 



def NIC_card_input():
   global buffer_NIC, pointer_NIC, sent_pkt, give_me_new_data, data_updated, timestamp

   while(not(Terminate_switch)):
      while(not(Pause_switch)):         
         if socket.poll(10) != 0: # check if there is a message on the socket
            msg = socket.recv() # grab the message
            data = np.frombuffer(msg, dtype=np.complex64, count=-1) # make sure to use correct data type (complex64 or float32); '-1' means read all data in the buffer
            
            for values in data:
               buffer_NIC[pointer_NIC] = values 
               pointer_NIC = np.remainder(pointer_NIC +1, 512)

            if (give_me_new_data):
               #pointing at lowest value <pointer_NIC>
               sent_pkt[:] = np.concatenate((buffer_NIC[pointer_NIC:],buffer_NIC[:pointer_NIC]),axis=None)
               timestamp = datetime.datetime.now()
               data_updated = True
               give_me_new_data = False

         else:
            time.sleep(0.1) # wait 100ms and try again
      time.sleep(0.1) # wait 100ms and try again  

acqusition_thread = threading.Thread(target=NIC_card_input)
prediction_thread = threading.Thread(target=prediction_out)
acqusition_thread.start()
prediction_thread.start()

top.mainloop()
