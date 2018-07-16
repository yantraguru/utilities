import sys
import requests

data_url = sys.argv[1]
local_filename = sys.argv[2]

print data_url
print local_filename

kaggle_info = {'UserName': "XXXXX", 'Password': "XXXX"}

r = requests.get(data_url)
r = requests.post(r.url, data = kaggle_info)
f = open(local_filename, 'w')
for chunk in r.iter_content(chunk_size = 512 * 1024):
    if chunk:
        f.write(chunk)
f.close()

