from kybra import ic, query, update

# Import and expose all the test functions
from tests import test_functions


@query
def greet() -> str:
    """Basic test function"""
    return "Hello from the logging test canister!"

