# Testing framework created using Python for functional testing of REST APIs. 

## Get started with writing API tests in a easy and simplified way. No boilerplate code required.

This testing framework created using python make it simple to write and  maintain tests for REST APIs without worrying about writing extra boilerplate code. 

You can mention the REST API server details like server address, port number and credentials in the global configuation file and then directly start writing test cases under tests folder. 

All the reusable fucntions like HTTP server methods are provided under the HTTP utility class. There is a Authentication helper class also available for authentication of user and fetching authorization token from the API server.

I have used Pytest fixtures to implement the HTTP utility class and Authentication helper class. Before a test case runs, the Authentication helper class authenticates user and fetches the authorization token. Then, Http utiliy class initialized and the authorization token is set in the request headers.

In a test case, you only need to call the HTTP utility class methods to perform the REST API operation and assert the result. 

## How to run the tests

Please download the code from this repository and make sure you have python verion greater or equal to 2.7 installed on your system. 

- Go inside the python-api-tester directory

  cd python-api-tester

- Run the following command to install the dependencies listed in setup.py

  python setup.py install

- Run the following command to run the test cases written under the "tests" module

  pytest .


A sample test for creating a user has been added in the repo. Please refer the code files in the repo. All the Pytest commands will work for this testing framework also.


Please feel free to provide you feedback and contribute to this project by creating a pull request. You can also reach me via email - luvhsharma1931@gmail.com
