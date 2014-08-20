import os
import sys
import time
import matplotlib.pyplot as pyplot
import numpy

from utils import get_platform_plugin
import pyvst


#===============================================================================
sample_rate = 44100
block_size = 2048
max_samples = sample_rate  * 5 # approx 5 seconds
freq_max = 20000


#===============================================================================
def process(plugin, type):
    t = numpy.arange(max_samples, dtype=type) / sample_rate

    input1 = numpy.sin(numpy.pi * (sample_rate * freq_max / max_samples * (t + .1)) * t)
    input2 = input1[::-1].flatten()
    inputs = numpy.array([input1, input2])
    outputs = numpy.zeros((plugin.number_of_outputs, max_samples), dtype=type)

    start = time.time()
    for i in range(max_samples/block_size):
        plugin.process_replacing(inputs[:, i*block_size:(i+1)*block_size],
                                 outputs[:, i*block_size:(i+1)*block_size],
                                 block_size)
    print "Elapsed time:", (time.time() - start)

    #pyvst.save_wav_file("display_input.wav", inputs, sample_rate)
    #pyvst.save_wav_file("display_output.wav", outputs, sample_rate)

    return (input1, input2), outputs


#===============================================================================
if __name__ == "__main__":
    if len(sys.argv) > 1:
        plugin = pyvst.VSTPlugin(sys.argv[1])
    else:
        plugin = pyvst.VSTPlugin(get_platform_plugin("mda Delay"))

    plugin.open()
    plugin.set_sample_rate(sample_rate)
    plugin.set_block_size(block_size)
    plugin.resume()

    plugin.dump_properties()

    if plugin.has_editor():
        plugin.open_gui()

    if plugin.can_process_double():
        print "Testing with doubles (64bits)"
        inputs, outputs = process(plugin, numpy.float64)
    else:
        print "Testing with floats (32bits)"
        inputs, outputs = process(plugin, numpy.float32)
    pyvst.plot(inputs, outputs, sample_rate)
    pyplot.show()

    plugin.suspend()
    plugin.close()
