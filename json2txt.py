import os
import json

jpath='/home/bai/bzc/jsontotxt/json'
tpath='/home/bai/bzc/jsontotxt/txt'

jfilenames=os.listdir(jpath)

for jfiename in jfilenames:
	jname=os.path.join(jpath,jfiename)
	tname=os.path.join(tpath,jfiename.replace('json', 'txt'))
	print(jname, tname)
	f=open(jname,'r',encoding='utf-8')
	dic=json.load(f)
	keys = dic.keys()
	dic2 = dic.get("annotations")
	
	for k, v in dic2.items():
		# print(k, v)
		up_left = [str(i) for i in v.get("point_up_left")]
		down_right = [str(i) for i in v.get("point_down_right")]
		t = v.get("text")
		s = ','.join(up_left) + ',' + ','.join(down_right) + ',' + ''.join(t.strip().split(' '))
		ff=open(tname,'a',encoding='utf-8')
		ff.write(s)
		ff.write("\n")
	# print(s)
	# print("=============================")

