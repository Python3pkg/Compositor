from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Compositor',
    version='1.0.0',
    description='Morphologically Optimal ASCII Art',
    long_description=long_description,
    url='https://github.com/athuras/Compositor',
    author='Alexander Huras',
    author_email='athuras@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
        ]
    keywords='ascii art image processing',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['numpy', 'docopt', 'pillow'],
    package_data={'sample': ['package_data.dat']},
    entry_points={'console_scripts': ['Compositor=Compositor.ui:main']},
)
