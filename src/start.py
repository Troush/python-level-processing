from PIL import Image
from collections import defaultdict

# Import pygraph
from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import breadth_first_search
# from pygraph.readwrite.dot import write

STEP = 5

im = Image.open('img/extras.png')
by_color = defaultdict(int)


i = 0

# print type(im.getdata())
# pixels = im.getdata()
# for p in range(0,len(im.getdata())):
# 	print pixels[p]
# for pixel in im.getdata():
# 	by_color[pixel] += 1
# # for key in by_color.keys():
# # 	print key,by_color[key]
# print by_color
im = im.resize((150, 150)) 
pix = im.load()
width,height = im.size

color_list = []
colors = {}

for x in range(width):
	for y in range(height):
		colors = {
			str([x,y]) : pix[x,y]
		}
		color_list.append(colors)
		# print pix[x,y]
# print color_list
# for c in color_list:
# 	print c.keys()[0],c[c.keys()[0]]
# for p in range(len(color_list)):
# 	gr.add_nodes(color_list[p].get('cord'))
# for p in range(len(color_list)):
# 	if (color_list[p].get(
# # print len(color_list)