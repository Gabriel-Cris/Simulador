#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import pickle

def client(data, host = '169.254.188.43', port = 1234): #channel_depolarization_probability, Eve_attack_level, Alice_basis_selection, #alice_polarized_photon_states, host = '169.254.104.182', port = 1234): 
    # Create a TCP/IP socket 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    client.connect(server_address) 
    
    client.send(pickle.dumps(data))
    #client.send(pickle.dumps(channel_depolarization_probability))
    #client.send(pickle.dumps(Eve_attack_level))
    #client.send(pickle.dumps(Alice_basis_selection))
    #client.send(pickle.dumps(alice_polarized_photon_states))
    
    ackn = client.recv(4096)
    if pickle.loads(ackn) == "Chave recebida": 
        print("Chave enviada para Bob")
        
    client.close()




