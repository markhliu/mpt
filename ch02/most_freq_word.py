news = (
    '''Python is an interpreted, high-level and general-purpose programming
     language. Python's design philosophy emphasizes code readability with
     its notable use of significant whitespace. 
     Its language constructs and object-oriented approach aim to help 
     programmers write clear, logical code for small- and large-scale 
     projects.
    ''')
wdcnt = dict()
wd = news.split()
for w in wd:
    wdcnt[w] = wdcnt.get(w, 0) + 1
print(wdcnt)
for w in list(wdcnt.keys()):
    if wdcnt[w] == max(list(wdcnt.values())):
        print(w)



