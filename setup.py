# Authors: Harshvardhan Singh
# License: GNU General Public License v3.0

from distutils.core import setup

# Taken from scikit-learn setup.py
DISTNAME = 'digicomm-project'
DESCRIPTION = 'Relay misbehaviour detection, theoretical analysis'
LONG_DESCRIPTION = open('README.md').read()
MAINTAINER = 'Harshvardhan Singh'
MAINTAINER_EMAIL = 'hs504@snu.edu.in'
URL = 'https://github.com/harshvs99/DigiCommProject/'
LICENSE = 'GNU General Public License v3.0'
VERSION = '0.1.0'

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["channelcoding/*, channelcoding/tests/*, tests/*"]

setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found
    #recursively.)
    packages=['main', 'main.relay_detect'],
    install_requires=[
          'numpy',
          'scipy',
          'matplotlib',
    ],
    #'package' package must contain files (see list above)
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data={'commpy': files},
    #'runner' is in the root.
    scripts=["runner"],
    test_suite='nose.collector',
    tests_require=['nose'],

    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    python_requires='>=3.2',
)