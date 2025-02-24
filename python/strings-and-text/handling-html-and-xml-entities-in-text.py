from html import unescape
from html.parser import HTMLParser
from xml.sax.saxutils import unescape as xml_unescape

s = 'Spicy &quot;Jalape&#241;o&quot'

parser = HTMLParser()

print(parser.unescape(s)) # Spicy "Jalapeño"
print(unescape(s)) # Spicy "Jalapeño"

t = 'the prompt is &gt;&gt;&gt;'

print(xml_unescape(t)) # the prompt is >>>
