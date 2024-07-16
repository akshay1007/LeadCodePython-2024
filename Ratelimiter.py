import time
from collections import deque
from typing import Deque, Dict

# Store user request timestamps
user_requests: Dict[str, Deque[float]] = {}
# Constants
WINDOW = 1  # seconds
RATE = 3

def is_rate_limited(user_id: str) -> bool:

    current_time = time.time()
    
    # If user is not in the dictionary, add them with an empty deque
    if user_id not in user_requests:
        user_requests[user_id] = deque()

    # Remove timestamps that are outside the window
    while user_requests[user_id] and user_requests[user_id][0] <= current_time - WINDOW:
        user_requests[user_id].popleft()
    
    # Check if user has exceeded the rate limit
    if len(user_requests[user_id]) >= RATE:
        return True
    
    # Add the current request timestamp
    user_requests[user_id].append(current_time)
    return False


