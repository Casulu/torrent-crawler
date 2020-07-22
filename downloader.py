import urllib.request
from cool import getNyaaTorrentUrl
import os


def getNextEpisode(anime):

    url = getNyaaTorrentUrl(anime["title"], anime["ep"])
    if url == "":
        return False
    try:
        os.mkdir("torrents")
    except:
        pass

    torrentpath = f"torrents/{anime['title'] + '_' + str(anime['ep'] + 1)}.torrent"
    open(torrentpath, 'x')
    urllib.request.urlretrieve(url, torrentpath)
    return True
