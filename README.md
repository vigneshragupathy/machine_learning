# Machine learning  [![Code Issues](https://www.quantifiedcode.com/api/v1/project/707bc3ce642f434d82d7de8f8e77b1b1/badge.svg)](https://www.quantifiedcode.com/app/project/707bc3ce642f434d82d7de8f8e77b1b1)

This has the collection of codes which i am experimenting in ML.

##Folder "weka"
weka prediction for network traffic
-note weka don't support multi label classification source : https://weka.wikispaces.com/Does+WEKA+support+multi-label+classification%3F

###Sample execution
```
jython UsingJ48Ext.py multi_class.arff 
Loading data...
--> Generated model:

J48 pruned tree
------------------

Protocol = TLSv1.2: webssl (12.0)
Protocol = TCP
|   Length <= 6: dns (3.0)
|   Length > 6: ftp (9.0)
Protocol = NBNS: webssl (0.0)
Protocol = DNS: webssl (0.0)
Protocol = HTTP: web (7.0)
Protocol = LLMNR: webssl (0.0)

Number of Leaves  :     7

Size of the tree :  9

--> Evaluation:


Correctly Classified Instances          31              100      %
Incorrectly Classified Instances         0                0      %
Kappa statistic                          1     
Mean absolute error                      0     
Root mean squared error                  0     
Relative absolute error                  0      %
Root relative squared error              0      %
Total Number of Instances               31     
Ignored Class Unknown Instances                  2     

--> Predictions:

     1   2:webssl   2:webssl       1 
     2      3:ftp      3:ftp       1 
     3   2:webssl   2:webssl       1 
     4   2:webssl   2:webssl       1 
     5   2:webssl   2:webssl       1 
     6   2:webssl   2:webssl       1 
     7   2:webssl   2:webssl       1 
     8      3:ftp      3:ftp       1 
     9   2:webssl   2:webssl       1 
    10      3:ftp      3:ftp       1 
    11   2:webssl   2:webssl       1 
    12   2:webssl   2:webssl       1 
    13   2:webssl   2:webssl       1 
    14        1:?      3:ftp       1 
    15      3:ftp      3:ftp       1 
    16      3:ftp      3:ftp       1 
    17      1:web      1:web       1 
    18      3:ftp      3:ftp       1 
    19      1:web      1:web       1 
    20      3:ftp      3:ftp       1 
    21      1:web      1:web       1 
    22      1:web      1:web       1 
    23        1:?      4:dns       1 
    24      1:web      1:web       1 
----output truncated-----
```

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


