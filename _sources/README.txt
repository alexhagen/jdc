jdc - Jupyter Dynamic Classes
=============================

*Alex Hagen*

``jdc`` is a Jupyter magic made to solve a very specific problem: that
sometimes you want to define classes dynamically in Jupyter notebooks,
and you want it to look good. On `Jupyter's
Github <https://github.com/jupyter/notebook/issues/1243>`__ there's a
lengthy discussion and wider view of this issue, but I've implemented a
quickfix which I think ended up looking pretty semantic. Thanks to `Igor
Sobreira <http://igorsobreira.com/2011/02/06/adding-methods-dynamically-in-python.html>`__
for the underlying IPython.

The example below will be most informative, but basically all ``jdc``
allows you to do is to add a cell and define

.. code:: python

    %%add_to our_class
    def our_function(self, our_variable):
      print our_variable

and that will add the method ``our_function`` to ``our_class``, whether
``our_class`` is a class, or an object with a class type.

.. code:: python

    import jdc.jdc as jdc

.. code:: python

    class func(object):
        def __init__(self, A):
            self.A = A

    one = func(1.0)
    two = func(2.0)

.. code:: python

    %%add_to func
    def y(self, x):
        print self.A * x**2

.. code:: python

    one.y(5.0)

.. code:: python

    %%add_to two
    def z(self, x):
        print self.A * x**3

.. code:: python

    two.y(5.0)

.. code:: python

    two.z(5.0)

.. code:: python

    try: 
        one.z(5.0)
    except AttributeError:
        print "See, it doesn't have it!"

Installation
------------

Right now, installation is pretty manual, but I'll be working on this.
The easiest way to install would be to make your own utilities directory

.. code:: bash

    mkdir ~/util
    cd ~/util

and clone the repo into it

.. code:: bash

    git clone https://github.com/alexhagen/jdc

and then add that directory into your ``PYTHONPATH``

.. code:: bash

    sudo echo "export PYTHONPATH=${PYTHONPATH}:~/util" >> ~/.bashrc

Then you can

.. code:: python

    import jdc.jdc as jdc

in any Jupyter notebook.
