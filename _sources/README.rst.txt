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

.. raw:: html

   <div class="cell border-box-sizing text_cell rendered">

.. raw:: html

   <div class="prompt input_prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="text_cell_render border-box-sizing rendered_html">

.. rubric:: Example\ `Â¶ <#Example>`__
   :name: Example

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing text_cell rendered">

.. raw:: html

   <div class="prompt input_prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="text_cell_render border-box-sizing rendered_html">

Below is an example on how to use ``jdc``. First we have to import the
class:

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing code_cell rendered">

.. raw:: html

   <div class="input">

.. raw:: html

   <div class="prompt input_prompt">

In [1]:

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="input_area">

.. raw:: html

   <div class="highlight hl-ipython2">

::

    import jdc

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing text_cell rendered">

.. raw:: html

   <div class="prompt input_prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="text_cell_render border-box-sizing rendered_html">

Then, we have to make a dummy class:

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing code_cell rendered">

.. raw:: html

   <div class="input">

.. raw:: html

   <div class="prompt input_prompt">

In [2]:

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="input_area">

.. raw:: html

   <div class="highlight hl-ipython2">

::

    class dog(object):
        def __init__(self, name, noise):
            self.name = name
            self.noise = noise
            
            
    rover = dog('Rover', 'ruff')
    spot = dog('Spot', 'woof')

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing text_cell rendered">

.. raw:: html

   <div class="prompt input_prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="text_cell_render border-box-sizing rendered_html">

Then, we want to add a function to that class:

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing code_cell rendered">

.. raw:: html

   <div class="input">

.. raw:: html

   <div class="prompt input_prompt">

In [3]:

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="input_area">

.. raw:: html

   <div class="highlight hl-ipython2">

::

    %%add_to dog
    def bark(self, times=1):
        saying = ('%s ' % self.noise) * times
        print "%s says: %s" % (self.name, saying)

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing text_cell rendered">

.. raw:: html

   <div class="prompt input_prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="text_cell_render border-box-sizing rendered_html">

And now we can access that function from any method of that class.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing code_cell rendered">

.. raw:: html

   <div class="input">

.. raw:: html

   <div class="prompt input_prompt">

In [4]:

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="input_area">

.. raw:: html

   <div class="highlight hl-ipython2">

::

    rover.bark(1)
    spot.bark(2)

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="output_wrapper">

.. raw:: html

   <div class="output">

.. raw:: html

   <div class="output_area">

.. raw:: html

   <div class="prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="output_subarea output_stream output_stdout output_text">

::

    Rover says: ruff 
    Spot says: woof woof 

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing text_cell rendered">

.. raw:: html

   <div class="prompt input_prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="text_cell_render border-box-sizing rendered_html">

If we want to add a function to only one object of that class, we can do
that, as well:

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing code_cell rendered">

.. raw:: html

   <div class="input">

.. raw:: html

   <div class="prompt input_prompt">

In [5]:

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="input_area">

.. raw:: html

   <div class="highlight hl-ipython2">

::

    %%add_to spot
    def sit(self):
        print '%s is now sitting' % self.name

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing code_cell rendered">

.. raw:: html

   <div class="input">

.. raw:: html

   <div class="prompt input_prompt">

In [6]:

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="input_area">

.. raw:: html

   <div class="highlight hl-ipython2">

::

    spot.sit()

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="output_wrapper">

.. raw:: html

   <div class="output">

.. raw:: html

   <div class="output_area">

.. raw:: html

   <div class="prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="output_subarea output_stream output_stdout output_text">

::

    Spot is now sitting

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing text_cell rendered">

.. raw:: html

   <div class="prompt input_prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="text_cell_render border-box-sizing rendered_html">

Note that the function added to a class object is only available to that
object, not all objects of that class:

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing code_cell rendered">

.. raw:: html

   <div class="input">

.. raw:: html

   <div class="prompt input_prompt">

In [7]:

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="input_area">

.. raw:: html

   <div class="highlight hl-ipython2">

::

    try: 
        rover.sit()
    except AttributeError:
        print "%s doesn't know that trick" % rover.name

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="output_wrapper">

.. raw:: html

   <div class="output">

.. raw:: html

   <div class="output_area">

.. raw:: html

   <div class="prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="output_subarea output_stream output_stdout output_text">

::

    Rover doesn't know that trick

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing text_cell rendered">

.. raw:: html

   <div class="prompt input_prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="text_cell_render border-box-sizing rendered_html">

And if we're writing a lot of code, we can now do that in a single cell.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing code_cell rendered">

.. raw:: html

   <div class="input">

.. raw:: html

   <div class="prompt input_prompt">

In [8]:

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="input_area">

.. raw:: html

   <div class="highlight hl-ipython2">

::

    %%add_to spot
    def rollover(self):
        print "%s rolled over" % self.name
        
    def highfive(self):
        print "%s is trying to high five you" % self.name
        
    def domytaxes(self):
        print "%s is just showing off now" % self.name

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing code_cell rendered">

.. raw:: html

   <div class="input">

.. raw:: html

   <div class="prompt input_prompt">

In [9]:

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="input_area">

.. raw:: html

   <div class="highlight hl-ipython2">

::

    spot.rollover()
    spot.highfive()
    spot.domytaxes()

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="output_wrapper">

.. raw:: html

   <div class="output">

.. raw:: html

   <div class="output_area">

.. raw:: html

   <div class="prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="output_subarea output_stream output_stdout output_text">

::

    Spot rolled over
    Spot is trying to high five you
    Spot is just showing off now

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="cell border-box-sizing text_cell rendered">

.. raw:: html

   <div class="prompt input_prompt">

.. raw:: html

   </div>

.. raw:: html

   <div class="inner_cell">

.. raw:: html

   <div class="text_cell_render border-box-sizing rendered_html">

and that's it.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Installation
------------

Right now, installation should now work through PyPI:

.. code:: bash


    pip install jdc

Please open up an issue if it doesn't work, I'll fix it!
