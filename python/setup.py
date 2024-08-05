from setuptools import setup, find_packages

INSTALL_REQUIRES = [
  "cyclonedds",
  "numpy",
  "pygame",
]

setup(
  name="unitree_dds_wrapper",
  author="Agnel Wang",
  version="0.1.0",
  description="Unitree DDS Wrapper to simplify the communication with Unitree Robots",
  install_requires=INSTALL_REQUIRES,
  packages=find_packages("."),
)