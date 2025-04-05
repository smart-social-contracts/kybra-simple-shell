try:
    from kybra import ic
except:
    pass

import ast
import json

def custom_print(message: str):
    try:
        ic.print(message)
    except:
        print(message)


def run_test(test_id: str) -> int:
    return globals()[f"test_{test_id}"]()


def test_escaped_strings():
    """Test function that returns various escaped strings to verify proper handling."""
    # String with various escape sequences
    test_string = "Line1\nLine2\tTabbed\rCarriage Return\fForm Feed\v\"Quotes\" and \\Backslashes\\"
    # Multiline string
    multiline = """This is a
multiline string
with "quotes" and \backslashes"""
    # Dictionary with nested structures
    complex_data = {
        "text": "Text with \n newlines and \t tabs",
        "numbers": [1, 2, 3],
        "nested": {
            "boolean": True,
            "null": None,
            "special": "Special \u2728 Unicode"
        }
    }
    
    # Return different formats for testing
    result = {
        "regular_string": test_string,
        "multiline_string": multiline,
        "repr_string": repr(test_string),
        "complex_data": complex_data,
        "json_string": json.dumps(complex_data)
    }
    
    return result


def test_properly_unescape_output():
    """Test function for the improved unescaping functionality."""
    # Sample of what might be returned from dfx
    sample_dfx_output = '("Line1\\nLine2\\tTabbed text")'
    
    # Current implementation - limited unescaping
    match = '("Line1\\nLine2\\tTabbed text")'.strip('(").') 
    basic_unescaped = match.replace('\\n', '\n').replace('\\"', '"')
    
    # Improved implementation - using ast.literal_eval
    # Extract the quoted string from dfx output
    improved_match = sample_dfx_output[2:-2]  # Remove (") and ")
    # Use ast.literal_eval to properly unescape the string
    try:
        properly_unescaped = ast.literal_eval(f'"{improved_match}"')
    except (SyntaxError, ValueError):
        properly_unescaped = improved_match
    
    # Return both approaches for comparison
    return {
        "original": sample_dfx_output,
        "basic_unescaped": basic_unescaped,
        "properly_unescaped": properly_unescaped
    }


if __name__ == "__main__":
    import sys

    operation = sys.argv[1]
    test_id = sys.argv[2]

    sys.exit(globals()[f"run_{operation}"](test_id))
