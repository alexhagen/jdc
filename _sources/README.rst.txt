jdc - Jupyter Dynamic Classes
=============================

*Alex Hagen*

``jdc`` is a Jupyter magic made to solve a very specific problem: that
sometimes you want to define classes dynamically in Jupyter notebooks,
and you want it to look good. On `Jupyter’s
Github <https://github.com/jupyter/notebook/issues/1243>`__ there’s a
lengthy discussion and wider view of this issue, but I’ve implemented a
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

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      .. rubric:: Example\ `¶ <#Example>`__
         :name: Example

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      Below is an example on how to use ``jdc``. First we have to import
      the class:

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [1]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     import jdc

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      Then, we have to make a dummy class:

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [2]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     class dog(object):
                         def __init__(self, name, noise):
                             self.name = name
                             self.noise = noise
                             
                             
                     rover = dog('Rover', 'ruff')
                     spot = dog('Spot', 'woof')

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      Then, we want to add a function to that class:

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [3]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     %%add_to dog
                     def bark(self, times=1):
                         saying = ('%s ' % self.noise) * times
                         print("%s says: %s" % (self.name, saying))
                         
                     def bark2(self, times=1):
                         saying = ('%s ' % self.noise) * times
                         print("%s says: %s" % (self.name, saying))

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      And now we can access that function from any method of that class.

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [4]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     rover.bark(1)
                     spot.bark(2)

   .. container:: jp-Cell-outputWrapper

      .. container:: jp-OutputArea jp-Cell-outputArea

         .. container:: jp-OutputArea-child

            .. container:: jp-OutputPrompt jp-OutputArea-prompt

            .. container:: jp-RenderedText jp-OutputArea-output

               ::

                  Rover says: ruff 
                  Spot says: woof woof 

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      If we want to add a function to only one object of that class, we
      can do that, as well:

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [5]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     %%add_to spot
                     def sit(self):
                         print('%s is now sitting' % self.name)

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [6]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     spot.sit()

   .. container:: jp-Cell-outputWrapper

      .. container:: jp-OutputArea jp-Cell-outputArea

         .. container:: jp-OutputArea-child

            .. container:: jp-OutputPrompt jp-OutputArea-prompt

            .. container:: jp-RenderedText jp-OutputArea-output

               ::

                  Spot is now sitting

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      Note that the function added to a class object is only available
      to that object, not all objects of that class:

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [7]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     try: 
                         rover.sit()
                     except AttributeError:
                         print("%s doesn't know that trick" % rover.name)

   .. container:: jp-Cell-outputWrapper

      .. container:: jp-OutputArea jp-Cell-outputArea

         .. container:: jp-OutputArea-child

            .. container:: jp-OutputPrompt jp-OutputArea-prompt

            .. container:: jp-RenderedText jp-OutputArea-output

               ::

                  Rover doesn't know that trick

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      And if we're writing a lot of code, we can now do that in a single
      cell.

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [8]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     %%add_to spot
                     def rollover(self):
                         print("%s rolled over" % self.name)
                         
                     def highfive(self):
                         print("%s is trying to high five you" % self.name)
                         
                     def domytaxes(self):
                         print("%s is just showing off now" % self.name)

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [9]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     spot.rollover()
                     spot.highfive()
                     spot.domytaxes()

   .. container:: jp-Cell-outputWrapper

      .. container:: jp-OutputArea jp-Cell-outputArea

         .. container:: jp-OutputArea-child

            .. container:: jp-OutputPrompt jp-OutputArea-prompt

            .. container:: jp-RenderedText jp-OutputArea-output

               ::

                  Spot rolled over
                  Spot is trying to high five you
                  Spot is just showing off now

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      Nesting functions and decorators should now work. Notice when
      calling the wrapped function that we must call it by
      ``func(self, *args)`` instead of ``self.func(*args)`` or
      ``func(*args)``.

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [10]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     %%add_to dog
                     def race(func):
                         def wrapper(self):
                             import time
                             t1 = time.time()
                             func(self)
                             t2 = time.time()
                             print("A new record time, %s finished in: " % self.name + str((t2 - t1)) + " seconds!\n")
                         return wrapper

                     @race
                     def race_course(self):
                         print("%s finished the course." % self.name)

.. container:: jp-Cell jp-CodeCell jp-Notebook-cell

   .. container:: jp-Cell-inputWrapper

      .. container:: jp-InputArea jp-Cell-inputArea

         .. container:: jp-InputPrompt jp-InputArea-prompt

            In [11]:

         .. container::
         jp-CodeMirrorEditor jp-Editor jp-InputArea-editor

            .. container:: CodeMirror cm-s-jupyter

               .. container:: highlight hl-ipython3

                  ::

                     spot.race_course()

   .. container:: jp-Cell-outputWrapper

      .. container:: jp-OutputArea jp-Cell-outputArea

         .. container:: jp-OutputArea-child

            .. container:: jp-OutputPrompt jp-OutputArea-prompt

            .. container:: jp-RenderedText jp-OutputArea-output

               ::

                  Spot finished the course.
                  A new record time, Spot finished in: 6.29425048828125e-05 seconds!

.. container:: jp-Cell-inputWrapper

   .. container:: jp-InputPrompt jp-InputArea-prompt

   .. container::
   jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput

      and that's it.

Installation
------------

Right now, installation should now work through PyPI:

.. code:: bash


   pip install jdc

Please open up an issue if it doesn’t work, I’ll fix it!

Note
----

@dsblank has pointed this out on the Jupyter discussion: > you can do
this in regular Python, without resorting to any extra magic: > > Cell
1: > > class MyClass(): > def method1(self): > print(“method1”) > Cell
2: > > class MyClass(MyClass): > def method2(self): > print(“method2”) >
Cell 3: > > instance = MyClass() > instance.method1() >
instance.method2() > That is, you can define a class recursively, cell
by cell. I don’t think > the final class is any different from one
defined all in one cell. So you > don’t need an extra package to “solve”
this problem.

I personally like the semantics of ``jdc``, so I won’t be removing it
from PyPI, but it’s always good to know alternatives, thanks @dsblank!
