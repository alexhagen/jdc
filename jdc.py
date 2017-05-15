from IPython.core.magic import (Magics, magics_class, line_cell_magic)
import inspect

ip = get_ipython()

@magics_class
class jdc_magics(Magics):

    @line_cell_magic
    def add_to(self, line, cell):
        """ adds a method to a class or object

            :param line: the method or class to add to
            :param cell: a python string defining class method that will be
                added to the class or object
        """
        lcls = ip.user_module.__dict__
        if line in lcls.keys():
            if inspect.isclass(lcls[line]):
                isclass = True
            else:
                isclass = False
                objecttype = eval('type(%s).__name__' % line, lcls)

        funcname = cell.split('(')[0]
        funcname = funcname.replace("def ", "")
        run_str = "%s\n" % cell
        run_str += "\n\n"
        if isclass:
            run_str += "%s.%s = %s\n" % (line, funcname, funcname)
        else:
            run_str += 'from types import MethodType\n'
            run_str += "%s.%s = MethodType(%s, %s)\n" % (line, funcname, funcname, line)
        exec(run_str, lcls)

ip.register_magics(jdc_magics)
