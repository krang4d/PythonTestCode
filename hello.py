#!/usr/bin/env python
#coding: utf-8
import urllib.request

i = 5

print ( u"Hello%d, World!"  %i, u"Привет, Мир!" )
print ( type(i) )

import keyword; print ( keyword.kwlist)


url = 'http://www.ya.ru'
r = urllib.request.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text.encode('cp1251'))

