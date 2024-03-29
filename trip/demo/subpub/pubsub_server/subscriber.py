from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer

class Subscriber(SimpleXMLRPCServer):

    def __init__(self, dispatcher, topic):
        super().__init__(("localhost", 9001))
        print("Listening on port 9001...")
        self.register_function(self.process, "process")
        self.subscribe(dispatcher, topic)


    def subscribe(self, dispatcher, topic):
        with ServerProxy(dispatcher) as dispatch:
            dispatch.subscribe("http://localhost:9001", topic)

    def process(self, message):
        print("Message: {}".format(message.get("payload", "Default message")))
        return "OK"

def main():
    subscriber_server = Subscriber("http://localhost:9000", "MessageTopic")
    subscriber_server.serve_forever(
    )

if __name__ == "__main__":
    main()