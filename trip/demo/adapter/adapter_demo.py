
from third_party import WhatIHave


class ObjectAdapter(object):

    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def required_function(self):
        return self.what_i_have.provided_function_1()

    def __getattr__(self, item):
        return getattr(self.what_i_have, item)

