from setuptools import setup

setup(name='Hello', 
      version='1.0', 
      description='Python package example', 
      author='MM', 
      author_email='', 
      packages=['Hello', 'Hello.InnerModule'], 
      license='MIT', 
      python_requires='>=3.8', 
      install_requires=[ 'numpy' ] 
     ) 

