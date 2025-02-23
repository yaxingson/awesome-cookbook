from fnmatch import fnmatch, fnmatchcase

# `fnmatch()`匹配模式的大小写区分规则和操作系统的底层文件系统相同
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

# `fnmatchcase()`匹配模式的大小写区分规则和操作系统的底层文件系统无关
print(fnmatchcase('foo.txt', '*.TXT'))
