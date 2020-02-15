##### `__name__`的作用

```python
if __name__ == '__main__'：
```

- 每个模块都有一个`__name__`属性，当其值是`__main__`时，表明该模块自身在运行，否则是被引入



##### 假判断

```
1、None --> None值

2、False --> False值

3、0 --> 数值零不管它是int,float还是complex类型

4、'',(),[] --> 任何一个空的序列

5、{} --> 空的集合

6、对于instance 如果它的__bool__()函数返回False 就判断为False
```



##### 列表操作

```
1、list.append(obj) 在列表末尾添加新的对象

2、list.count(obj) 统计某个元素在列表中出现的次数

3、list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

4、list.index(obj) 从列表中找出某个值第一个匹配项的索引位置

5、list.insert(index, obj) 将对象插入列表

6、list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

7、list.remove(obj) 移除列表中某个值的第一个匹配项
```



##### 数据类型

在 python 中，类型属于对象，变量是没有类型的：

```python
a=[1,2,3]

a="Runoob"
```

`[1,2,3]` 是 List 类型，`"Runoob"` 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用，可以是指向 List 类型对象，也可以是指向 String 类型对象。



##### 读和写文件

open() 将会返回一个 file 对象，基本语法格式如下:

```python
f = open(filename, mode)
```

- filename：包含了你要访问的文件名称的字符串值

- mode：决定了打开文件的模式：只读，写入，追加等


| 模式 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |

```
f.write()
f.read()
f.readline()
f.readlines()
f.tell()
f.seek(offset, from_what) 
```

- f.readline：如果返回一个空字符串, 说明已经已经读取到最后一行

- f.readlines ：将返回该文件中包含的所有行，放在数组里面

- f.tell：返回文件对象当前所处的位置

- f.seek改变文件当前的位置

  ```
  from_what：0 表示开头, 1 表示当前位置, 2 表示文件的结尾
  seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
  seek(x,1) ： 表示从当前位置往后移动x个字符
  seek(-x,2)：表示从文件的结尾往前移动x个字符
  ```



##### with-as表达式

有一些任务，可能事先需要设置，事后做清理工作。对于这种场景，Python的`with语句`提供了一种非常方便的处理方式。一个很好的例子是文件处理，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。

如果不用with语句，代码如下：

```python
file = open("/tmp/foo.txt")
data = file.read()
file.close()
```

这里有两个问题：

- 一是可能忘记关闭文件句柄
- 二是文件读取数据发生异常，没有进行任何处理

with版本的代码

```python
with open("/tmp/foo.txt") as file:
    data = file.read()
```



##### with如何工作

- 紧跟with后面的语句，**求值后，得到一个匿名返回对象**
-  调用返回对象的`__enter__() `方法，将返回值赋值给as后面的变量
- 当with后面的代码块全部被执行完之后，将调用**返回对象**的 `__exit__()`方法

```python
class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"
    
    def __exit__(self, type, value, trace):
        print "In __exit__()"

def get_sample():
    return Sample()

with get_sample() as sample:
    print "sample:", sample
```

```
In __enter__()
sample: Foo
In __exit__()
```



##### 函数声明

```
def init(name, age = 5, *args, **kwargs):
```

- 调用函数时，如果没有传递参数，则会使用默认参数（age = 5）
- 加了星号 `*` 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
- 加了两个星号`**` 的参数会以字典的形式导入



##### 类-面向对象

- 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的**第一个参数名称**

- self代表类的实例，而非类

  ```python
  class Complex:
      def __init__(self, realpart, imagpart):
          self.r = realpart
          self.i = imagpart
  
  x = Complex(3.0, -4.5)
  ```

- 类的私有属性：**两个下划线开头**，声明该属性为私有，不能在类的外部被使用或直接访问
- 类的私有方法：**两个下划线开头**，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用



##### `_init__、__del__与__new__`

- `__init__(self, *args, **kwargs)`：在创建对象后被自动调用
- `__del__(self)`：在对象销毁时被调用，往往用于清除数据或还原环境等操作
- `__new__(cls, *args, **kwargs)`：实例化时调用的第一个方法

