# Unique Id Generators

As a noobie, I used to generated id's using uuid() package for npm.It is good, and has advantages, but not without several drawbacks :

The unique id's are just unique strings, they don't really mean anything. This is a good and a bad thing.

(a) **Good because** - no one can really make sense of 1000 random id's. For example if you're Facebook, and the id's you carry have meaning, for example if you use incremental id's from db to represent users. 

In that case it's very easy to write a web scraper which can go to Facebook.com/user/1 , /user/2 and so on to scrape data, since id's are predictable.

(b) **Bad because** if I want to sort out user image uploads in order, a incremental id is easier for me to use and fetch data. If I need first 10 images, I fetch 0 to 9 or 1 to 10 , it's easy to predict data. 

2. 128 bit - uuids take 128 bit of storage space. This is not necessarily bad but more like we can get the same thing done for cheaper. 

3. UUIDs are strings and just a int / big int based id generation will be more performant in the database. 


Now, if you just need unique ids and nothing else, uuid might be good to go in most cases, but this repo has following implementation to refer in case you need something more. 


# Strategies for unique id generation

Below is demonstration of multiple id generation patterns, including patterns inspired from twitter/sony, amazon, Instagram etc.

## Id's that are incremental in nature - v1

Since time grows linearly, it's always incremental compared to the past, it's a good base to generate incremental id's of. The use case is to have your own basic id generation inside a function. 

The catch : If two ids are generated at the same time, they will clash. This applies within the same machine and across the network with this basic program.

## Making the incremental id generator work on multi-node systems - v2

To improve v1, we will implement support for machine id's and threads inside each machine to add support for multi-node & multi-threaded systems.

## ID generation service 

To make id generation more reliable and have less possibilities of conflicts, we implement a service that will generated id's for everything that requires ids. 

This will batching based implementation inspired by amazon.

## Twitter's snowflake service

Implementation of snowflake id generation service, inspired from twitter. (now X) 

## Stored procedure based ID generation (inspired by Instagram)

The id generation that scales well with the database, simply by generating id inside the db with stored procedure. 