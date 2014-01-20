# -*- coding: utf-8 -*-

from ctypes import *

VstIntPtr = POINTER(c_int)

class VstAEffectFlags(object):
  effFlagsHasEditor     = 1 << 0
  effFlagsCanReplacing  = 1 << 4
  effFlagsProgramChunks = 1 << 5
  effFlagsIsSynth       = 1 << 8
  effFlagsNoSoundInStop = 1 << 9
  effFlagsCanDoubleReplacing = 1 << 12

class AEffectOpcodes(object):
  effOpen = 0
  effClose = 1
  effSetProgram = 2
  effGetProgram = 3
  effSetProgramName = 4
  effGetProgramName = 5
  effGetParamLabel = 6
  effGetParamDisplay = 7
  effGetParamName = 8
  effSetSampleRate = 10
  effSetBlockSize = 11
  effMainsChanged = 12
  effEditGetRect = 13
  effEditOpen = 14
  effEditClose = 15
  effEditIdle = 19
  effGetChunk = 23
  effSetChunk = 24
  effNumOpcodes = 25

class AudioMasterOpcodes(object):
  audioMasterAutomate = 0
  audioMasterVersion = 1
  audioMasterCurrentId = 2
  audioMasterIdle = 3
  audioMasterPinConnected = 4 # deprecated

class VstStringConstants(object):
  kVstMaxProgNameLen = 24
  kVstMaxParamStrLen = 8
  kVstMaxVendorStrLen = 64
  kVstMaxProductStrLen = 64
  kVstMaxEffectNameLen = 32
  kVstExtMaxParamStrLen = 32

class AEffect(Structure):
  _fields_ = [
    ('magic', c_int),
    ('dispatcher', c_void_p),
    ('process', c_void_p),
    ('setParameter', c_void_p),
    ('getParameter', c_void_p),
    ('numPrograms', c_int),
    ('numParams', c_int),
    ('numInputs', c_int),
    ('numOutputs', c_int),
    ('flags', c_int),
    ('resvd1', c_void_p),
    ('resvd2', c_void_p),
    ('initialDelay', c_int),
    ('realQualities', c_int),
    ('offQualities', c_int),
    ('ioRatio', c_float),
    ('object', c_void_p),
    ('user', c_void_p),
    ('uniqueID', c_int),
    ('version', c_int),
    ('processReplacing', c_void_p),
    ('processDoubleReplacing', c_void_p),
  ]

class ERect(Structure):
  _fields_ = [
    ('top', c_short),
    ('left', c_short),
    ('bottom', c_short),
    ('right', c_short),
 ]

audiomaster_callback = CFUNCTYPE(c_void_p, POINTER(AEffect), c_int, c_int, c_long, c_void_p, c_float)

def create_dispatcher_proc(pointer):
  prototype = CFUNCTYPE(c_void_p, POINTER(AEffect), c_int, c_int, c_long, c_void_p, c_float)
  return prototype(pointer)

def create_process_proc(pointer):
  prototype = CFUNCTYPE(None, POINTER(AEffect), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), c_int)
  return prototype(pointer)

def create_process_double_proc(pointer):
  prototype = CFUNCTYPE(None, POINTER(AEffect), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int)
  return prototype(pointer)

def create_set_param_proc(pointer):
  prototype = CFUNCTYPE(None, POINTER(AEffect), c_int, c_float)
  return prototype(pointer)

def create_get_param_proc(pointer):
  prototype = CFUNCTYPE(c_float, POINTER(AEffect), c_int)
  return prototype(pointer)
