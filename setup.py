from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(name='api-testing',
      description='API Testing framework for functional testing of REST APIs',
      url='https://github.com/luvsharma19/api-testing',
      version='1.0.0',
      author='luv sharma',
      long_description=long_description,
      long_description_content_type="text/markdown",
          classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
      python_requires='>=3.7',
      packages=find_packages(),
      install_requires=['requests', 'flake8'])
