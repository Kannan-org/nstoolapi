import requests 
from bs4 import BeautifulSoup 
import time

urls ='http://ns.tools/'

def api_call(): 
    # the target we want to open	 
    dom = input("Enter dom : ")
    url = urls+dom
    #open with GET method 
    resp=requests.get(url) 
    time.sleep(5)
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        print("Successfully opened the web page") 
        print("The Overall Score as Follows:- \n") 

    # we need a parser,Python built-in HTML parser is enough . 
        soup=BeautifulSoup(resp.text,'html.parser')	 

    # l is the list which contains all the text i.e news 
        l=soup.find("span",{"class":"__score-title"})
        dns=soup.find("div",{"id":"score__dns__disp"})
        domain=soup.find("div",{"id":"score__domain__disp"})
        mail=soup.find("div",{"id":"score__mail__disp"})
        web=soup.find("div",{"id":"score__web__disp"})
        score=soup.find("span",{"itemprop":"ratingValue"})

    #now we want to print only the text part of the anchor. 
    #find all the elements of a, i.e anchor 
        print("The detailed Score for DNS  are below.:- \n")
        print(dns.string)
        print("The detailed Score for Domain are below.:- \n")
        print(domain.string)
        print("The detailed Score for mail are below.:- \n")
        print(mail.string)
        print("The detailed Score for web are below.:- \n")
        print(web.string)
        print("___________________________________________________________ \n")
        print(l.string)
        print("____________________________________________________________ \n")
        print(score.string)
    else: 
        print("Error") 
		
if __name__ == "__main__":
    api_call()