import os
import sys
import matplotlib.pyplot as pyplot
import numpy

#===============================================================================
ROOT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(ROOT_PATH)
import pyvst


#===============================================================================
SampleRate = 44100
Samples = (2048 * 20)  * 5 # approx 5 seconds


#===============================================================================
def display(plugin, type):
    input1 = numpy.random.randn(Samples).astype(numpy.float32)
    input2 = input1[::-1].flatten()
    output = numpy.zeros((plugin.number_of_outputs, Samples), dtype=type)

    for i in range(Samples/2048):
        plugin.process_replacing([input1[i*2048:(i+1)*2048], input2[i*2048:(i+1)*2048]] * (plugin.number_of_inputs / 2),
                                  output[:, i*2048:(i+1)*2048],
                                  2048)

    return (input1, input2), output


#===============================================================================
def plot(inputs, outputs):
    x= SampleRate * numpy.arange(Samples/2.) / Samples
    pyplot.figure()
    a = pyplot.subplot(2, 2, 1)
    a.grid(True)
    pyplot.title("Input L")
    pyplot.loglog(x, numpy.abs(numpy.fft.fft(inputs[0])[:Samples/2]))
    #pyplot.plot(inputs[0])
    a = pyplot.subplot(2, 2, 2)
    a.grid(True)
    pyplot.title("Input R")
    pyplot.loglog(x, numpy.abs(numpy.fft.fft(inputs[1])[:Samples/2]))
    #pyplot.plot(inputs[1])

    a = pyplot.subplot(2, 2, 3)
    a.grid(True)
    pyplot.title("Output L")
    pyplot.loglog(x, numpy.abs(numpy.fft.fft(outputs[0])[:Samples/2]))
    #pyplot.plot(outputs[0])
    a = pyplot.subplot(2, 2, 4)
    a.grid(True)
    pyplot.title("Output R")
    pyplot.loglog(x, numpy.abs(numpy.fft.fft(outputs[1])[:Samples/2]))
    #pyplot.plot(outputs[1])


#===============================================================================
if __name__ == "__main__":
    if len(sys.argv) > 1:
        plugin = pyvst.VSTPlugin(sys.argv[1])
    else:
        pluginpath = os.path.join(ROOT_PATH, "bin", "linux64", "mda Delay.so")
        plugin = pyvst.VSTPlugin(pluginpath)

    plugin.open()
    plugin.set_sample_rate(SampleRate)
    plugin.set_block_size(2048)
    plugin.resume()

    plugin.dump_properties()

    if plugin.has_editor():
        plugin.open_gui()

    if plugin.can_process_double():
        print "Testing with doubles (64bits)"
        inputs, outputs = display(plugin, numpy.float64)
    else:
        print "Testing with floats (32bits)"
        inputs, outputs = display(plugin, numpy.float32)
    plot(inputs, outputs)
    pyplot.show()

    plugin.suspend()
    plugin.close()
