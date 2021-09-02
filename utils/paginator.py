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
    object = None
    current_position = 0
    has_more = False
    with_subclasses = False

    def __init__(self, object, with_subclasses=False):
        self.object = object
        self.__check_and_set_has_more(self.current_position, object)
        self.with_subclasses = with_subclasses

    def __check_and_set_has_more(self, current_position, object):
        if current_position >= len(object.objects.all()):
            self.has_more = False
        else:
            self.has_more = True

    def get_objects(self, offset, limit):
        self.current_position = offset + limit
        self.__check_and_set_has_more(self.current_position, self.object)
        return PaginatedResults(self.object.objects.all()[offset:limit], self.has_more, self.with_subclasses)
