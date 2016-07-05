def shorten(url):
    slen=len(url)
    url=url.lower()
    if url.startswith("www."):
        url=url[4:]
    endex=url.index('.')
    end=url[endex:]
    url=url[:endex]
    newurl = ''.join([l for l in url if l not in ['a','e','i','o','u']])
    return str(len(newurl+end))+'/'+str(slen)

if __name__ == "__main__":
    for tc in xrange(int(raw_input())):
        print shorten(raw_input())
