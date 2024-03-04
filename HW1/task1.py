import functools
from collections import OrderedDict
import requests


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                # Рахуємо кількість використань
                deco._cache_count[cache_key] += 1
                return deco._cache[cache_key]
            # Передаем все аргументы и ключевые аргументы в f
            result = f(*args, **kwargs)
            # видаляємо якшо досягли ліміта
            if len(deco._cache) >= max_limit:
                least_used_key = min(
                    deco._cache_count, key=deco._cache_count.get)
                deco._cache.pop(least_used_key)
                deco._cache_count.pop(least_used_key)
            deco._cache_count[cache_key] = 0
            deco._cache[cache_key] = result
            return result
        deco._cache = OrderedDict()
        deco._cache_count = {}
        return deco
    return internal


# ТЕСТ


@cache(max_limit=3)
def cache_test(x):
    print("Нове значення в кеші")
    return x * x


print(cache_test(2))
print(cache_test(4))
print(cache_test(2))
print(cache_test(2))
print(cache_test(4))
print(cache_test(4))
print(cache_test(5))
print(cache_test(5))
print(cache_test(4))
print(cache_test(3))
print(cache_test(3))
print(cache_test(4))
print(cache_test(2))
print(cache_test(3))
print(cache_test(2))
print(cache_test(4))
print(cache_test(4))
print(cache_test(3))
print(cache_test(5))
print(cache_test(5))

print(cache_test._cache)


@cache(max_limit=3)
def fetch_url(url, first_n=30):
    res = requests.get(url)
    print("Нове значення в кеші")
    return res.content[:first_n] if first_n else res.content


print(fetch_url('https://dnipro.ithillel.ua/'))
print(fetch_url('https://dnipro.ithillel.ua/'))
print(fetch_url('https://dnipro.ithillel.ua/'))
print(fetch_url('https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-decorators'))
print(fetch_url('https://habr.com/ru/companies/piter/articles/732310/'))
print(fetch_url('https://habr.com/ru/companies/piter/articles/732310/'))
print(fetch_url('https://habr.com/ru/companies/piter/articles/732310/'))
print(fetch_url('https://pypi.org/project/memory-profiler/'))
print(fetch_url('https://pypi.org/project/memory-profiler/'))
print(fetch_url('https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-decorators'))
print(fetch_url('https://docs.python.org/3/reference/compound_stmts.html#grammar-token-python-grammar-decorators'))
