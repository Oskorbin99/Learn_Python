# collections.OrderedDict — помнят порядок вставки ключей

import collections

d = collections.OrderedDict(one=1, two=2, three=3)

print(d)

d['четыре'] = 4
print(d)
print(d.keys())

# collections.defaultdict — возвращает значения, заданные по умолчанию для отсутствующих ключей

dd = collections.defaultdict(list)

dd['собаки'].append('Руфус')
dd['собаки'].append('Кэтрин')
dd['собаки'].append('Сниф')
print(dd['собаки'])
print(dd['собаки'])

# collections.ChainMap — производит поиск в многочисленных словарях как в одной таблице соответствия

from collections import ChainMap
dict1 = {'один': 1, 'два': 2}
dict2 = {'три': 3, 'четыре': 4}
chain = ChainMap(dict1, dict2)
print(chain)
# ChainMap выполняет поиск в каждой коллекции в цепочке
# слева направо, пока не найдет ключ (или не потерпит неудачу):
print(chain['три'])

print(chain['один'])

#print(chain['отсутствует'])

# types.MappingProxyType — обертка для создания словарей только для чтения
from types import MappingProxyType
writable = {'один': 1, 'два': 2}# доступный для обновления
read_only = MappingProxyType(writable)

# Этот представитель/прокси с доступом только для чтения:
# >>> read_only['один']
# 1
# >>> read_only['один'] = 23
# TypeError:
"'mappingproxy' object does not support item assignment"
# Обновления в оригинале отражаются в прокси:
# >>> writable['один'] = 42
# >>> read_only
# mappingproxy({'один': 42, 'один': 2})



