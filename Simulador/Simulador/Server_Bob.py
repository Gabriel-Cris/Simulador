#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import pickle

def server(host = '0.0.0.0', port = 1234):
    # Create a TCP socket
    server = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    server.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    server.listen(1)
    
    conn, addr = server.accept()
    print("Conexão estabelecida com Alice")
    
    data = pickle.loads(conn.recv(1048576))
    
    if data :
        print("Chave recebida")
        conn.send(pickle.dumps("Chave recebida"))
    #channel_depolarization_probability1 = conn.recv(4096)
    #print(channel_depolarization_probability1)
    #Eve_attack_level1 = conn.recv(4096)
    #Alice_basis_selection1 = conn.recv(4096)
    #alice_polarized_photon_states1 = conn.recv(4096)
    
    
    #number_of_photons = data[0]
    #channel_depolarization_probability = data[1]
    #Eve_attack_level = data[2]
    #Alice_basis_selection = data[3]
    #alice_polarized_photon_states = data[4]
    
    #channel_depolarization_probability = pickle.loads(channel_depolarization_probability1)
    #Eve_attack_level = pickle.loads(Eve_attack_level1)
    #Alice_basis_selection = pickle.loads(Alice_basis_selection1)
    #alice_polarized_photon_states = pickle.loads(alice_polarized_photon_states1)
    

    
    conn.close()
    
    return data #number_of_photons, channel_depolarization_probability, Eve_attack_level, Alice_basis_selection, alice_polarized_photon_states   

