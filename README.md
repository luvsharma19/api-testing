# Testing framework created using Python for functional testing of REST APIs. 

## Get started with writing API tests in a easy and simplified way. No boiler plate code required.

This testing framework created using python make it simple to write and  maintain tests for REST APIs without worrying about writing extra boilerplate code. 

You can mention the REST API server details like server address, port number and credentials in the global configuation file and then directly start writing test cases under tests folder. 

All the reusable fucntions like HTTP server methods are provided under the HTTP utility class. There is a Authentication helper class also available for authentication of user and fetching authorization token from the API server.

I have used Pytest fixtures to implement the HTTP utility class and Authentication helper class. Before a test case runs, the Authentication helper class authenticates user and fetches the authorization token. Then, Http utiliy class initialized and the authorization token is set in the request headers.

In a test case, you only need to call the HTTP utility class methods to perform the REST API operation and assert the result. 
