from setuptools import setup, Extension

setup(
  name = 'mjsmodule', 
  version = '0.0.0.0.1',
    ext_modules = [
      Extension('mjsmodule', ['mjsso.c','client.c','player.c','score.c'], 
                extra_compile_args=['-Wno-unused-variable'])
    ]
)
