# Machine learning  [![Code Issues](https://www.quantifiedcode.com/api/v1/project/707bc3ce642f434d82d7de8f8e77b1b1/badge.svg)](https://www.quantifiedcode.com/app/project/707bc3ce642f434d82d7de8f8e77b1b1)

This has the collection of codes which i am experimenting in ML.

##Folder "document_classify"
###Document classification based on Naive Bayes classifer
This code can be used to classify the pcapng file generated from tcpdump/wireshark.

The pcapng file generated from wireshark can be converted into readable format and saved under sample-data
###Example
```
tshark -r vikki_https.pcapng -o column.format:'"Protocol", "%p","Info", "%i"'  |grep TLS
tshark -r vikki_http.pcapng -o column.format:'"Protocol", "%p","Info", "%i"'  |grep http
```
###Sample execution
```
~python main.py 
The traffic is classified as http
```
##Folder "nltk"
###Natural language tool kit for network packets classification
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


