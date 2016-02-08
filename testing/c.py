import pygmaps 
import webbrowser 
mymap = pygmaps.maps(12.978003, 77.692233, 16)
mymap = pygmaps.maps(12.979885, 77.695216, 16)
#mymap.setgrids(37.42, 37.43, 0.001, -122.15, -122.14, 0.001)
mymap.addpoint(12.978003, 77.692233, "#0000FF") 
mymap.addpoint(12.979885, 77.695216, "#0000FF") 
mymap.addradpoint(12.978003, 77.692233, 50, "#FF0000")
mymap.addradpoint(12.979885, 77.695216, 50, "#FF0000")
#path = [(37.429, -122.145),(37.428, -122.145),(37.427, -122.145),(37.427, -122.146),(37.427, -122.146)] 
#mymap.addpath(path,"#00FF00") 
mymap.draw('./mymap.draw.html') 
#url = url = './mymap.draw.html'
url = './mymap.draw.html'
webbrowser.open_new_tab(url) 
