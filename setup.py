from setuptools import setup, find_packages

setup(name='pytest-api-tester',
      description='Testing framework created using Python for functional testing of REST APIs.',
      url='https://github.com/luvsharma19/python-api-tester',
      version='1.0.0',
      author='luv sharma',
      author_email='luvsharma1931@yahoo.com',
      python_requires='>=3.7',
      packages=find_packages(),
      install_requires=['requests', 'flake8'])
