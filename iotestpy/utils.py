import logging


def _handle(tried, **kwargs):
    return None


def _checker(result, tried, exception=None, **kwargs):
    return True


def _on_failure(result, **kwargs):
    raise Exception("Failed to execute! Result: %s" % result)


def execute_with_retrying(handle=_handle, checker=_checker, on_failure=_on_failure, max_tries=1, **kwargs):
    for tried in range(1, max_tries + 1):
        result = None
        e = None
        try:
            result = handle(tried=tried, **kwargs)
        except Exception as exc:
            e = exc
            logging.warning("Failed to execute: %s", exc)

        # The checker may also throw an exception to terminate the retry
        if checker(result=result, tried=tried, exception=e, **kwargs):
            return result

        # If it's the last try, it means we've exhausted all attempts
        if tried == max_tries:
            on_failure(result=result, **kwargs)
            return result
    return None
