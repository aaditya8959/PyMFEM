# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pmesh
else:
    import _pmesh

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

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

MFEM_VERSION = _pmesh.MFEM_VERSION

MFEM_VERSION_STRING = _pmesh.MFEM_VERSION_STRING

MFEM_VERSION_TYPE = _pmesh.MFEM_VERSION_TYPE

MFEM_VERSION_TYPE_RELEASE = _pmesh.MFEM_VERSION_TYPE_RELEASE

MFEM_VERSION_TYPE_DEVELOPMENT = _pmesh.MFEM_VERSION_TYPE_DEVELOPMENT

MFEM_VERSION_MAJOR = _pmesh.MFEM_VERSION_MAJOR

MFEM_VERSION_MINOR = _pmesh.MFEM_VERSION_MINOR

MFEM_VERSION_PATCH = _pmesh.MFEM_VERSION_PATCH

MFEM_SOURCE_DIR = _pmesh.MFEM_SOURCE_DIR

MFEM_INSTALL_DIR = _pmesh.MFEM_INSTALL_DIR

MFEM_TIMER_TYPE = _pmesh.MFEM_TIMER_TYPE

MFEM_HYPRE_VERSION = _pmesh.MFEM_HYPRE_VERSION

import mfem._par.mesh
import mfem._par.matrix
import mfem._par.vector
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.operators
import mfem._par.ncmesh
import mfem._par.element
import mfem._par.densemat
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.coefficient
import mfem._par.sparsemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.fespace
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.handle
import mfem._par.hypre
import mfem._par.bilininteg
import mfem._par.linearform
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
class ParMesh(mfem._par.mesh.Mesh):
    r"""Proxy of C++ mfem::ParMesh class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Finalize(self, refine=False, fix_orientation=False):
        r"""Finalize(ParMesh self, bool refine=False, bool fix_orientation=False)"""
        return _pmesh.ParMesh_Finalize(self, refine, fix_orientation)

    def GetComm(self):
        r"""GetComm(ParMesh self) -> MPI_Comm"""
        return _pmesh.ParMesh_GetComm(self)

    def GetNRanks(self):
        r"""GetNRanks(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNRanks(self)

    def GetMyRank(self):
        r"""GetMyRank(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetMyRank(self)
    gtopo = property(_pmesh.ParMesh_gtopo_get, doc=r"""gtopo : mfem::GroupTopology""")
    have_face_nbr_data = property(_pmesh.ParMesh_have_face_nbr_data_get, _pmesh.ParMesh_have_face_nbr_data_set, doc=r"""have_face_nbr_data : bool""")
    face_nbr_group = property(_pmesh.ParMesh_face_nbr_group_get, _pmesh.ParMesh_face_nbr_group_set, doc=r"""face_nbr_group : mfem::Array<(int)>""")
    face_nbr_elements_offset = property(_pmesh.ParMesh_face_nbr_elements_offset_get, _pmesh.ParMesh_face_nbr_elements_offset_set, doc=r"""face_nbr_elements_offset : mfem::Array<(int)>""")
    face_nbr_vertices_offset = property(_pmesh.ParMesh_face_nbr_vertices_offset_get, _pmesh.ParMesh_face_nbr_vertices_offset_set, doc=r"""face_nbr_vertices_offset : mfem::Array<(int)>""")
    face_nbr_elements = property(_pmesh.ParMesh_face_nbr_elements_get, doc=r"""face_nbr_elements : mfem::Array<(p.mfem::Element)>""")
    face_nbr_vertices = property(_pmesh.ParMesh_face_nbr_vertices_get, doc=r"""face_nbr_vertices : mfem::Array<(mfem::Vertex)>""")
    send_face_nbr_elements = property(_pmesh.ParMesh_send_face_nbr_elements_get, _pmesh.ParMesh_send_face_nbr_elements_set, doc=r"""send_face_nbr_elements : mfem::Table""")
    send_face_nbr_vertices = property(_pmesh.ParMesh_send_face_nbr_vertices_get, _pmesh.ParMesh_send_face_nbr_vertices_set, doc=r"""send_face_nbr_vertices : mfem::Table""")
    pncmesh = property(_pmesh.ParMesh_pncmesh_get, _pmesh.ParMesh_pncmesh_set, doc=r"""pncmesh : p.mfem::ParNCMesh""")

    def GetNGroups(self):
        r"""GetNGroups(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNGroups(self)

    def GroupNVertices(self, group):
        r"""GroupNVertices(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNVertices(self, group)

    def GroupNEdges(self, group):
        r"""GroupNEdges(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNEdges(self, group)

    def GroupNTriangles(self, group):
        r"""GroupNTriangles(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNTriangles(self, group)

    def GroupNQuadrilaterals(self, group):
        r"""GroupNQuadrilaterals(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNQuadrilaterals(self, group)

    def GroupVertex(self, group, i):
        r"""GroupVertex(ParMesh self, int group, int i) -> int"""
        return _pmesh.ParMesh_GroupVertex(self, group, i)

    def GroupEdge(self, group, i, *args):
        if len(args) == 0:
            from mfem.par import intp  
            edge = intp()
            o = intp()  
            _pmesh.ParMesh_GroupEdge(self, group, i, edge, o)
            return edge.value(), o.value()
        else:
            return _pmesh.ParMesh_GroupEdge(self, group, i, *args)      



    def GroupTriangle(self, group, i, face, o):
        r"""GroupTriangle(ParMesh self, int group, int i, int & face, int & o)"""
        return _pmesh.ParMesh_GroupTriangle(self, group, i, face, o)

    def GroupQuadrilateral(self, group, i, face, o):
        r"""GroupQuadrilateral(ParMesh self, int group, int i, int & face, int & o)"""
        return _pmesh.ParMesh_GroupQuadrilateral(self, group, i, face, o)

    def GenerateOffsets(self, N, loc_sizes, offsets):
        r"""GenerateOffsets(ParMesh self, int N, HYPRE_Int [] loc_sizes, mfem::Array< HYPRE_Int > *[] offsets)"""
        return _pmesh.ParMesh_GenerateOffsets(self, N, loc_sizes, offsets)

    def ExchangeFaceNbrData(self):
        r"""ExchangeFaceNbrData(ParMesh self)"""
        return _pmesh.ParMesh_ExchangeFaceNbrData(self)

    def ExchangeFaceNbrNodes(self):
        r"""ExchangeFaceNbrNodes(ParMesh self)"""
        return _pmesh.ParMesh_ExchangeFaceNbrNodes(self)

    def GetNFaceNeighbors(self):
        r"""GetNFaceNeighbors(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNFaceNeighbors(self)

    def GetFaceNbrGroup(self, fn):
        r"""GetFaceNbrGroup(ParMesh self, int fn) -> int"""
        return _pmesh.ParMesh_GetFaceNbrGroup(self, fn)

    def GetFaceNbrRank(self, fn):
        r"""GetFaceNbrRank(ParMesh self, int fn) -> int"""
        return _pmesh.ParMesh_GetFaceNbrRank(self, fn)

    def GetFaceToAllElementTable(self):
        r"""GetFaceToAllElementTable(ParMesh self) -> Table"""
        return _pmesh.ParMesh_GetFaceToAllElementTable(self)

    def GetSharedFaceTransformations(self, sf, fill2=True):
        r"""GetSharedFaceTransformations(ParMesh self, int sf, bool fill2=True) -> FaceElementTransformations"""
        return _pmesh.ParMesh_GetSharedFaceTransformations(self, sf, fill2)

    def GetNSharedFaces(self):
        r"""GetNSharedFaces(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNSharedFaces(self)

    def GetSharedFace(self, sface):
        r"""GetSharedFace(ParMesh self, int sface) -> int"""
        return _pmesh.ParMesh_GetSharedFace(self, sface)

    def ReorientTetMesh(self):
        r"""ReorientTetMesh(ParMesh self)"""
        return _pmesh.ParMesh_ReorientTetMesh(self)

    def ReduceInt(self, value):
        r"""ReduceInt(ParMesh self, int value) -> long"""
        return _pmesh.ParMesh_ReduceInt(self, value)

    def Rebalance(self):
        r"""Rebalance(ParMesh self)"""
        return _pmesh.ParMesh_Rebalance(self)

    def GetBoundingBox(self, ref = 2):
        from  .vector import Vector
        min = Vector()
        max = Vector()      
        _mesh.Mesh_GetBoundingBox(self, min, max, ref)      
        return min.GetDataArray().copy(), max.GetDataArray().copy()



    def GetCharacteristics(self, h_min, h_max, kappa_min, kappa_max):
        r"""GetCharacteristics(ParMesh self, double & h_min, double & h_max, double & kappa_min, double & kappa_max)"""
        return _pmesh.ParMesh_GetCharacteristics(self, h_min, h_max, kappa_min, kappa_max)

    def FindPoints(self, point_mat, elem_ids, ips, warn=True, inv_trans=None):
        r"""FindPoints(ParMesh self, DenseMatrix point_mat, intArray elem_ids, IntegrationPointArray ips, bool warn=True, InverseElementTransformation inv_trans=None) -> int"""
        return _pmesh.ParMesh_FindPoints(self, point_mat, elem_ids, ips, warn, inv_trans)

    def PrintSharedEntities(self, fname_prefix):
        r"""PrintSharedEntities(ParMesh self, char const * fname_prefix)"""
        return _pmesh.ParMesh_PrintSharedEntities(self, fname_prefix)
    __swig_destroy__ = _pmesh.delete_ParMesh

    def __init__(self, *args):
        r"""
        __init__(ParMesh self, ParMesh pmesh, bool copy_nodes=True) -> ParMesh
        __init__(ParMesh self, MPI_Comm comm, Mesh mesh, int * partitioning_=None, int part_method=1) -> ParMesh
        __init__(ParMesh self, MPI_Comm comm, std::istream & input, bool refine=True) -> ParMesh
        __init__(ParMesh self, ParMesh orig_mesh, int ref_factor, int ref_type) -> ParMesh
        __init__(ParMesh self, MPI_Comm comm, char const * mesh_file) -> ParMesh
        """
        _pmesh.ParMesh_swiginit(self, _pmesh.new_ParMesh(*args))

    def ParPrintToFile(self, mesh_file, precision):
        r"""ParPrintToFile(ParMesh self, char const * mesh_file, int const precision)"""
        return _pmesh.ParMesh_ParPrintToFile(self, mesh_file, precision)

    def Print(self, *args):
        r"""
        Print(ParMesh self, std::ostream & out=mfem::out)
        Print(ParMesh self, char const * file, int precision=8)
        """
        return _pmesh.ParMesh_Print(self, *args)

    def PrintXG(self, *args):
        r"""
        PrintXG(ParMesh self, std::ostream & out=mfem::out)
        PrintXG(ParMesh self, char const * file, int precision=8)
        """
        return _pmesh.ParMesh_PrintXG(self, *args)

    def PrintAsOne(self, *args):
        r"""
        PrintAsOne(ParMesh self, std::ostream & out=mfem::out)
        PrintAsOne(ParMesh self, char const * file, int precision=8)
        """
        return _pmesh.ParMesh_PrintAsOne(self, *args)

    def PrintAsOneXG(self, *args):
        r"""
        PrintAsOneXG(ParMesh self, std::ostream & out=mfem::out)
        PrintAsOneXG(ParMesh self, char const * file, int precision=8)
        """
        return _pmesh.ParMesh_PrintAsOneXG(self, *args)

    def PrintInfo(self, *args):
        r"""
        PrintInfo(ParMesh self, std::ostream & out=mfem::out)
        PrintInfo(ParMesh self, char const * file, int precision=8)
        """
        return _pmesh.ParMesh_PrintInfo(self, *args)

    def ParPrint(self, *args):
        r"""
        ParPrint(ParMesh self, std::ostream & out)
        ParPrint(ParMesh self, char const * file, int precision=8)
        ParPrint(ParMesh self)
        """
        return _pmesh.ParMesh_ParPrint(self, *args)

# Register ParMesh in _pmesh:
_pmesh.ParMesh_swigregister(ParMesh)


