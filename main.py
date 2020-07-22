#!usr/bin/env python 3.8
import sys
import json
import subscriber
from downloader import getNextEpisode


def printOptions():
    print("1. Add subscription")
    print("2. Remove subscription")
    print("3. List subscriptions")
    print("q. Exit")


def printSubList(subList):
    print()
    for show in subList:
        print(f"{subList.index(show) + 1}. \"{show['title']}\" at ep: {show['ep'] + 1}")
    print()

def startMenu():
    inp = ''
    while inp != 'q':
        printOptions()
        inp = input()
        if inp == '1':
            subinp = ''
            print("Input subscription with format: 'Series name', 'last episode watched'")
            print("Exit by inputting 'q'")
            while subinp != "q":
                subinp = input()
                if subinp != 'q':
                    subinp = subinp.split(',')
                    if len(subinp) == 2:
                        subscriber.subscribe(subinp[0], int(subinp[1]), subList)
                        logInp = subinp[0].replace('"', "")
                        print(f"Subscribed to {logInp}")
                    else:
                        print("Could not interpret input")
        elif inp == '2':
            subinp = ''
            print("Input name of the anime to remove from subscription list.")
            print("Exit by inputting 'q'. Input 'all' to clear subscriptions")
            while subinp != "q":
                subinp = input()
                if subinp != 'q':
                    output = subscriber.unsubscribe(subinp, subList)
                    if output[1]:
                        print(f"Unsubscribed to {output[0]}.")
                    else:
                        print("Could not find specified anime in list")
        elif inp == '3':
            printSubList(subList)

#///////////////////////////////////////////////////////////////////////
subList = []
try:
    open('subscriptions.json', 'x')
except FileExistsError:
    try:
        with open('subscriptions.json', 'r') as readfile:
            subList = json.load(readfile)
    except json.decoder.JSONDecodeError:
        pass

if sys.argv[1] == "crawl":
    for anime in subList:
        print(f"Finding next episode for {anime['title']}")
        if getNextEpisode(anime):
            print(f"Episode {anime['ep'] + 1} was found!\n")
            subList[subList.index(anime)]["ep"] = subList[subList.index(anime)]["ep"] + 1
        else:
            print("No new episode was found\n")
elif sys.argv[1] == "menu":
    startMenu()
else:
    exit(f'\"{sys.argv[1]}\" is not a recognized argument')
with open("subscriptions.json", 'w') as outfile:
    json.dump(subList, outfile, indent=4)