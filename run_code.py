import builtins
from typing import List
from typing import *
from constants import dangerous_functions
from special_data_types import ListNode

def run_code(user_code):
    
    safe_builtins = {k: v for k, v in builtins.__dict__.items() if k not in dangerous_functions}
            
    restricted_globals = {
        '__builtins__': safe_builtins,
        'List': List,
        'ListNode': ListNode,
        'Optional': Optional, 
    }
    exec(user_code, restricted_globals)
    return restricted_globals