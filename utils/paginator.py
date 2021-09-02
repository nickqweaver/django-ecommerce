class PaginatedResults():
    results = None
    has_more = False

    def __init__(self, results, has_more, with_subclasses=False):
        if with_subclasses:
            self.results = results.select_subclasses()
        else:
            self.results = results
        self.has_more = has_more


class Paginator():
    objects = None
    current_position = 0
    has_more = False
    with_subclasses = False

    def __init__(self, objects, with_subclasses=False):
        self.objects = objects
        self.__check_and_set_has_more(self.current_position, objects)
        self.with_subclasses = with_subclasses

    def __check_and_set_has_more(self, current_position, objects):
        if current_position >= len(objects.all()):
            self.has_more = False
        else:
            self.has_more = True

    def get_objects(self, offset, limit):
        self.current_position = offset + limit
        self.__check_and_set_has_more(self.current_position, self.objects)
        return PaginatedResults(self.objects.all()[offset:limit], self.has_more, self.with_subclasses)
