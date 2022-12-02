# import our libraries
from sec_api import QueryApi
import json

# I have used my own api_key, in order to obtain access to the SEC database
api_key = "351e6fbb9b9ab7546cc1356e86ff02ac5f2b37dfa9592653ece8648af212f80f"

queryApi = QueryApi(api_key=api_key)

# This query will search for all 8-K filings containing an EXHIBIT 2.1. This query will only show 10 filings
query = {
    "query": {
        "query_string": {
            "query": "formType:\"8-K\" AND documentFormatFiles.description:\"EX-2.1\""
        }
    },
    "from": "0",
    "size": "10",
    "sort": [{"filedAt": {"order": "desc"}}]
}

# The results of the query are defined as filings
response = queryApi.get_filings(query)

# Print our first filing
print(json.dumps(response["filings"][0], indent=2))
