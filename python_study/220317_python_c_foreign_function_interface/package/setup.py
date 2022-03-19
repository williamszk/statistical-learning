# https://www.youtube.com/watch?v=X5irxO5VCHw&ab_channel=anthonywritescode


from setuptools import setup

setup(
    name="uuidcffi", #  C foreign function interface
    version="1",
    py_modules=["uuidcffi"],
    install_requires=["cffi"],
    setup_requires=["cffi"],
    cffi_modules=["build_uuidcffi.py:ffibuilder"],
)























