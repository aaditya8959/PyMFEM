# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_point')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_point')
    _point = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_point', [dirname(__file__)])
        except ImportError:
            import _point
            return _point
        try:
            _mod = imp.load_module('_point', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _point = swig_import_helper()
    del swig_import_helper
else:
    import _point
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


import mfem._par.element
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.densemat
import mfem._par.vector
import mfem._par.operators
import mfem._par.matrix
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.hash
class Point(mfem._par.element.Element):
    """Proxy of C++ mfem::Point class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.element.Element]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.element.Element]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Point, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::Point self) -> Point
        __init__(mfem::Point self, int const * ind, int attr=-1) -> Point
        __init__(mfem::Point self, int const * ind) -> Point
        """
        this = _point.new_Point(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetType(self):
        """GetType(Point self) -> mfem::Element::Type"""
        return _point.Point_GetType(self)


    def GetVertices(self, *args):
        """
        GetVertices(Point self, intArray v)
        GetVertices(Point self) -> int *
        """
        return _point.Point_GetVertices(self, *args)


    def GetNVertices(self):
        """GetNVertices(Point self) -> int"""
        return _point.Point_GetNVertices(self)


    def GetNEdges(self):
        """GetNEdges(Point self) -> int"""
        return _point.Point_GetNEdges(self)


    def GetEdgeVertices(self, ei):
        """GetEdgeVertices(Point self, int ei) -> int const *"""
        return _point.Point_GetEdgeVertices(self, ei)


    def GetNFaces(self, nFaceVertices):
        """GetNFaces(Point self, int & nFaceVertices) -> int"""
        return _point.Point_GetNFaces(self, nFaceVertices)


    def GetFaceVertices(self, fi):
        """GetFaceVertices(Point self, int fi) -> int const *"""
        return _point.Point_GetFaceVertices(self, fi)


    def Duplicate(self, m):
        """Duplicate(Point self, mfem::Mesh * m) -> Element"""
        return _point.Point_Duplicate(self, m)

    __swig_destroy__ = _point.delete_Point
    __del__ = lambda self: None
Point_swigregister = _point.Point_swigregister
Point_swigregister(Point)

# This file is compatible with both classic and new-style classes.

cvar = _point.cvar

