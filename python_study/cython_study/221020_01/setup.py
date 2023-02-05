from setuptools import setup
from Cython.Build import cythonize

setup(
    name='my-awesome-cython-code',
    ext_modules=cythonize(["hello.pyx", "integrate_comp.pyx",
    "integrate_cy.pyx" 
    ]),
    zip_safe=False,
)