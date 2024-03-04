import functools
import memory_profiler
import requests


def memory_usage(f):
    @functools.wraps(f)
    def deco(*args, **kwargs):
        mem_before_func = memory_profiler.memory_usage()[0]
        print(mem_before_func)
        result = f(*args, **kwargs)
        mem_after_func = memory_profiler.memory_usage()[0]
        print(mem_after_func)
        print(f"Использовано {mem_after_func - mem_before_func}MB памяти.")
        return result
    return deco

#ТЕСТ
@memory_usage
def fetch_url(url, first_n=100):
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


print(fetch_url('https://dnipro.ithillel.ua/ru', first_n=42))

@memory_usage
def create_list(n):
    my_list = list(range(n))
    return my_list


result = create_list(200_000_000)
