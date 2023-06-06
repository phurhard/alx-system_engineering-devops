Learnt how to work with pagination in API calls and how to use recursive functions for calls

```
0-subs: Returns the total number of subscribers to a subreddit

Whilw embarking on this task, the major challenge was how to set up a custom user agent, but searching on google, got a redirection to the question on (reddit platform)[r/redditdev], after that came the challenge of getting the required endpoint, all operations proved abortive as the response was a constant 404 not found. then i proceeded to copy from sample code online, i tried running it, it ran correctly. this lead to me trying to debug what went wrong, and i found out that in my url declaring, i didn't follow the correct formatting.
what i did || what i should have done
api = "https://www.reddit.com/r/{subreddit}/.json" || api = f"https://www.reddit.com/r/{subreddit}/.json

duration
The debugging took me a total of 1hour 15minutes
on to task two now
```

```
1-top_ten: Prints the titles of the first 10 hot posts listed for a given subreddit

This task is easy to accomplish, bacause the example i saw that helped me complete the task above, was based on this task. i just had to adjust the API endpoint
```
