from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name = 'sigfig',
    description = ('manipulate and format numerical data for presentation',
                   'through accurately rounding by significant figures,',
                   'number of decimals, or uncertainty')

    version = '1.1.0',
    license = 'MIT',
    url = 'https://pypi.org/project/sigfig/',
    install_requires =['SortedContainers']
    packages = find_packages(exclude = ['doc', 'test']),
    long_description = long_description,
    long_description_content_type = 'text/x-rst',
    author = 'Mike & Travis',
    author_email = 'mike.busuttil@gmail.com, valdezt@gmail.com',

    keywords = ['round', 'rounding', 'significant figures', 'sigfinicant digits',
                'sigfigs', 'sigdigs', 'decimals', 'uncertainty', 'uncertainties',
                'numeric', 'numerical', 'number', 'numbers', 'data',
                'format', 'style',  'publication'],
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: Financial and Insurance Industry',
                   'Intended Audience :: Healthcare Industry',
                   'Intended Audience :: Other Audience',
                   'Intended Audience :: Manufacturing',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.1',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Topic :: Education',
                   'Topic :: Education :: Computer Aided Instruction (CAI)',
                   'Topic :: Office/Business :: Financial',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   'Topic :: Scientific/Engineering :: Mathematics',
                   'Topic :: Scientific/Engineering :: Physics',
                   'Topic :: Software Development',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities']
)
