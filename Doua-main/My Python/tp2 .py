import os

os.makedirs("test_dir2")
if os.path.exists("test_dir2"):
   print("file is exist")
else:
    print("file not founded")

