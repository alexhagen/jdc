# jdc - Jupyter Dynamic Classes

*Alex Hagen*

``jdc`` is a Jupyter magic made to solve a very specific problem: that sometimes
you want to define classes dynamically in Jupyter notebooks, and you want it to
look good.  On
[Jupyter's Github](https://github.com/jupyter/notebook/issues/1243) there's a
lengthy discussion and wider view of this issue, but I've implemented a quickfix
which I think ended up looking pretty semantic.  Thanks to
[Igor Sobreira](http://igorsobreira.com/2011/02/06/adding-methods-dynamically-in-python.html)
for the underlying IPython.

The example below will be most informative, but basically all ``jdc`` allows you
to do is to add a cell and define

```python
%%add_to our_class
def our_function(self, our_variable):
  print our_variable
```

and that will add the method ``our_function`` to ``our_class``, whether
``our_class`` is a class, or an object with a class type.


## Installation

Right now, installation should now work through PyPI:

```bash

pip install jdc

```

Please open up an issue if it doesn't work, I'll fix it!

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