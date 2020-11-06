from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(name='api-testing',
      description='API Testing framework for functional testing of REST APIs',
      url='https://github.com/luvsharma19/api-testing',
      version='1.0.0',
      author='luv sharma',
      license='MIT',
      long_description=long_description,
      long_description_content_type="text/markdown",
          classifiers=[
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
    keywords='rest api testing, api testing, api tests, rest api, testing, pytest',
    project_urls={
    'Source': 'https://github.com/luvsharma19/api-testing'
},
    python_requires='>=2.7',
    packages=find_packages(),
    install_requires=['requests', 'flake8'])
