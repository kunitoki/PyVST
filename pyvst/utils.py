import wave
import numpy
import struct
import cStringIO
import matplotlib.pyplot as pyplot


#===============================================================================
def save_wav_file(name, data, sample_rate):
    # For storing packed string
    def pack(data):
        sio = cStringIO.StringIO()
        for d in data:
            sio.write(struct.pack('h',d))
        return sio.getvalue()

    # open wave
    w = wave.open(name, 'wb')
    w.setnchannels(data.ndim)
    w.setsampwidth(2)
    w.setframerate(sample_rate)

    # might want to make this more efficient later
    if data.ndim == 2:
        outputs = numpy.zeros((data.ndim, len(data[0])), dtype=numpy.int16)
        for x in xrange(len(data[0])):
            outputs[0][x] = int(data[0][x] * 32767)
            outputs[1][x] = int(data[1][x] * 32767)
        data = numpy.array(zip(outputs[0], outputs[1]), dtype=numpy.int16).flat
        w.setnframes(len(data) / 2)
    else:
        w.setnframes(len(data))

    w.writeframesraw(pack(data))
    w.close()


#===============================================================================
def plot(inputs, outputs, SampleRate=44100, NFFT=8192, noverlap=1024):
    pyplot.figure()

    if len(inputs) > 0:
        a = pyplot.subplot(2, len(inputs), 1)
        pyplot.title("Input L")
        pyplot.specgram(inputs[0], NFFT = NFFT, Fs = SampleRate, noverlap = noverlap )
        #pyplot.plot(inputs[0])

    if len(inputs) > 1:
        a = pyplot.subplot(2, 2, 2)
        pyplot.title("Input R")
        pyplot.specgram(inputs[1], NFFT = NFFT, Fs = SampleRate, noverlap = noverlap )
        #pyplot.plot(inputs[1])

    if len(outputs) > 0:
        a = pyplot.subplot(2, len(outputs), len(outputs) + 1)
        pyplot.title("Output L")
        pyplot.specgram(outputs[0], NFFT = NFFT, Fs = SampleRate, noverlap = noverlap )
        #pyplot.plot(outputs[0])

    if len(outputs) > 1:
        a = pyplot.subplot(2, 2, 4)
        pyplot.title("Output R")
        pyplot.specgram(outputs[1], NFFT = NFFT, Fs = SampleRate, noverlap = noverlap )
        #pyplot.plot(outputs[1])

    return pyplot

