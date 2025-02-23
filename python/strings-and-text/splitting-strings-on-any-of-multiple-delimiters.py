import re

line = 'agent-gpt allows; you, to,configure,  and'

print(re.split(r'[;,\s]\s*', line))

# 当正则表达式模式中包含捕获组时，最终结果也会包含匹配的文本
fields = re.split(r'(;|,|\s)\s*', line)

print(fields)

# 使用非捕获组（?:）
fields = re.split(r'(?:;|,|\s)\s*', line)

print(fields)
