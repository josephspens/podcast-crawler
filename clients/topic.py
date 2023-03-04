from concurrent import futures
from typing import Callable, List
from google.cloud import pubsub_v1


def get_callback(data: str) -> Callable[[pubsub_v1.publisher.futures.Future], None]:
    """Generates a publish callback"""
    def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
        try:
            # Wait 60 seconds for the publish call to succeed.
            print(publish_future.result(timeout=10))
        except futures.TimeoutError:
            print(f"Publishing {data} timed out.")

    return callback


class Topic:
    def __init__(self, project_id, topic_id):
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(
            project_id, topic_id)

    def publish_all_blocking(self, events) -> None:
        publish_futures = self.publish_all(events)
        print(publish_futures)
        # Wait for all the publish futures to resolve before exiting.
        futures.wait(publish_futures, return_when=futures.FIRST_COMPLETED)

    def publish_all(self, events: List[str]) -> List[pubsub_v1.publisher.futures.Future]:
        return list(map(self.publish, events))

    def publish(self, event: str) -> pubsub_v1.publisher.futures.Future:
        print(event)
        # When you publish a message, the client returns a future.
        publish_future = self.publisher.publish(
            self.topic_path, event.encode("utf-8"))
        # Non-blocking. Publish failures are handled in the callback function.
        publish_future.add_done_callback(get_callback(event))
        return publish_future
