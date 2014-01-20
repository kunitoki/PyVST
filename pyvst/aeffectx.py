# -*- coding: utf-8 -*-

from ctypes import *

class Vst2StringConstants(object):
  kVstMaxNameLen = 64
  kVstMaxLabelLen = 64
  kVstMaxShortLabelLen = 8
  kVstMaxCategLabelLen = 24
  kVstMaxFileNameLen = 100

class VstEventTypes(object):
  kVstMidiType = 1
  kVstAudioType = 2 # deprecated
  kVstVideoType = 3 # deprecated
  kVstParameterType = 4 # deprecated
  kVstTriggerType = 5 # deprecated
  kVstSysExType = 6

class VstMidiEventFlags(object):
  kVstMidiEventIsRealtime = 1 << 0

class VstTimeInfoFlags(object):
  kVstTransportChanged = 1
  kVstTransportPlaying = 1 << 1
  kVstTransportCycleActive = 1 << 2
  kVstTransportRecording = 1 << 3
  kVstAutomationWriting = 1 << 6
  kVstAutomationReading = 1 << 7
  kVstNanosValid = 1 << 8
  kVstPpqPosValid = 1 << 9
  kVstTempoValid = 1 << 10
  kVstBarsValid = 1 << 11
  kVstCyclePosValid = 1 << 12
  kVstTimeSigValid = 1 << 13
  kVstSmpteValid = 1 << 14
  kVstClockValid = 1 << 15

class VstSmpteFrameRate(object):
  kVstSmpte24fps = 0
  kVstSmpte25fps = 1
  kVstSmpte2997fps = 2
  kVstSmpte30fps = 3
  kVstSmpte2997dfps = 4
  kVstSmpte30dfps = 5
  kVstSmpteFilm16mm = 6
  kVstSmpteFilm35mm = 7
  kVstSmpte239fps = 10
  kVstSmpte249fps = 11
  kVstSmpte599fps = 12
  kVstSmpte60fps = 13

class VstHostLanguage(object):
  kVstLangEnglish = 1
  kVstLangGerman = 2
  kVstLangFrench = 3
  kVstLangItalian = 4
  kVstLangSpanish = 5
  kVstLangJapanese = 6

class AEffectXOpcodes(object):
  effProcessEvents = 25
  effCanBeAutomated = 26
  effString2Parameter = 27

  effGetProgramNameIndexed = 29

  effGetInputProperties = 33
  effGetOutputProperties = 34
  effGetPlugCategory = 35

  effOfflineNotify = 38
  effOfflinePrepare = 39
  effOfflineRun = 40
  effProcessVarIo = 41
  effSetSpeakerArrangement = 42

  effSetBypass = 44
  effGetEffectName = 45

  effGetVendorString = 47
  effGetProductString = 48
  effGetVendorVersion = 49
  effVendorSpecific = 50
  effCanDo = 51
  effGetTailSize = 52

  effGetParameterProperties = 56

  effGetVstVersion = 58
  effEditKeyDown = 59
  effEditKeyUp = 60
  effSetEditKnobMode = 61
  effGetMidiProgramName = 62
  effGetCurrentMidiProgram = 63
  effGetMidiProgramCategory = 64
  effHasMidiProgramsChanged = 65
  effGetMidiKeyName = 66
  effBeginSetProgram = 67
  effEndSetProgram = 68
  effGetSpeakerArrangement = 69
  effShellGetNextPlugin = 70
  effStartProcess = 71
  effStopProcess = 72
  effSetTotalSampleToProcess = 73
  effSetPanLaw = 74
  effBeginLoadBank = 75
  effBeginLoadProgram = 76
  effSetProcessPrecision = 77
  effGetNumMidiInputChannels = 78
  effGetNumMidiOutputChannels = 79

