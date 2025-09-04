import time

from urllib3.response import HTTPResponse
from urllib3.util.retry import Retry as BaseRetry


class Retry(BaseRetry):
    """
    Requests Retrier
    """

    def parse_ratelimit_retry_after(self, ratelimit_retry_after: str) -> float | None:
        """
        Parse the timestamp and return the delay before the next retry
        """
        lower_bound = float(ratelimit_retry_after)

        delay = lower_bound - time.time()
        if delay > 0:
            return delay

        return None

    def get_retry_after(self, response: HTTPResponse) -> float | None:  # type: ignore
        """
        Manage Rate-limiting headers from the server.
        Support standard header Retry-After and custom header X-RateLimit-RetryAfter
        """

        # parse Retry-After header if defined
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            return self.parse_retry_after(retry_after)

        ratelimit_retry_after = response.headers.get("X-RateLimit-RetryAfter")
        if ratelimit_retry_after:
            return self.parse_ratelimit_retry_after(ratelimit_retry_after)

        return None
