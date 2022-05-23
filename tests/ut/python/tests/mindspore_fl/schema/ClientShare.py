# automatically generated by the FlatBuffers compiler, do not modify

# namespace: schema

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ClientShare(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ClientShare()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsClientShare(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ClientShare
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ClientShare
    def FlId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ClientShare
    def Share(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # ClientShare
    def ShareAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # ClientShare
    def ShareLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ClientShare
    def ShareIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # ClientShare
    def Index(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(3)
def ClientShareStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddFlId(builder, flId): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(flId), 0)
def ClientShareAddFlId(builder, flId):
    """This method is deprecated. Please switch to AddFlId."""
    return AddFlId(builder, flId)
def AddShare(builder, share): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(share), 0)
def ClientShareAddShare(builder, share):
    """This method is deprecated. Please switch to AddShare."""
    return AddShare(builder, share)
def StartShareVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def ClientShareStartShareVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartShareVector(builder, numElems)
def AddIndex(builder, index): builder.PrependInt32Slot(2, index, 0)
def ClientShareAddIndex(builder, index):
    """This method is deprecated. Please switch to AddIndex."""
    return AddIndex(builder, index)
def End(builder): return builder.EndObject()
def ClientShareEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)