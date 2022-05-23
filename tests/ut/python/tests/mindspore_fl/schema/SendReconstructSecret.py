# automatically generated by the FlatBuffers compiler, do not modify

# namespace: schema

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SendReconstructSecret(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SendReconstructSecret()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSendReconstructSecret(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # SendReconstructSecret
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SendReconstructSecret
    def FlId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # SendReconstructSecret
    def ReconstructSecretShares(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from mindspore_fl.schema.ClientShare import ClientShare
            obj = ClientShare()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SendReconstructSecret
    def ReconstructSecretSharesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SendReconstructSecret
    def ReconstructSecretSharesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # SendReconstructSecret
    def Iteration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SendReconstructSecret
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # SendReconstructSecret
    def Signature(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # SendReconstructSecret
    def SignatureAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # SendReconstructSecret
    def SignatureLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SendReconstructSecret
    def SignatureIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def Start(builder): builder.StartObject(5)
def SendReconstructSecretStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddFlId(builder, flId): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(flId), 0)
def SendReconstructSecretAddFlId(builder, flId):
    """This method is deprecated. Please switch to AddFlId."""
    return AddFlId(builder, flId)
def AddReconstructSecretShares(builder, reconstructSecretShares): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(reconstructSecretShares), 0)
def SendReconstructSecretAddReconstructSecretShares(builder, reconstructSecretShares):
    """This method is deprecated. Please switch to AddReconstructSecretShares."""
    return AddReconstructSecretShares(builder, reconstructSecretShares)
def StartReconstructSecretSharesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SendReconstructSecretStartReconstructSecretSharesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartReconstructSecretSharesVector(builder, numElems)
def AddIteration(builder, iteration): builder.PrependInt32Slot(2, iteration, 0)
def SendReconstructSecretAddIteration(builder, iteration):
    """This method is deprecated. Please switch to AddIteration."""
    return AddIteration(builder, iteration)
def AddTimestamp(builder, timestamp): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(timestamp), 0)
def SendReconstructSecretAddTimestamp(builder, timestamp):
    """This method is deprecated. Please switch to AddTimestamp."""
    return AddTimestamp(builder, timestamp)
def AddSignature(builder, signature): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(signature), 0)
def SendReconstructSecretAddSignature(builder, signature):
    """This method is deprecated. Please switch to AddSignature."""
    return AddSignature(builder, signature)
def StartSignatureVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def SendReconstructSecretStartSignatureVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSignatureVector(builder, numElems)
def End(builder): return builder.EndObject()
def SendReconstructSecretEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)