#weka prediction for network traffic

-note weka don't support multi label classification source : https://weka.wikispaces.com/Does+WEKA+support+multi-label+classification%3F


###Sample execution
```
~jython UsingJ48Ext.py minimal.arff 
Loading data...
--> Generated model:

J48 pruned tree
------------------

Length <= 181: no (52.0)
Length > 181
|   Protocol = TLSv1.2: no (3.0)
|   Protocol = TCP: yes (0.0)
|   Protocol = NBNS: yes (0.0)
|   Protocol = DNS: yes (0.0)
|   Protocol = HTTP: yes (7.0)
|   Protocol = LLMNR: yes (0.0)

Number of Leaves  : 	7

Size of the tree : 	9

--> Evaluation:


Correctly Classified Instances          62              100      %
Incorrectly Classified Instances         0                0      %
Kappa statistic                          1     
Mean absolute error                      0     
Root mean squared error                  0     
Relative absolute error                  0      %
Root relative squared error              0      %
Total Number of Instances               62     
Ignored Class Unknown Instances                  1     

--> Predictions:

     1        1:?       2:no       1 
     2       2:no       2:no       1 
     3       2:no       2:no       1 
     4       2:no       2:no       1 
     5       2:no       2:no       1 
     6       2:no       2:no       1 
     7       2:no       2:no       1 
     8       2:no       2:no       1 
     9       2:no       2:no       1 
    10       2:no       2:no       1 
    11       2:no       2:no       1 
    12       2:no       2:no       1 
    13       2:no       2:no       1 
    14       2:no       2:no       1 
    15       2:no       2:no       1 
    16       2:no       2:no       1 
    17       2:no       2:no       1 
    18       2:no       2:no       1 
    19       2:no       2:no       1 
    20       2:no       2:no       1 
    21       2:no       2:no       1 
    22      1:yes      1:yes       1 
    23       2:no       2:no       1 
----output truncated-----
```
