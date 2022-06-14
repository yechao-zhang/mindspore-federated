# automatically generated by the FlatBuffers compiler, do not modify

# namespace: schema

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ReturnShareSecrets(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ReturnShareSecrets()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsReturnShareSecrets(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ReturnShareSecrets
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ReturnShareSecrets
    def Retcode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ReturnShareSecrets
    def Iteration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ReturnShareSecrets
    def EncryptedShares(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from mindspore_fl.schema.ClientShare import ClientShare
            obj = ClientShare()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ReturnShareSecrets
    def EncryptedSharesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ReturnShareSecrets
    def EncryptedSharesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # ReturnShareSecrets
    def NextReqTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(4)
def ReturnShareSecretsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddRetcode(builder, retcode): builder.PrependInt32Slot(0, retcode, 0)
def ReturnShareSecretsAddRetcode(builder, retcode):
    """This method is deprecated. Please switch to AddRetcode."""
    return AddRetcode(builder, retcode)
def AddIteration(builder, iteration): builder.PrependInt32Slot(1, iteration, 0)
def ReturnShareSecretsAddIteration(builder, iteration):
    """This method is deprecated. Please switch to AddIteration."""
    return AddIteration(builder, iteration)
def AddEncryptedShares(builder, encryptedShares): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(encryptedShares), 0)
def ReturnShareSecretsAddEncryptedShares(builder, encryptedShares):
    """This method is deprecated. Please switch to AddEncryptedShares."""
    return AddEncryptedShares(builder, encryptedShares)
def StartEncryptedSharesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ReturnShareSecretsStartEncryptedSharesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartEncryptedSharesVector(builder, numElems)
def AddNextReqTime(builder, nextReqTime): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(nextReqTime), 0)
def ReturnShareSecretsAddNextReqTime(builder, nextReqTime):
    """This method is deprecated. Please switch to AddNextReqTime."""
    return AddNextReqTime(builder, nextReqTime)
def End(builder): return builder.EndObject()
def ReturnShareSecretsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)