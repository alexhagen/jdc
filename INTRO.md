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
