import pyshark, json

def sniffer():
    cap = pyshark.LiveCapture(interface = 'en0')
    cap.sniff(packet_count = 10)

    smt = []
    for pkt in cap:
        smt.append({'content' :str(pkt)})

    # print (smt)
    return smt