import os
import sys

#==============================================================================
this_path = os.path.abspath(os.path.dirname(__file__))
pyvst_path = os.path.split(this_path)[0]
root_path = os.path.split(pyvst_path)[0]
bin_path = os.path.join(root_path, "bin")

sys.path.append(root_path)

#==============================================================================
def get_platform_plugin(plugin_name):
    plat = sys.platform
    arch = "64" if sys.maxsize > 2**32 else "32"
    if plat.startswith('linux'):
        return os.path.join(bin_path, "linux" + arch, plugin_name + ".so")
    elif plat.startswith('win') or plat.startswith('cygwin'):
        return os.path.join(bin_path, "win" + arch, plugin_name + ".dll")
    elif plat.startswith('darwin'):
        return os.path.join(bin_path, "macosx", plugin_name + ".vst")
    raise Exception("Uknown platform !")
