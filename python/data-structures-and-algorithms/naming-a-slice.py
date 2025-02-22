url = 'https://cn.bing.com/search?q=dropbox&qs=n&form=QBRE&sp=-1&lq=0'

QUERY_SLICE = slice(url.index('?')+1, len(url))

query_string = url[QUERY_SLICE]

print(query_string)

print(QUERY_SLICE.start)
print(QUERY_SLICE.stop)
print(QUERY_SLICE.step)

print(QUERY_SLICE.indices(len(url)))
