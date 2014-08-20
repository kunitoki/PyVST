import os
import sys
from ctypes import *

from utils import get_platform_plugin
import pyvst


#===============================================================================
def test_load(pluginpath):
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.dump_properties()

def test_check_magic(pluginpath):
    plugin = pyvst.VSTPlugin(pluginpath)
    assert plugin._VSTPlugin__effect.magic == (ord("V") << 24) + (ord("s") << 16) + (ord("t") << 8) + ord("P")

def test_open_close(pluginpath):
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.open()
    plugin.close()
    
def test_properties(pluginpath):
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.open()
    assert plugin.get_name() == "DX10"
    assert plugin.get_vendor() == "mda"
    assert plugin.get_product() == "mda DX10"
    assert plugin.number_of_programs == 32
    assert plugin.number_of_parameters == 16
    assert plugin.number_of_inputs == 0
    assert plugin.number_of_outputs == 2
    assert plugin.latency == 0
    assert plugin.is_synth()
    assert not plugin.has_editor()
    plugin.close()

def test_resume_suspend(pluginpath):
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.open()
    plugin.set_sample_rate(44100)
    plugin.set_block_size(1024)
    plugin.resume()
    plugin.suspend()
    plugin.close()

def test_parameters(pluginpath):
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.set_parameter(1, 0.)
    assert plugin.get_parameter(1) == 0.
    plugin.set_parameter(1, 1.)
    assert plugin.get_parameter(1) == 1.

def test_programs(pluginpath):
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.set_program(10)
    print cast(pointer(plugin.get_program()), POINTER(c_void_p)).contents.value
    print pointer(c_int(10)).contents.value
    assert plugin.get_program() == pointer(c_int(10))
    plugin.set_program(0)
    assert plugin.get_program() == 0


#===============================================================================
if __name__ == "__main__":
    pluginpath = get_platform_plugin("mda DX10")

    test_load(pluginpath)
    test_check_magic(pluginpath)
    test_open_close(pluginpath)
    test_properties(pluginpath)
    test_resume_suspend(pluginpath)
    test_parameters(pluginpath)
    #test_programs(pluginpath)
