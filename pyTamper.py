#!/usr/bin/env python
import urllib2
import argparse
urls=""
http_method=""
class RequestHttp(urllib2.Request):
    def __init__(self,url,data=None,headers={},origin_req_host=None,unverifiable=False,method=""):
        print type(method),method
        self._method=method
        urllib2.Request.__init__(self,url,data,headers,origin_req_host,unverifiable)
        
    def get_method(self):
        return self._method
def request(urls,methods):
    req=RequestHttp(url=urls,method=methods)
    try:
        opener=urllib2.build_opener(urllib2.HTTPHandler)
        res=opener.open(req)
        return res.read()
    except urllib2.HTTPError as e:
        print "%s:%s" %(e.code,e.read())

def main():
    #http_method=""
    #url=""
    parser=argparse.ArgumentParser()
    parser.add_argument("-u","--url",action="store",dest="url",help="add an url which is the target request",required=True)
    parser.add_argument("-m","--method",action="store",dest="http_method",help="modifiy an method of http")
    args=parser.parse_args()
    print "%s:%s;%s:%s" %(type(args.url),args.url,type(args.http_method),args.http_method)
    #print url,http_method
    #res=request(args.url,args.http_method)
    #req=RequestHttp(url=args.url,method=args.http_method)
    #opener=urllib2.build_opener(urllib2.HTTPHandler)
    #res=opener.open(req)
    print request(args.url,args.http_method)
if __name__ == "__main__":
    main()

    
