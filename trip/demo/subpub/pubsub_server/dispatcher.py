from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer

class Dispatcher(SimpleXMLRPCServer):

    def __init__(self):
        self.topic_subscribers = dict()
        super().__init__(("localhost", 9000))
        print("listening on port 9000...")

        self.register_function(self.subscribe, "subscribe")
        self.register_function(self.unsubscribe, "unsubscribe")
        self.register_function(self.unsubscribe_all, "unsubscribe_all")
        self.register_function(self.send, "send")

    def subscribe(self, subscriber, topic):
        print('Subscribing {} to {}'.format(subscriber, topic))
        self.topic_subscribers.setdefault(topic, set()).add(subscriber)
        return "OK"

    def unsubscribe(self, subscirber, topic):
        print('Unsubscring {} from {}'.format(subscirber, topic))
        self.topic_subscribers.setdefault(topic, set()).discard(subscirber)
        return "OK"

    def unsubscribe_all(self, topic):
        print("Unsubscribing all from {}".format(topic))
        self.topic_subscribers[topic] = set()

    def send(self, message):
        print("Sending Message: \nTopic: {}\nPayload: {}".format(
            message["topic"], message["payload"]
        ))
        for subscriber in self.topic_subscribers[message.get("topic", "all")]:
            with ServerProxy(subscriber) as subscriber_proxy:
                subscriber_proxy.process(message)
        return "OK"

def main():
    dispatcher_server = Dispatcher()
    dispatcher_server.serve_forever()

if __name__ == "__main__":
    main()

