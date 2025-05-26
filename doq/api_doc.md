# Beschreibung der <var>Open Trivia API</var>


## Session Tokens

- Benutzen: ```https://opentdb.com/api.php?amount=10&token=YOURTOKENHERE```

- Erhalten: ``` https://opentdb.com/api_token.php?command=request```

- Reset: ```https://opentdb.com/api_token.php?command=reset&token=YOURTOKENHERE```

## Response Codes


 -   Code 0: Success Returned results successfully.
 -   Code 1: No Results Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)
 -   Code 2: Invalid Parameter Contains an invalid parameter. Arguements passed in aren't valid. (Ex. Amount = Five)
 -   Code 3: Token Not Found Session Token does not exist.
 -   Code 4: Token Empty Session Token has returned all possible questions for the specified query. Resetting the Token is necessary.
 -   Code 5: Rate Limit Too many requests have occurred. Each IP can only access the API once every 5 seconds.

## Encoding 
 -   Default Encoding (HTML Codes):
 -   Legacy URL Encoding:
 -   URL Encoding (RFC 3986):
 -   Base64 Encoding:

## API Tools

### Category Lookup:

```https://opentdb.com/api_category.php```

### Category Question Count Lookup: 

```https://opentdb.com/api_count.php?category=CATEGORY_ID_HERE```

#### Global Question Count Lookup: 

```https://opentdb.com/api_count_global.php```



 HINT:  
  - Only 1 Category can be requested per API Call. To get questions from any category, don't specify a category.
  - A Maximum of 50 Questions can be retrieved per call.

