def test_sort(func, array, reversed_order=False):
    assert sorted(array, reverse=reversed_order) == func(array), 'Проверьте алгоритм'
    print('Test passed')


def test_median(func, array):
    median = sorted(array)[len(array) // 2]
    median_tested = func(array)
    assert median == median_tested, f'{median} != {median_tested}'
    print('Test passed')
