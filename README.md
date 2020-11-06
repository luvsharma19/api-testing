# api-testing: API Testing framework for functional testing of REST APIs

## Get started with writing API tests in an easy and simplified way. No boilerplate code required.

This API testing framework created using python make it simple to write and  maintain tests for REST APIs without worrying about writing extra boilerplate code. 

You can mention the REST API server details like server address, port number and credentials in the global configuation file and then directly start writing test cases under tests folder. 

All the reusable functions like HTTP server methods are provided under the HTTP utility class. There is a Authentication helper class also available for authentication of user and fetching authorization token from the API server.

Pytest fixtures are used to implement the setup and teardown methods from HTTP utility class and Authentication helper class. Before a test case runs, the Authentication helper class authenticates user and fetches the authorization token. Then, the Http utiliy class is initialized and the authorization token is set in the request headers. After the test case run is completed, the authorization token is deleted also from the API server.

You can start writing the test cases directly and call the HTTP utility class methods to perform the REST API operations. You can use Pytest assertions to assert on the REST API operation result.

## How to run the tests

Please make sure you have python version greater than or equal to 3.7 installed on your system. You can install it from official python website: https://www.python.org/downloads/release/python-379/

- Download or clone the code from the api-testing repository to your system
  https://github.com/luvsharma19/api-testing  

- Go to the directory location of downloaded or cloned code folder - "api-testing"
  cd api-testing

- Run the following command to install the dependencies listed in requirements.txt
  pip install -r requirements.txt

- Write test cases under the folder "tests". ( A example test case for creating a user is already present in the folder )

- Run the following command to run the test cases written under the "tests" folder
  pytest .

You can go through the folder structure of the api-testing module to get familier with testing framework. Also, all the Pytest commands will work for this testing framework also.

Please feel free to provide you feedback and contribute to this project by creating a pull request. You can also reach me via email - luvsharma1931@yahoo.com
