from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.data_length = len(data)
        self.current_product = 0

    def __next__(self):
        try:
            product = self.data[self.current_product]
        except IndexError:
            raise StopIteration()
        else:
            self.current_product += 1
            return product
