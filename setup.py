import os
from setuptools import setup, find_packages

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

execfile(os.path.join(ROOT_PATH, 'neb/version.py'))
long_description = open(os.path.join(ROOT_PATH, 'README.md')).read()

classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development',
]

setup(name='neb',
      version=__version__,
      description='Trinity API Library',
      long_description=long_description,
      author='Christopher Peplin',
      author_email='peplin@bueda.com',
      license='MIT',
      classifiers=classifiers,
      url='http://github.com/bueda/neb',
      packages=find_packages(),
      install_requires=['restkit>=2.1.1']
)
