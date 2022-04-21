import os
import urllib.request
from urllib.parse import urlparse, parse_qs

def download_video(url):
    os.system(f'youtube-dl {url}')




def download_video2(url):
    resp = urllib.request.urlopen(url)
    data = resp.read()

    video_id = list(parse_qs(url).values())[0][0]
    print(f'{video_id =}')

    with open(f'{video_id}.mp4', 'wb') as fh:
        fh.write(data)

    print(f'YOutube video downloaded from {url}')


if __name__ == '__main__':
    download_video('https://www.youtube.com/watch?v=gvVHSndpkEg')
    download_video2('https://www.youtube.com/watch?v=gvVHSndpkEg')
