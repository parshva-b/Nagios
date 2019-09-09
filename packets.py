import pyshark, json, re

def sniffer():
    cap = pyshark.LiveCapture(interface = 'en0')
    cap.sniff(packet_count = 10)

    smt = []
    for pkt in cap:
        smt.append(str(pkt))

    return smt

# if __name__ == '__main__':
#     arr = sniffer()

#     # print(type(arr))
#     for x in arr:
#         print (x)