from bs4 import BeautifulSoup, NavigableString
from pprint import pprint
import re
import sys

'''
from imdb import IMDB


m = IMDB(html)
print m.getName()
print m.getRating()
print m.getCategory()
print m.getRateReview()
print m.getPublishDateAndLocation()

Output:
Rush
8.3
['Action', 'Biography', 'Drama']
{'total_critic_review': '362', 'total_rate': '155746', 'total_user_review': '364'}
('13 September 2013', 'UK')

'''

class IMDB(object):
    """Get all information of a imdb movie, pass html text of imdb page"""

    def __init__(self, html=None):
        if not html:
            self.soup = None
        else:
            self.soup = BeautifulSoup(html)

    def setSoup(self,html):
        self.soup = BeautifulSoup(html)

    def printMatch(self,m):
        if m:
            return m.group(0)
        else:
            return "NF"

    def getRating(self):
        #print "Get rating ...."
        #soup = BeautifulSoup(html)
        for imdbHtmlPage in self.soup.find_all("div", "star-box-giga-star"):
            #print imdbHtmlPage
            m=re.search(r'\d+.*\d+',"'"+str(imdbHtmlPage)+"'")
            #pprint( "Rate: "+printMatch( m ) )
            return self.printMatch( m )
        return None

    def getName(self):
        for imdbData in self.soup.find_all("h1", "header"):
            #print imdbData
            return self.__getNameFromTag(str(imdbData))

    def getCategory(self):
        w=[]
        for imdbData in self.soup.find_all("div", "infobar"):
            ps = BeautifulSoup(str(imdbData))
            for link in ps.find_all('a'):
                try:
                    cat = str(link.span.string)
                    #print "cat",cat
                    w.append( cat )
                except :
                    pass
        return w

    def getRateReview(self):
        r = {}
        for s in self.soup.find_all("div", "star-box-details"):
            k = 0
            for d in s.select("a > span"):
                #print d.get_text()
                if k == 0:
                    r["total_rate"] = str( d.get_text() ).replace(",","")
                elif k == 1:
                    r["total_user_review"] = str( d.get_text().split(" ")[0] ).replace(",","")
                elif k == 2:
                    r["total_critic_review"] = str( d.get_text().split(" ")[0] ).replace(",","")
                    break
                k += 1
        return r

    def getPublishDateAndLocation(self):
        for imdbData in self.soup.find_all("div", "infobar"):
            ps = BeautifulSoup(str(imdbData))
            for link in ps.find_all('a'):
                if not hasattr(link.span,"string"):
                    try:
                        p = link.get_text()
                        w = p.split()
                        publish_date = w[0]+" "+w[1]+" "+w[2]

                        publish_location = w[3]
                        publish_location = publish_location.replace("(","")
                        publish_location = publish_location.replace(")","")

                        return publish_date, publish_location
                    except :
                        pass
        return None, None

    def __getNameFromTag(self,s):
        try:
            nSoup = BeautifulSoup(s);
            #print "K: ",nSoup.span.string
            return nSoup.span.string
#            b=s.find(">")+1
#            e=s.find("<",b)
#            rt = s[b:e]
#            rt = rt.strip()
#            return rt
        except :
            print str(sys.exc_info())
        return None