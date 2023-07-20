# from confluent_kafka import Consumer, Producer
#
#
# class KafkaService:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         self.consumer = None
#         self.producer = None
#
#     def initialize_consumer(self, config):
#         if not self.consumer:
#             self.consumer = Consumer(config)
#
#     def initialize_producer(self, config):
#         if not self.producer:
#             self.producer = Producer(config)
#
#     def get_consumer(self):
#         return self.consumer
#
#     def get_producer(self):
#         return self.producer
#
#
# # Usage example
# kafka_service = KafkaService()
#
# # Initialize the consumer
# consumer_config = {
#     'bootstrap.servers': 'your_bootstrap_servers',
#     'group.id': 'your_consumer_group_id'
# }
# kafka_service.initialize_consumer(consumer_config)
#
# # Get the consumer instance
# consumer = kafka_service.get_consumer()
# # Use the consumer for consuming Kafka messages
#
# # Initialize the producer
# producer_config = {
#     'bootstrap.servers': 'your_bootstrap_servers'
# }
# kafka_service.initialize_producer(producer_config)
#
# # Get the producer instance
# producer = kafka_service.get_producer()
# # Use the producer for producing Kafka messages
