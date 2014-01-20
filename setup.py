#!/usr/bin/env python

from setuptools import setup

setup(name='pyvst',
      version='0.2.0',
      description='Python ctypes-based VST wrapper',
      author='Matthieu Brucher, Lucio Asnaghi',
      author_email='matthieu.brucher@gmail.com, kunitoki@gmail.com',
      packages=['pyvst', ],
      classifiers =
            [ 'Development Status :: 4 - Beta',
              'Environment :: Win32 (MS Windows)',
              'Environment :: Plugins',
              'Intended Audience :: Developers',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: GNU General Public License (GPL)',
              'Operating System :: Microsoft :: Windows',
              'Topic :: Multimedia :: Sound/Audio',
              'Topic :: Scientific/Engineering',
            ]
      )

