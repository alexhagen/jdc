## Note

@dsblank has pointed this out on the Jupyter discussion:
> you can do this in regular Python, without resorting to any extra magic:
> 
> Cell 1:
> 
> class MyClass():
>     def method1(self):
>         print("method1")
> Cell 2:
> 
> class MyClass(MyClass):
>     def method2(self):
>         print("method2")
> Cell 3:
> 
> instance = MyClass()
> instance.method1()
> instance.method2()
> That is, you can define a class recursively, cell by cell. I don't think > the final class is any different from one defined all in one cell. So you > don't need an extra package to "solve" this problem.

I personally like the semantics of `jdc`, so I won't be removing it from PyPI, but it's always good to know alternatives, thanks @dsblank!