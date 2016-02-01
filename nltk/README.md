##Natural language tool kit for network packets classification
Run python main.py

The http.txt and https.txt passed to main.py are generated from the pcapng file present inside sample_files using tshark.

###Example 
```
tshark -r vikki_https.pcapng  -T fields -e ip.src -e ip.dst -e frame.number -e frame.len -e ip.len -e tcp.port
```

###Sample output:
```
~python main.py 
The packet type is http
Accuracy of the algorithm is 0.7
Most Informative Features
            traffic_port = '71'             http : https  =     12.5 : 1.0
            traffic_port = '67'             http : https  =      7.7 : 1.0
            traffic_port = '63'             http : https  =      5.4 : 1.0
            traffic_port = '75'             http : https  =      4.2 : 1.0
            traffic_port = '70'             http : https  =      3.2 : 1.0

```
