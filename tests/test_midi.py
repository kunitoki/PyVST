import os
import sys
import struct
import numpy

#===============================================================================
ROOT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(ROOT_PATH)
import pyvst


#==============================================================================
def generate_wave(plugin, filename, duration_samples, sample_rate, block_size):
    # create buffers
    #input1 = numpy.zeros(numpy.sin(numpy.pi * (sample_rate * FreqMax / Samples * (t + .1)) * t)
    #input2 = input1[::-1].flatten()
    inputs = numpy.zeros((plugin.number_of_inputs, duration_samples), dtype=numpy.float32)
    outputs = numpy.zeros((plugin.number_of_outputs, duration_samples), dtype=numpy.float32)

    # events
    events = [
        (0x90, 0x3C, 0x7F, 0),
        (0x80, 0x3C, 0x00, sample_rate * 2),
    ]

    for i in xrange(duration_samples / block_size):
        events = plugin.process_note_events(events, block_size)
        plugin.process_replacing(inputs[:,i*block_size:(i+1)*block_size],
                                 outputs[:,i*block_size:(i+1)*block_size],
                                 block_size)
    
    pyvst.save_wav_file(filename, outputs, sample_rate)


#==============================================================================
if __name__ == '__main__':
    if len(sys.argv) > 1:
        plugin = pyvst.VSTPlugin(sys.argv[1])
    else:
        pluginpath = os.path.join(ROOT_PATH, "bin", "linux64", "mda DX10.so")
        plugin = pyvst.VSTPlugin(pluginpath)

    plugin.open()
    plugin.dump_properties(True, False)

    #if plugin.has_editor():
    #    plugin.open_gui()

    if plugin.is_synth() or plugin.can_receive_events():
        block_size = 2048
        sample_rate = 44100
        duration_seconds = 5
        duration_samples = duration_seconds * sample_rate

        # processing plugin
        plugin.set_sample_rate(sample_rate)
        plugin.set_block_size(block_size)
        plugin.resume()

        # generate default wave
        generate_wave(plugin, 'test_midi.wav', duration_samples, sample_rate, block_size)

        # save chunk
        #data = plugin.get_chunk()
        #if len(data) > 0:
        #    f = open("example.chunk", "wb")
        #    for d in data:
        #        f.write(d)
        #    f.close()

        # generate different wave
        #plugin.set_parameter(14, 0.90)
        #plugin.set_parameter(19, 0.75)
        #plugin.set_parameter(20, 1.00)
        #generate_wave(plugin, 'example_2.wav', duration_samples, sample_rate, block_size)

        # restore the sound saved
        #f = open("example.chunk", "rb")
        #data = f.read()
        #plugin.set_chunk(data)
        #f.close()

        #generate_wave(plugin, 'example_3.wav', duration_samples, sample_rate, block_size)

        # generate a sound for each preset
        #for p in xrange(plugin.number_of_programs):
        #    plugin.set_program(p)
        #    generate_wave(plugin, 'example_%d.wav' % p, duration_samples, sample_rate, block_size)

        # show plot spectrum data 
        #p = pyvst.plot([], outputs, sample_rate)
        #p.show()

        plugin.suspend()

    plugin.close()
