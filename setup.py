from setuptools import setup

setup(
    name='pypardiso',
    version="0.3.3",
    packages=['pypardiso'],
    install_requires=['mkl-service', 'numpy', 'scipy', 'psutil'],
    author="Adrian Haas",
    license=open('LICENSE.txt').read(),
    url="https://github.com/haasad/PyPardisoProject",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    description='Python interface to the Intel MKL Pardiso library to solve large sparse linear systems of equations',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
