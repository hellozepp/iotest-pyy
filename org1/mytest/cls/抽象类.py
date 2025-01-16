import threading
from abc import ABC, abstractmethod


class Callback(ABC):
    @abstractmethod
    def handle(self):
        pass

    def on_error(self):
        pass


import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)


class TransactionError(Exception):
    pass


class DataSourceTransactionManager:
    # 模拟 DataSourceTransactionManager 类的功能
    @contextmanager
    def transaction(self, isolation_level):
        # 开始事务
        try:
            yield
            # 提交事务
        except Exception as e:
            # 回滚事务
            raise TransactionError from e


def is_in_existing_tx():
    # 模拟检查是否在现有事务中的功能
    return False


tx_thread_local = threading.local()


def with_tx_and_retry(transaction_manager, consumer, isolation_level, retry_limit):
    in_existing_tx = False
    retry_count = 0
    try:
        in_existing_tx = is_in_existing_tx()
        if not in_existing_tx:
            tx_thread_local.tx = object()

        while True:
            try:
                return with_transaction(transaction_manager, consumer, isolation_level)
            except Exception as runtime_exception:
                exception_class_name = type(runtime_exception).__name__
                message = str(runtime_exception)
                if in_existing_tx:
                    logger.warning("failed on = %s, message = %s, and inExistingTx, will throw", exception_class_name,
                                   message)
                    raise runtime_exception
                elif retry_count < retry_limit:
                    logger.warning("failed on = %s, message = %s, retryCount = %d, will retry", exception_class_name,
                                   message, retry_count)
                    retry_count += 1
                else:
                    logger.warning("failed on = %s, message = %s, and touch retry-limit, will throw",
                                   exception_class_name, message)
                    raise runtime_exception
    finally:
        if not in_existing_tx:
            del tx_thread_local.tx


class DataIntegrityViolationError(Exception):
    pass


class ExceedMaxAllowedPacketError(Exception):
    pass


class PersistError(Exception):
    pass


def with_transaction(transaction_manager, consumer, isolation_level, before_commit, timeout):
    with transaction_manager.transaction(isolation_level, timeout):
        try:
            result = consumer.handle()
            if before_commit is not None:
                before_commit.handle()
            # 模拟事务提交
            return result
        except Exception as e:
            # 模拟事务回滚
            if isinstance(e, DataIntegrityViolationError):
                consumer.onError()
            raise PersistError("Persist messages failed") from e
