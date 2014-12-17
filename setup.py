from setuptools import setup, Extension, find_packages

setup(name='ns_sample',
      version='0.1',
      author='Filip Sufitchi',
      author_email="fsufitchi@gmail.com",
      description="Neustar Code Sample",
      url="https://github.com/fsufitch/ns-sample",
      packages=find_packages('src'),
      package_dir={'':'src'},
      entry_points = {
        'console_scripts': ["ns_demo=ns_sample.script:main"],
        },
      install_requires=["docker-py"],
      )
