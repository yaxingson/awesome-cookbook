# 目录

## 制作模块的层次包

> 命名空间包

Python软件包结构:

```txt
|-- graphics/
  | -- __init__.py  # 包含可选的初始化代码
  | -- primitive/
    |-- __init__.py
    |-- line.py
    |-- fill.py
    |-- text.py
  |-- formats/
    |-- __init__.py
    |-- png.py
    |-- jpg.py

```

`__init__.py`文件的常见用法:

1. 自动加载子模块:

```py
# graphics/formats/__init__.py
from . import jpg
from . import png

```

2. 从多个文件中把定义统一到一个单独的逻辑命名空间中

> 当未定义`__init__.py`文件时，程序会创建一个"命名空间包"

## 控制所有内容的导入

当使用`from module import *`导入语句时，在模块中定义变量`__all__`，可以显式列出可导出的符号名:

```py
class FormatError:
  pass

class UnsupportedError:
  pass

# 模块私有符号名
def _decode_config():
  pass

def decode():
  pass

__all__ = ['decode']

```

> 当`__all__`中包含未定义的名称时，执行import语句时会抛出`AttributeError`异常


## 使用相对名称导入包子模块

要在软件包的子模块中导入同一个包中其他的子模块，请使用相对名称来导入:

```py
from .encode import *

# 使用完整的绝对名称，缺点是将最顶层的包名称硬编码到源码中（不推荐）
from image.png.decode import *

```
> import语句中的`.`和`..`语法只能用在`from xx import yy`导入语句中

位于包顶层目录的模块或包中的模块直接以脚本的形式执行时不能使用相对导入

## 将模块拆分为多个文件

可以通过将模块转换为包的方式将模块分解为多个单独的文件:

```py
# utils.py
def base64():
  pass

def md5():
  pass

```
创建一个包目录，并通过`__init__.py`将各个模块文件拼接在一起:


```txt
|-- utils/
  |-- __init__.py
  |-- encoding.py
  |-- crypto.py

```

```py
# __init__.py
from .encoding import base64
from .crypto import md5

```

引入惰性导入:

```py
# __init__.py

def base64():
  from .encoding import base64
  return base64()

def md5():
  from .crypto import md5
  return md5()

```

> 惰性加载有时会破坏继承或类型检查机制

## 在公共命名空间下制作独立的代码目录

## 重新加载模块

## 使目录或压缩文件可作为主脚本运行

## 在包内读取数据文件

## 将目录添加到 sys.path

## 使用字符串中给定的名称导入模块

## 使用导入钩子从远程机器加载模块

## 在导入时修补模块

## 仅为自己安装包

安装自定义包或第三方包到用户级目录:

```sh
$ python setup.py install --user

$ python install --user package_name

```


## 创建新的 Python 环境

## 分发包

典型的程序库目录结构:

```txt
|-- project_name/
  |-- README.md
  |-- doc/
  |-- project_name/
    |-- __init__.py
    |-- foo.py
    |-- bar.py
    |-- utils/
      |-- __init__.py
      |-- spam.py
  |-- examples/

```

编写`setup.py`文件:

```py
# setup.py
from distutils.core import setup

setup(
  name='',
  version='',
  author='',
  author_email='',
  url='',
  # 必须列出包中的每个子目录
  packages=['project_name', 'project_name.utils']
)

```
创建`MANIFEST.in`文件，指定希望包含在包中的非源码文件:

```in
# MANIFEST.in
include *.md
recursive-include examples *
recursive-include doc *

```

创建源代码级的分发包:

```sh
$ bash python setup.py sdist

```

> [Python Package Index](https://pypi.org/)
