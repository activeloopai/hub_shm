from distutils.core import setup, Extension
from setuptools import find_packages

import sys
import platform
import subprocess

if sys.version_info[0] == 3 and sys.version_info[1] == 6:
    subprocess.run(
        ["python", "shm/py36_clinic.py", "shm/posixshmem.c"]
    )
elif sys.version_info[0] == 3 and sys.version_info[1] == 7:
    subprocess.run(
        ["python", "shm/py37_clinic.py", "shm/posixshmem.c"]
    )
else:
    raise ValueError("Must run on Python 3.6 or 3.7")


linux_module = Extension(
    "shm/_posixshmem",
    define_macros=[
        ("HAVE_SHM_OPEN", "1"),
        ("HAVE_SHM_UNLINK", "1"),
        ("HAVE_SHM_MMAN_H", 1),
    ],
    libraries=["rt"],
    sources=["shm/posixshmem.c"],
)


darwin_module = Extension(
    "shm/_posixshmem",
    define_macros=[
        ("HAVE_SHM_OPEN", "1"),
        ("HAVE_SHM_UNLINK", "1"),
        ("HAVE_SHM_MMAN_H", 1),
    ],
    sources=["shm/posixshmem.c"],
)


setup(
    name="hub_shm",
    version="1.0.0",
    description="Hub Shared Memory",
    py_modules=["hub_shm"],
    packages=find_packages(),
    ext_modules=[linux_module]
    if platform.system() == "Linux"
    else [darwin_module]
    if platform.system() == "Darwin"
    else [],
)
