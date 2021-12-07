from typing import List
from typing import TypeVar, Generic

T = TypeVar('T')


class PaginatedResults(Generic[T]):

    def __init__(self, results: List[T], has_more: bool = False, with_subclasses: bool = False) -> None:
        if with_subclasses:
            self.results = results.select_subclasses()
        else:
            self._results = results
        self._has_more = has_more

    @property
    def results(self) -> List[T]:
        return self._results

    @property
    def has_more(self) -> bool:
        return self._has_more

    @results.setter
    def results(self, results: List[T]) -> None:
        self._results = results

    @has_more.setter
    def has_more(self, has_more: bool) -> None:
        self._has_more = has_more


class Paginator(Generic[T]):
    _objects: T
    _current_position: int = 0
    _has_more: bool
    _with_subclasses: bool

    def __init__(self, objects: T, with_subclasses: bool = False):
        self._objects = objects
        self.__check_and_set_has_more(self._current_position, objects)
        self._with_subclasses = with_subclasses


    def __check_and_set_has_more(self, current_position, objects) -> None:
        if current_position >= len(objects.all()):
            self._has_more = False
        else:
            self._has_more = True

    def get_objects(self, offset, limit) -> List[T]:
        self._current_position = offset + limit
        self.__check_and_set_has_more(self._current_position, self._objects)
        try:
            results: List[T] = PaginatedResults(
                self._objects.all()[offset:offset+limit], self._has_more, self._with_subclasses)
            return results
        except:
            raise Exception(
                "There was a problem fetching your results")
     