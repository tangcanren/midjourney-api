from collections import defaultdict

from loguru import logger

from util._queue import taskqueue

RESULT_TABLE = defaultdict(dict)


def callback(data):
  logger.debug(f"callback data: {data}")
  # TODO(Deo): clean up the table
  print(data, '***', type(data))
  RESULT_TABLE[data['trigger_id']] = data


def queue_release(trigger_id: str):
  logger.debug(f"queue_release: {trigger_id}")
  taskqueue.pop(trigger_id)
