from src.baseclasses.builder import BuilderBaseClass

from faker import Faker

fake = Faker()

"""
Common itemType generator
"""

class ItemsTypeBuilder(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.result = {}
        self.reset()

    def set_item_type(self, item_type=fake.word()):
        self.result['genre_name'] = item_type
        return self

    def reset(self):
        self.set_item_type()

    def build(self):
        return self.result
