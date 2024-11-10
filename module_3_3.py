from main import values_list_2


def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list_ = [1, 'str', False]
values_dict = {'a': [1, 2, 3], 'b': 'grey', 'c': 123}
print_params(*values_list_)
print_params(**values_dict)
values_list_2 = ['urb', 123]
print_params(52, *values_list_2)




