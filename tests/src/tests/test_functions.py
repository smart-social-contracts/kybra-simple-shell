try:
    from kybra import ic
except:
    pass


def custom_print(message: str):
    try:
        ic.print(message)
    except:
        print(message)


def run_test(test_id: str) -> int:
    return globals()[f"test_{test_id}"]()


if __name__ == "__main__":
    import sys

    operation = sys.argv[1]
    test_id = sys.argv[2]

    sys.exit(globals()[f"run_{operation}"](test_id))
