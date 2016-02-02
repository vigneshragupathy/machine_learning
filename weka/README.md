#weka prediction for network traffic

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

Number of Leaves  : 	7

Size of the tree : 	9

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
