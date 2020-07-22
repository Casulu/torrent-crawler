from crawler import getLinks


def search(dictionary, substr):
    for key in dictionary:
        if substr in key:
            return key
    return None


def getNyaaTorrentUrl(query, watchedEp):
    baseUrl = "https://nyaa.si/"
    userSearch = "/user/HorribleSubs"
    queryformat = "?f=0&c=0_0&q="
    downloadUrl = ""

    if watchedEp + 1 < 10:
        epString = '0' + f'{watchedEp + 1}'
    else:
        epString = f'{watchedEp + 1}'

    query = query + f"+-+{epString} " "[1080p]"
    query = query.replace(" ", "+")

    searchUrl = baseUrl + userSearch + queryformat + query

    torrentLinks = getLinks(searchUrl, titlelinks=True)
    epKey = search(torrentLinks, f" - {epString} ")
    if epKey != None:
        epPage = torrentLinks[epKey]
        downloadUrl = baseUrl + "download/" + epPage[5:] + ".torrent"
    return downloadUrl
