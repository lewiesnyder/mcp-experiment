# MCP Experiment
A simple MCP server for various experiments like a sql agent

## Notes
* Download the the [chinook sample database](https://www.sqlitetutorial.net/sqlite-sample-database/) to `./dist/chinook.db`
* `poetry install`


## Resources
-  **schema://main** -> the chinook database schema

## Tools
- **query_data** - query the database 
    - args: sql (str) the sql to run against the database
 

 ## As docker
 ```
 docker build --rm -t mcp-experiment .
 ```
