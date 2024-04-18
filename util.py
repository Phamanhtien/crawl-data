def getAllATags(tag, aTags): 
    for childTag in tag.keys():
        if type(tag[childTag]) is dict:
            if type(tag[childTag]) is dict:
                if 'href' in tag[childTag]:
                    aTags.append(tag[childTag]['href'])
                getAllATags(tag[childTag], aTags)
        if type(tag[childTag]) is list:
            for childTag in tag[childTag]:
             if type(childTag) is dict: getAllATags(childTag, aTags)

def cleanHref(aTags, domain):
    for i in range(len(aTags)-1):
        if domain in aTags[i]:
            domainLen = len(domain)
            aTags[i] = aTags[i][domainLen -1: len(aTags)]
        if 'http' in aTags:
            aTags[i] = '#'

def classify(aTags):
    classified = {}
    for i in range(len(aTags)-1):
        if aTags[i] != '#':
            parts = aTags[i].split('/')
            if len(parts) > 1:
                if parts[1] not in classified:
                    classified[parts[1]] = []
                classified[parts[1]].append(aTags[i])
    return classified


