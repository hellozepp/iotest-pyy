from setuptools import setup

dependencies = [
    "packaging >= 14.3, <24.0.0dev",
    "python-dateutil >= 2.7.2, <3.0dev",
    "requests >= 2.21.0, < 3.0.0dev",
    "pyarrow >= 10.0.1, <11.0.0",
    "pandas >=1.5.3",
    "APScheduler >= 3.10.4",
    "mock",
    "simplejson",
    "backports.zoneinfo>=0.2.1;python_version<'3.9'",
    "sanic",
    "flask",
    "sqlglot",
    "fastapi==0.103.1",
    "uvicorn==0.23.2",
    "gunicorn",
    "numpy~=1.24.4", # gunicorn needs numpy
    "tzlocal",
    "pytest"
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
