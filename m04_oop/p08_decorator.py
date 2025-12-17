def log_execution_time(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[{func.__name__}] started at {start}")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] ended at {end}")
        print(f"[{func.__name__}] executed in {end - start:4f}s")
        #return f"result = {result}"
        return result

    return wrapper


def print_result(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("-" * 80)
        print(f"| RESULT: {result} |")
        print("-" * 80)
        return result

    return wrapper


@print_result
@log_execution_time
def complex_calculation(n: int) -> int:
    return sum(range(n))


if __name__ == "__main__":
    complex_calculation(500000000)
