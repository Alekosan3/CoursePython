
class SearchRelationOfClass:
    def __init__(self, n):
        self.dictor = {} # Создаем словарь чтобы туда поместить Граф. Значения которые мы потом будем перебирать

        for i in range(n):
            l = input().split(':') # разбиваем введенное значение на ключ и значение. Значением будет список
            l = [el.strip() for el in l] # убираем лишние пробелы справа и слева чтобы не получить левые данные

            if len(l) > 1: # Если список состоит из двух элементов то добавляем в словарь ключ и список со значениями
                self.dictor.update({l[0]:l[1].split(' ')})

            else: # Иначе если список состоит только с одним значением то создаем ключ с пустым списком
                self.dictor.update({l[0]:[]})

    def print_all_list(self):

        print(self.dictor) # Выводим все что есть в словаре чтобы проверить правильно ли попадают значения туда

    def find_path(self, start, end, path=[]):

        graph = self.dictor

        path = path + [start]

        if start == end:
            return path

        if not start in graph:
            return None

        for node in graph[start]:
            if node not in path:
                newpath = SearchRelationOfClass.find_path(self, node, end, path)
                if newpath:
                    return newpath

        return None

    def has_relation_between_two_classes(self, n):

        for i in range(n):
            l = input().split(' ')
            m = self.find_path(l[1],l[0])

            if type(m) != type(None):
                if l[1] in m:
                    print('Yes')
                else:
                    print('NO')
            else:
                print('NO')


searcher = SearchRelationOfClass(int(input()))

searcher.has_relation_between_two_classes(int(input()))