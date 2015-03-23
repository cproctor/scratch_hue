#import ez_setup
#ez_setup.use_setuptools() 

from setuptools import setup, find_packages
 
setup(
    name = 'scratch_hue_extension',
    packages = find_packages(),
    # py_modules = ['ez_setup'],
    scripts = ['scratch_hue_helper'],
    install_requires = ['phue', 'flask'],
    package_data = {
        '': ['COPYING.txt', 'LICENSE', 'README.md', 'scratch_hue_extension.s2e', 'setup.cfg']
    },
    version = '0.0.11',
    description = 'Provides a http helper app to allow Scratch 2 to control Philips Hue lights',
    author='Chris Proctor',
    author_email='chris.proctor@gmail.com',
    url='http://mrproctor.net/scratch',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Topic :: Education'
    ]
)
