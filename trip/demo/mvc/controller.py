import sys
from model import NameModel, TimeModel
from view import GreetingView


class GreetingController:

    def __init__(self):
        self.name_model = NameModel()
        self.time_model = TimeModel()
        self.view = GreetingView()

    def handle(self, request):
        if request in self.name_model.get_name_list():
            self.view.generated_greeting(name=request, time_of_day=self.time_model.get_time_of_day(), known=True)
        else:
            self.name_model.save_name(request)
            self.view.generated_greeting(name=request, time_of_day=self.time_model.get_time_of_day(), known=False)

def main(name):
    request_handler = GreetingController()
    request_handler.handle(name)


if __name__ == "__main__":
    main(sys.argv[1])

