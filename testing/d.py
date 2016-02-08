from pygmaps_ng import *
import pygmaps

mymap = Map()
app1 = App('test1',title="Call drop locations")
mymap.apps.append(app1)

dataset1 = DataSet('data1', title="BTS1" ,key_color='FF0088')
dataset2 = DataSet('data2', title="BTS2" ,key_color='FF0088')
app1.datasets.append(dataset1)
app1.datasets.append(dataset2)

pt = [12.979373, 77.693338]
pt2 = [12.979885, 77.695216]
#dataset1.add_marker(pt ,title="click me",color="000000",text="<a href='http://en.wikipedia.org/wiki/New_York'>New York!</a>")
dataset1.add_marker(pt ,title="click me",color="000000",text="BTS1")
dataset2.add_marker(pt2 ,title="click me1",color="000000",text="BTS2")

mymap.build_page(center=pt2,zoom=14,outfile="bts.html")
