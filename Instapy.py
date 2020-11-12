
class SearchRelationOfClass:
    def __init__(self, n):

        self.dictor = {} # Создаем словарь чтобы туда поместить Граф. Значения которые мы потом будем перебирать

        for i in range(n):

            l = input().split(':') # разбиваем введенное значение на ключ и значение. Значением будет список
            l = [el.strip() for el in l] # убираем лишние пробелы справа и слева чтобы не получить левые данные


            if len(l) > 1: # Если список состоит из двух элементов то добавляем в словарь ключ и список со значениями

                self.dictor.update({l[0]:l[1].split(' ')})
                print(self.dictor)

            else: # Иначе если список состоит только с одним значением то создаем ключ с пустым списком

                self.dictor.update({l[0]:[]})

    def print_all_list(self):

        print(self.dictor.items()) # Выводим все что есть в словаре чтобы проверить правильно ли попадают значения туда

    def find_path(graph, start, end, path=[]):

        path = path + [start]

        if start == end:

            return path

        if not start in graph:

            return None

        for node in graph[start]:

            if node not in path:

                newpath = SearchRelationOfClass.find_path(graph, node, end, path)

                if newpath:
                    return newpath

        return None

searcher = SearchRelationOfClass(5)

searcher.print_all_list()