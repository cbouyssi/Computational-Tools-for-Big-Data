from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["cdecompression.pyx", "ctext_extractor.pyx", "csplit_file.pyx"])
)
