from fastapi import FastAPI, Query
from typing import List, Tuple

app = FastAPI()

statistics = {}

def fizz_buzz(int1: int, int2: int, limit: int, str1: str, str2: str) -> List[str]:
    result = []
    for i in range(1, limit + 1):
        if i % int1 == 0 and i % int2 == 0:
            result.append(str1 + str2)
        elif i % int1 == 0:
            result.append(str1)
        elif i % int2 == 0:
            result.append(str2)
        else:
            result.append(str(i))
    return result

@app.get('/fizzbuzz', response_model=List[str])
def fizzbuzz(int1: int = Query(..., description="First integer"),
             int2: int = Query(..., description="Second integer"),
             limit: int = Query(..., description="Limit of numbers"),
             str1: str = Query(..., description="String for multiples of int1"),
             str2: str = Query(..., description="String for multiples of int2")):

    result = fizz_buzz(int1, int2, limit, str1, str2)

    # Update statistics
    request_params = (int1, int2, limit, str1, str2)
    statistics[request_params] = statistics.get(request_params, 0) + 1
    return result

@app.get('/statistics')
def get_statistics():
    if not statistics:
        return {'message': 'No statistics available'}

    most_used_request = max(statistics, key=statistics.get)
    hits = statistics[most_used_request]

    return {
        'most_used_request': {
            'int1': most_used_request[0],
            'int2': most_used_request[1],
            'limit': most_used_request[2],
            'str1': most_used_request[3],
            'str2': most_used_request[4],
            'hits': hits
        }
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