class AudioMasterOpcodesX(object):
  audioMasterWantMidi = 6
  audioMasterGetTime = 7
  audioMasterProcessEvents = 8
  audioMasterSetTime = 9 # deprecated
  audioMasterTempoAt = 10 # deprecated
  audioMasterGetNumAutomatableParameters = 11 # deprecated
  audioMasterGetParameterQuantization = 12 # deprecated
  audioMasterIOChanged = 13
  audioMasterNeedIdle = 14 # deprecated
  audioMasterSizeWindow = 15
  audioMasterGetSampleRate = 16
  audioMasterGetBlockSize = 17
  audioMasterGetInputLatency = 18
  audioMasterGetOutputLatency = 19
  audioMasterGetPreviousPlug = 20 # deprecated
  audioMasterGetNextPlug = 21 # deprecated
  audioMasterWillReplaceOrAccumulate = 22 # deprecated
  audioMasterGetCurrentProcessLevel = 23
  audioMasterGetAutomationState = 24
  audioMasterOfflineStart = 25
  audioMasterOfflineRead = 26
  audioMasterOfflineWrite = 27
  audioMasterOfflineGetCurrentPass = 28
  audioMasterOfflineGetCurrentMetaPass = 29
  audioMasterSetOutputSampleRate = 30 # deprecated
  audioMasterGetOutputSpeakerArrangement = 31 # deprecated
  audioMasterGetVendorString = 32
  audioMasterGetProductString = 33
  audioMasterGetVendorVersion = 34
  audioMasterVendorSpecific = 35
  audioMasterSetIcon = 36 # deprecated
  audioMasterCanDo = 37
  audioMasterGetLanguage = 38
  audioMasterOpenWindow = 39 # deprecated
  audioMasterCloseWindow = 40 # deprecated
  audioMasterGetDirectory = 41
  audioMasterUpdateDisplay = 42
  audioMasterBeginEdit = 43
  audioMasterEndEdit = 44
  audioMasterOpenFileSelector = 45
  audioMasterCloseFileSelector = 46  
  audioMasterEditFile = 47 # deprecated
  audioMasterGetChunkFile = 48 # deprecated
  audioMasterGetInputSpeakerArrangement = 49 # deprecated

class VstEvent(Structure):
    _fields_ = [
        ('type', c_int),
        ('byteSize', c_int),
        ('deltaFrames', c_int),
        ('flags', c_char * 16),
    ]

class VstMidiEvent(Structure):
    _fields_ = [
        ('type', c_int),
        ('byteSize', c_int),
        ('deltaFrames', c_int),
        ('flags', c_int),
        ('noteLength', c_int),
        ('noteOffset', c_int),
        ('midiData', c_char * 4),
        ('detune', c_char),
        ('noteOffVelocity', c_char),
        ('reserved1', c_char),
        ('reserved2', c_char),
    ]

class VstMidiSysexEvent(Structure):
    _fields_ = [
        ('type', c_int),
        ('byteSize', c_int),
        ('deltaFrames', c_int),
        ('flags', c_int),
        ('dumpBytes', c_int),
        ('resvd1', POINTER(c_int)),
        ('sysexDump', c_char_p),
        ('resvd2', POINTER(c_int)),
    ]

class VstEvents(Structure):
    _fields_ = [
        ('numEvents', c_int),
        ('reserved', POINTER(c_int)),
        ('events', POINTER(VstEvent)),
        ('events_', POINTER(VstEvent)),
    ]

class VstTimeInfo(Structure):
    _fields_ = [
        ('samplePos', c_double),
        ('sampleRate', c_double),
        ('nanoSeconds', c_double),
        ('ppqPos', c_double),
        ('tempo', c_double),
        ('barStartPos', c_double),
        ('cycleStartPos', c_double),
        ('cycleEndPos', c_double),
        ('timeSigNumerator', c_int),
        ('timeSigDenominator', c_int),
        ('smpteOffset', c_int),
        ('smpteFrameRate', c_int),
        ('samplesToNextClock', c_int),
        ('flags', c_int),
    ]

class VstVariableIo(Structure):
    _fields_ = [
        ('inputs', POINTER(POINTER(c_float))),
        ('outputs', POINTER(POINTER(c_float))),
        ('numSamplesInput', c_int),
        ('numSamplesOutput', c_int),
        ('numSamplesInputProcessed', POINTER(c_int)),
        ('numSamplesOutputProcessed', POINTER(c_int)),
    ]

VstEventsPtr = POINTER(VstEvent)
VstMidiEventsPtr = POINTER(VstMidiEvent)

def create_process_events_proc(pointer):
  prototype = CFUNCTYPE(None, POINTER(AEffect), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), c_int)
  return prototype(pointer)
