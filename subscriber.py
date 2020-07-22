
def subscribe(animeName, watchedEp, subList):
    animeName = animeName.replace('"', "")
    for show in subList:
        if animeName.lower() == show["title"].lower():
            show["ep"] = watchedEp
            print("Show already subscribed. Updating episode")
            return subList
    subList.append({"title": animeName, "ep": watchedEp})
    return subList

def unsubscribe(animeName, subList):
    animeName = animeName.replace('"', "")
    for show in subList:
        if animeName.lower() == show["title"].lower():
            logName = show["title"]
            subList.remove(show)
            return logName, True
    return "", False

def unsubAll(subList):
    subList = []
    return subList



