# 目录

## 四舍五入数值

将一个浮点数取整到固定的小数位:

```py
print(round(1.25, 1)) # 1.2
print(round(1.26, 1)) # 1.3
print(round(-1.21, 1)) # -1.2

# 当值恰好等于两个整数间的一半时，取整操作会取离该值最接近的偶数
print(round(1.5)) # 2

a = 1627731

# 参数`ndigits`为负数时，会相应地取整到十位、百位和千位等
print(round(a, -1)) # 1627730
print(round(a, -2)) # 1627700
print(round(a, -3)) # 1628000

```

以固定的精度位数输出数值:

```py
x = 1.23456

print(format(x, '0.3f')) # '1.235'
print('{:0.3f}'.format(x)) # '1.235'

```

不要采用对浮点数取整的方式”修正“精度上的问题:

```py
a = 2.1
b = 4.2

c = a + b

print(c) # 6.300000000000001
print(round(c, 2)) # 6.3

```

## 进行精确的小数计算

> 浮点数误差实际是底层CPU的浮点运算单元和IEEE 754浮点数算术标准的一种特性

利用`decimal`模块:

```py
from decimal import Decimal, localcontext

a = Decimal('4.2')
b = Decimal('2.2')

c = a + b

print(c) # '6.4'
print(c == Decimal('6.4')) # True

print(a / b) # '1.909090909090909090909090909'

# 创建一个本地上下文环境修改默认设定
with localcontext() as ctx:
  ctx.prec = 50
  print(a / b) # '1.9090909090909090909090909090909090909090909090909'

```

> 通用十进制算术规范

大数和小数相加导致的误差:

```py
import math

numbers = [1.23e+18, 1, -1.23e+18]

print(sum(numbers)) # 0.0
print(math.fsum(numbers)) # 1.0

```

## 格式化数字以输出

数值格式化输出:

```py
x = 1234.56789

print(format(x, '0.2f')) # '1234.57'
print(format(x, '>10.1f')) # '    1234.6'

# 包含千位分隔符，指定宽度和精度的一般格式为'[<>^]?width[,]?(.digits)?'
print(format(x, ',')) # '1,234.56789'
print(format(x, '0,.1f')) # '1,234.6'

# 采用科学计数法表示形式
print(format(x, 'e')) # '1.234568e+03'
print(format(x, '0.2E')) # '1.23E+03'

```

特定于本地环境的千位分隔符:

```py
import locale 

x = 1234567.89

swap_separators = { ord('.'):',', ord(','):'.' }

print(format(x, ',')) # '1,234,567.89'
print(format(x, ',').translate(swap_separators)) # '1.234.567,89'

```

## 处理二进制、八进制和十六进制整数

将一个整数转换为二进制、八进制或十六进制的文本字符串:

```py
x = 1234

print(bin(x)) # 0b10011010010
print(oct(x)) # 0o2322
print(hex(x)) # 0x4d2

print(format(x, 'b')) # 10011010010
print(format(x, 'o')) # 2322
print(format(x, 'x')) # 4d2

# 转换负整数时，输出也会带有符号
# 当需要产生一个无符号数值时，需要加上最大值来设置比特位的长度

print(format(-x, 'b')) # -10011010010
print(format(2**32 + (-x), 'b')) # 11111111111111111111101100101110

```

将字符串形式的整数转换为不同的进制:

```py
print(int('4d2', 16)) # 1234
print(int('1001010001', 2)) # 593

```

> Python中请确保在八进制数前添加0o前缀

```py
import os

os.chmod('script.py', 0o755)

```

## 从字节打包和解包大整数

## 进行复数数学运算

复数的表示和算术运算操作:

```py
import cmath

a = complex(2, 4)
b = 3 - 5j

print((a.real, a.imag)) # (2.0, 4.0)
print(b.conjugate()) # (3+5j)

print(a + b) # (5-1j)
print(a - b) # (-1+9j)
print(a * b) # (26+2j)
print(a / b) # (-0.4117647058823529+0.6470588235294118j)
print(abs(a)) # 4.47213595499958

# 求复数的正弦、余弦和平方根
print(cmath.sin(a)) # (24.83130584894638-11.356612711218174j)
print(cmath.cos(a)) # (-11.36423470640106-24.814651485634187j)
print(cmath.exp(a)) # (-4.829809383269385-5.5920560936409816j)

```

使用python模块处理复数:

```py
import math
import cmath
import numpy as np

a = np.array([2+3j, 4-5j, 6-7j, 8+9j])

print(a)
print(a + 2)
print(np.sin(a))

try:
  # 标准数学函数库默认情况下不会产生复数值
  math.sqrt(-1)
except ValueError as e:
  pass

print(cmath.sqrt(-1)) # 1j

```

## 处理无穷大和NaN

处理浮点数中的无穷大、负无穷大和NaN:

```py
import math

a = float('inf')
b = float('-inf')
c = float('nan')

print(a, math.isinf(a))
print(b, math.isinf(b))
print(c, math.isnan(c))

# 无穷大值在数学计算中会传播
print(a + 45) # inf
print(a * 10) # inf
print(10 / a) # 0.0

# 产生NaN的某些特定操作
print(a / a) # nan
print(a + b) # nan

# NaN会通过所有的操作传播，且不会引发异常
print(c + 23) # nan
print(c / 2) # nan
print(c * 2)  # nan
print(math.sqrt(c)) # nan

```

NaN在做比较时从不会被判定为相等，唯一安全检测NaN的方法是调用`math.isnan()`:


```py
import math

d = float('nan')
e = float('nan')

print(d == e) # False
print(d is e) # False
print(math.isnan(d)) # True

```

## 使用分数进行计算

## 处理大数值数组

## 进行矩阵和线性代数计算

## 随机选择事物

## 将天数转换为秒，以及其他基本时间转换

## 确定上周五的日期

## 查找当前月份的日期范围

## 将字符串转换为日期时间

## 操作涉及时区的日期
