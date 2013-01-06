#!/usr/bin/env python

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('io', parent_package, top_path,
                           setup_name = 'setupscons.py')

    config.add_sconscript('SConstruct')

    config.add_data_dir('tests')
    config.add_subpackage('matlab')
    config.add_subpackage('arff')
    config.add_subpackage('harwell_boeing')
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
