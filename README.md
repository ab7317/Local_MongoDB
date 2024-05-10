# Local_MongoDB

##Description 
This will have the class to interact with MongoDB, it can be used to push csv files to mongoDB or preform other functions on a database

##Setup
- service name - MongoDB
- version - 7.0.9

##DB
- URI -> "mongodb://localhost:27017/"
When sending queries you can filter for greater than and less than with the following syntax
- All example below use the FB_Assets table
- [{"Coin":"ATOM"}, {"USDValue": {"$gt": 1000000}}] This query would find all ATOM's with a USDValue greater than 1000000
- [{"Coin":"ATOM"}, {"USDValue": {"$lt": 1000000}}] This query would find all ATOM's with a USDValue lower than 1000000
- [{"Coin":"ATOM"}, {"USDValue": {"$gt": 1000000}}, {"Time": {"$gt":"18-00"}}] This query would do the same as the first but only with times after 6pm 
