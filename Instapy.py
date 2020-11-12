
class SearchRelationOfClass:
    def __init__(self, n):

        self.dictor = {}

        for i in range(n):

            l = input().split(':')

            if len(l) > 1:

                self.dictor.update({l[0]:l[1].split(' ')})

            else:

                self.dictor.update({l[0]:[]})

    def print_all_list(self):

        print(self.dictor.items())

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