# DatoramaPy

## Authentication

* Getting API Token

![api_token](https://i.imgur.com/pb9CMaD.png)

## Usage

* Query API Example
```python
from datorama import Datorama

datorama = Datorama("your_api_token")

query_to_send = {
    "workspaceId": "XXXX",
    "dateRange": "THIS_MONTH",
    "measurements": [
        {
            "name": "Data Stream Total Rows" 
        } 
    ],
    "dimensions": [
        "Data Stream" 
    ]
}

datorama.query(query_to_send)
```
