from setuptools import setup, find_packages

setup(
    name="termyUI",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'windows-curses==2.3.3',
        'pyfiglet==1.0.2',
        'termcolor==1.0.2',
        're',
        'term-image==0.7.2'
    ],
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),

)