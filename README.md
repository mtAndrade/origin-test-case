# origin-test-case

## Technologies
* Aiohttp Framework: with Gunicorn and Marshmallow libraries
* Python 3.8
* Docker & Docker-Compose

## How to Run
To run this application you will need to first have docker & docker-compose installed.
Run the following commands to build and start the application using docker
```sh
$ make docker-build
$ make docker-start
```

The application should start on port `8080`.


## Endopoints & How to use.

|Endpoint|Method|Action|
| ------ | ------ |------ |
|/risk/profile|POST| Create a Risk Profile|

Here is an usage example 
```
curl --location --request POST 'localhost:3000/risk/profile' \
--header 'Content-Type: application/json' \
--data-raw '{
  "age": 1,
  "dependents": 2,
  "house": {"ownership_status": "owned"},
  "income": 0,
  "marital_status": "married",
  "risk_questions": [1,0,1],
  "vehicle": {"year": 2018}
}'
```

To run the tests you should run
```sh
$ make docker-test
```

## Choices and strategies

In this section I will describe the technologies used in the project and the reasons why I chose them.

### Aiohttp

I chose Aiohttp mostly because it is a simple and fast client/server framework with which I have some familiarity. 
I chose a stable yet recent enought Python version that met all the framework's requirements. The language choice was mainly intended as a refresh course for myself. It has been a while since a coded with something other than PHP.

### Docker & Server 

Docker is my go to technology for my local development.
At first I was focused on creating a structure that could have been easily deployed, with different environments and pipelines. But this approach was taking too much time so I gave up as this was not required by the test.

### Main Algorithm
I used a slightly changed Chain Of Responsibilities Pattern. Python has a very neat way of chaining functions and I used it to develop the ChainScoreRule, which holds all and maintain the chain. A Profiler, which is a Factory-like class, is responsible to create several chains to score each risk aspect. The idea behind this implementation was keep the code structure and business logic as segregated as possible while providing a nice readable chain of events. I started the application thinking about the Strategy Pattern, but it made less sense than Chain. The main gain of the Strategy is to change logic in runtime, which is not something this project needed and, in time, the number rules could grow and Strategy would become messier over time. 


 ### Final notes
 I had quite a bit of fun with this little project. It is quite simple and yet challenging. 

 This project could benefit from some improvements like a CI/CD, logging, coverage, linter and  more tests, because there is no such thing as too many tests.



