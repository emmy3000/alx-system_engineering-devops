# 0x16. API Advanced

## Description:
------------
The "0x16. API Advanced" project explores advanced concepts in working with APIs, focusing primarily on the Reddit API. It covers a range of tasks, from understanding and navigating API documentation to practical implementation of recursive API calls, pagination handling, JSON parsing, and dictionary sorting. This project provides hands-on experience in extracting and processing data from a real-world API.

## Key Concepts Covered:
----------------------
- Reading API documentation to identify relevant endpoints.
- Utilizing API pagination to handle large data sets.
- Parsing JSON responses from APIs to extract meaningful information.
- Implementing recursive API calls for retrieving data across multiple pages.
- Sorting dictionaries based on their values.

## Project Files:
--------------
| Module/Script   | Functionality                                    |
|-----------------|-------------------------------------------------|
| `0-subs.py`     | Queries Reddit API for the number of subscribers|
|                 | for a given subreddit.                          |
|                 | Handles invalid subreddit input and returns 0.  |
| `1-top_ten.py`  | Queries Reddit API and prints titles of the     |
|                 | first 10 hot posts for a specified subreddit.   |
| `2-recurse.py`  | Implements a recursive function to query the    |
|                 | Reddit API and retrieve titles of all hot       |
|                 | articles for a given subreddit. Handles         |
|                 | pagination and returns a list of titles or None |
|                 | if no results are found.                        |

## Author:
-------
Jim Jenkins

This project provides valuable hands-on experience in dealing with practical scenarios involving API interactions, data extraction, and manipulation using the Python programming language. It equips learners with the skills to tackle real-world challenges when working with APIs and empowers them to retrieve and analyze data effectively.
