import re

from setuptools import setup


def read_version(path_to_py_module):
    with open(path_to_py_module) as py_module:
        match = re.search('__version__ = \'([\d.]+)\'', py_module.read())
        if match:
            return match.group(1)
        raise RuntimeError('Can not find the package version in {}'.format(path_to_py_module))


setup(
    name='tubular-pyspark',
    version=read_version('pyspark/__init__.py'),
    packages=[
        'pyspark',
        'pyspark.mllib',
        'pyspark.mllib.linalg',
        'pyspark.mllib.stat',
        'pyspark.ml',
        'pyspark.ml.linalg',
        'pyspark.ml.param',
        'pyspark.sql',
        'pyspark.streaming',
    ],
    install_requires=[
        'py4j==0.10.3',
    ],
    extras_require={
        'ml': ['numpy>=1.7'],
        'mllib': ['numpy>=1.7'],
        'sql': ['pandas'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: Apache Software License',
    ],
    description='Apache Spark Python API',
    keywords='spark pyspark',
    author='Spark Developers',
    author_email='dev@spark.apache.org',
    url='https://github.com/apache/spark/tree/master/python',
    license='http://www.apache.org/licenses/LICENSE-2.0',
)
