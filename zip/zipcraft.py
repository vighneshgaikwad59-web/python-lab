z=open("text",mode="w")
z.write("hello world")
z.close

y=open("text2",mode="w")
y.write("hello world 3")
y.close

import zipfile
comp=zipfile.ZipFile("hello world","w")
comp.write("text",compress_type=zipfile.ZIP_DEFLATED)
comp.write("text2",compress_type=zipfile.ZIP_DEFLATED)
comp.close()
print("work done")

obj=zipfile.ZipFile("hello world","r")
obj.extractall("extract content")
obj.close()

