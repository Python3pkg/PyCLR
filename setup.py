from setuptools import setup, find_packages

setup(
    name='pyclr',
    version='0.0.5',
    description='Easy colors in your terminal.',
    long_description='Easy colors in your terminal.',

    url='https://github.com/ScottehMax/PyCLR',

    author='Scott Maxwell',
    author_email='scott@scotteh.me',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='development',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

) 
