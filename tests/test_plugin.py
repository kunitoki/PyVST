import os
import sys

#===============================================================================
ROOT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(ROOT_PATH)
import pyvst

pluginpath = os.path.join(ROOT_PATH, "bin", "linux64", "mda Delay.so")


#===============================================================================
def test_load():
    plugin = pyvst.VSTPlugin(pluginpath)

def test_check_magic():
    plugin = pyvst.VSTPlugin(pluginpath)
    assert plugin._VSTPlugin__effect.magic == (ord("V") << 24) + (ord("s") << 16) + (ord("t") << 8) + ord("P")

def test_basic_info():
    plugin = pyvst.VSTPlugin(pluginpath)
    assert plugin.get_name() == "Delay"
    assert plugin.get_vendor() == "mda"
    assert plugin.get_product() == "mda Delay"

def test_open_close():
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.open()
    plugin.close()

def test_resume_suspend():
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.resume()
    plugin.suspend()

def test_properties():
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.open()

    assert plugin.number_of_programs == 1
    assert plugin.number_of_parameters == 6
    assert plugin.number_of_inputs == 2
    assert plugin.number_of_outputs == 2
    assert plugin.latency == 0
    assert not plugin.is_synth()
    assert not plugin.has_editor()

def test_parameters():
    plugin = pyvst.VSTPlugin(pluginpath)
    plugin.set_parameter(1, 0.)
    assert plugin.get_parameter(1) == 0.
    plugin.set_parameter(1, 1.)
    assert plugin.get_parameter(1) == 1.
