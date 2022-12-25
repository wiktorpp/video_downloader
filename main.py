import m3u8_To_MP4

import sys
print(sys.argv)
import os
dir = os.getcwd()
for filename in os.listdir(dir):
    if filename.endswith(".html"):
        html = open(dir+"/"+filename, "r").read()
        url = "https://stream.mux.com/"+html.split("https://stream.mux.com/")[1].split('"')[0]
        name = html.split('data-area="program-title">')[1].split('<')[0]
        collection = html.split('data-area="collection-title">')[1].split("<")[0].strip()
        try: os.mkdir(collection)
        except FileExistsError: pass
        m3u8_To_MP4.multithread_download(
            url, 
            mp4_file_dir=f"./{collection}", 
            mp4_file_name=name
        )
        os.remove(dir+"/"+filename)
