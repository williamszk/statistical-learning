from setuptools import setup
from Cython.Build import cythonize

setup(
    name='my-awesome-cython-code',
    ext_modules=cythonize([
        "integrate1.py",
        "integrate2.py",
        "module.py",
    ]),
    zip_safe=False,
)