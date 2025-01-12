import time
import pytest 

def slow_function():
    time.sleep(0.5)
    return("Done")

@pytest.mark.benchmark
def test_slow_function(benchmark):
    result = benchmark(slow_function)
    assert result == "Done"