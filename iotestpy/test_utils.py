import sys
import unittest
import time
from functools import partial

from iotestpy.utils import execute_with_retrying


class TestExecuteWithRetrying(unittest.TestCase):

    def test_successful_execution(self):
        def handle(tried):
            return tried

        def checker(result, tried, exception=None):
            return result == 1

        result = execute_with_retrying(handle=handle, checker=checker, max_tries=3)
        self.assertEqual(result, 1)

    def test_retry_until_success(self):
        attempts = [0]

        def handle(tried):
            attempts[0] += 1
            if attempts[0] < 3:
                raise Exception("Simulated failure")
            return "Success"

        def checker(result, tried, exception):
            return result == "Success"

        result = execute_with_retrying(handle=handle, checker=checker, max_tries=3)
        self.assertEqual(result, "Success")
        self.assertEqual(attempts[0], 3)

    def test_max_retries_reached_3_times(self):
        attempts = [0]

        def handle(tried):
            attempts[0] += 1
            return f"Attempt {attempts[0]}"

        result = execute_with_retrying(handle=handle, checker=lambda result, tried, exception: False,
                                       on_failure=lambda result: result,
                                       max_tries=3)
        self.assertEqual(result, "Attempt 3")
        self.assertEqual(attempts[0], 3)

    def test_unlimited_retries(self):
        attempts = [0]

        def handle(tried):
            attempts[0] += 1
            if attempts[0] < 10:
                return f"Attempt {attempts[0]}"
            return "Success"

        def checker(result, tried, exception=None):
            return result == "Success"

        result = execute_with_retrying(handle=handle, checker=checker, max_tries=sys.maxsize)
        self.assertEqual(result, "Success")
        self.assertEqual(attempts[0], 10)

    def test_infinite_retry_with_timeout(self):
        start_time = time.time()
        max_execution_time = 5  # 5 seconds timeout
        attempts = [0]
        job_status = ['RUNNING']

        def __wait_job_finished(tried=1, **kwargs):
            attempts[0] += 1
            if job_status[0] == 'SUCCEEDED':
                return {"status": "SUCCEEDED", "result": "Job completed"}
            elif time.time() - start_time > max_execution_time:
                job_status[0] = 'TIMEOUT'
                raise Exception("Job timed out")
            return {"status": "RUNNING", "progress": attempts[0]}

        def __handle_result_check(result, tried, exception=None, **kwargs):
            if exception:
                raise exception
            if result and result['status'] == 'SUCCEEDED':
                return True
            time.sleep(1)  # Simulate some processing time
            return False

        try:
            result = execute_with_retrying(
                __wait_job_finished,
                __handle_result_check,
                max_tries=1000
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            self.assertEqual(str(e), "Job timed out")
        self.assertGreater(attempts[0], 1)
        self.assertLess(time.time() - start_time, max_execution_time + 2)  # Allow 1 second margin

        # Simulate job completion
        job_status[0] = 'SUCCEEDED'
        result = execute_with_retrying(
            partial(__wait_job_finished, _job_id="test_job"),
            partial(__handle_result_check, _job_id="test_job"),
            max_tries=1000
        )
        self.assertEqual(result['status'], 'SUCCEEDED')


if __name__ == '__main__':
    unittest.main()
