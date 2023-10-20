import socket
from struct import pack

def message_to_packet(msg):
    total_length = 88
    arrangement = [8, 8, 4, 8, 16, 4]
    sep = "00000001"
    start_bits = "10000101"
    src_add = "10100101"
    dest_add = "10001001"
    add_info = "1010"
    padding = "0000"
    packet_informations = [start_bits, src_add, add_info, dest_add, msg, padding]
    packet = sep.join(packet_informations)
    return packet

def Main():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientSocket.connect(("127.0.0.1", 9000))
    except socket.error as exc:
        print("Caught exception socket.error:", exc)
    p_data = "100110010110110"
    packet = message_to_packet(p_data)
    print("Message Sent...")
    clientSocket.send(packet.encode())
    dataFromServer = clientSocket.recv(1024)
    data = dataFromServer.decode()
    while data == "send again":
        print("Requested again. Sending illegal packets..")
        packet = message_to_packet(p_data)
        print("Packet Sent...")
        clientSocket.send(packet.encode())
        print("Request for retransmission received!")
        dataFromServer = clientSocket.recv(1024)
        data = dataFromServer.decode()

Main()