from django.db.models import Q
import operator
import functools

class FilterAggregator:

  def __init__(self, operand: str ) -> None:
    self._operand: str = operand
    self._list = []

  def add(self, q_object: Q) -> None:
    self._list.append(q_object)

  def get_aggregated_results(self) -> Q:
    operation = operator.and_
    if self._operand == "OR":
      operation = operator.or_
    return functools.reduce(operation, self._list)