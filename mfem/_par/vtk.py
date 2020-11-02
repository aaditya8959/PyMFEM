# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _vtk
else:
    import _vtk

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _vtk.SWIG_PyInstanceMethod_New
_swig_new_static_method = _vtk.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._par.element
import mfem._par.globals
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
VTKFormat_ASCII = _vtk.VTKFormat_ASCII

VTKFormat_BINARY = _vtk.VTKFormat_BINARY

VTKFormat_BINARY32 = _vtk.VTKFormat_BINARY32


def CreateVTKElementConnectivity(con, geom, ref):
    r"""CreateVTKElementConnectivity(intArray con, mfem::Geometry::Type geom, int ref)"""
    return _vtk.CreateVTKElementConnectivity(con, geom, ref)
CreateVTKElementConnectivity = _vtk.CreateVTKElementConnectivity

def WriteVTKEncodedCompressed(out, bytes, nbytes, compression_level):
    r"""WriteVTKEncodedCompressed(std::ostream & out, void const * bytes, uint32_t nbytes, int compression_level)"""
    return _vtk.WriteVTKEncodedCompressed(out, bytes, nbytes, compression_level)
WriteVTKEncodedCompressed = _vtk.WriteVTKEncodedCompressed

def BarycentricToVTKTriangle(b, ref):
    r"""BarycentricToVTKTriangle(int * b, int ref) -> int"""
    return _vtk.BarycentricToVTKTriangle(b, ref)
BarycentricToVTKTriangle = _vtk.BarycentricToVTKTriangle

def VTKByteOrder():
    r"""VTKByteOrder() -> char const *"""
    return _vtk.VTKByteOrder()
VTKByteOrder = _vtk.VTKByteOrder


