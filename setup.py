from setuptools import setup
 
setup(
    name = 'scratch_hue_extension',
    packages = ['scratch_hue_extension'],
    version = '0.0.1',
    description = 'Provides a http helper app to allow Scratch 2 to control Philips Hue lights',
    author='Chris Proctor',
    author_email='chris.proctor@gmail.com',
    url='http://mrproctor.net/scratch',
    download_url='https://github.com/cproctor/scratch_hue/tarball/0.1',
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
