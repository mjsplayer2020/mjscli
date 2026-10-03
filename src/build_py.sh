#!/bin/sh
python3 setup.py install

mv ./build/lib.linux-x86_64-cpython-312/mjsmodule.cpython-312-x86_64-linux-gnu.so ../.
