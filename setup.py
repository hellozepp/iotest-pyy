from setuptools import setup

dependencies = [
    "proto-plus >= 1.22.0, <2.0.0dev",
    "packaging >= 14.3, <24.0.0dev",
    "protobuf>=3.19.5,<5.0.0dev,!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5",
    "python-dateutil >= 2.7.2, <3.0dev",
    "requests >= 2.21.0, < 3.0.0dev",
    "pyarrow >= 10.0.1, <11.0.0",
    "sqlalchemy >= 1.4.0, <2.0.0",
    "cz-ossfs >= 0.0.2",
    "cos-python-sdk-v5 >= 1.9.25",
    "pandas >=1.5.3",
    "s3fs[boto3] == 2023.5.0",
    "boto3 == 1.28.17",
    "google-cloud-storage <= 2.17.0",
    "gcsfs <= 2024.6.0",
    "APScheduler >= 3.10.4",
    "mock",
    "simplejson",
]

setup(
    name='iotest-pyy',
    version='',
    packages=['iotestpy', 'iotestpy.db', 'iotestpy.db2', 'iotestpy.oop', 'iotestpy.oop.test', 'iotestpy.model',
              'iotestpy.model.org', 'iotestpy.pyapi', 'iotestpy.pyapi.logtest2sub', 'iotestpy.fileio',
              'iotestpy.fileio.serialization', 'iotestpy.fileio.serialization.myprotobuf', 'iotestpy.pylang',
              'iotestpy.pylang.pkg', 'iotestpy.pylang.str', 'iotestpy.pysock', 'iotestpy.pysock.tcp',
              'iotestpy.pysock.tcp.nio', 'iotestpy.pysock.udp', 'iotestpy.httpDemo', 'iotestpy.parallel',
              'iotestpy.parallel.thread', 'iotestpy.parallel.process', 'iotestpy.parallel.coroutine',
              'iotestpy.exception', 'iotestpy.pythoncpp', 'iotestpy.pywebtest'],
    url='',
    license='',
    install_requires=dependencies,
    author='zhanglin',
    author_email='',
    description=''
)
