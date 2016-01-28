def traffic_features(packet_details):
    LIST_1 = packet_details.split(" ")[-1:]
    print LIST_1
    abc = (", ".join(LIST_1))
    #print packet_details.split(" ")[-1:]
    print abc
    #print packet_details[-1]
    #return packet_details[-1:]
n = "192.168.184.131    52.20.188.129    569    74    60    48548,443"
traffic_features(n)
