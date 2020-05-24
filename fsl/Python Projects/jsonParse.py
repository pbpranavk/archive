import json
import requests
import first
from contextlib import closing

url = "http://openlibrary.org/search.json?q="


if __name__ == '__main__':
    print("Enter the title of the book that you want to search for:")
    title = input()
    title = title.split(' ')
    title = "+".join(title)
    resp = requests.get(url+title)
    #print(resp.content)
    resp = resp.json()
    #print(resp)
    #resp = resp.docs[0]
    #for(k,v) in resp.items():
    #    if k=='subject':
    #        print("Key = "+k,end ='')
    #        print("Value = "+v)
    f = open('response.txt','w')
    #f.write(resp)
    for(k,v) in resp.items():
    #    if k=='subject':
            f.write("Key ="+str(k)+" ")
            try:
                f.write("Value = "+str(v)+"\n")
            except Exception as e:
                pass
    f.close()
    print('Done')
