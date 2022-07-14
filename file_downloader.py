'''Need to download a file from the web?
you can use #python for that ! , 
Here's an example of downloading a zip file!'''

import urllib.request
# f = urllib.request.urlopen("https://some/url")

f = urllib.request.urlopen("https://github.com/khRehman/spelling_correction_python/archive/refs/heads/master.zip")

data = f.read()
with open("data.zip", "wb") as code:
    code.write(data)