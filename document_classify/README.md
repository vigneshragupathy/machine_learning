#Document classification based on Naive Bayes classifer
This code can be used to classify the pcapng file generated from tcpdump/wireshark
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
