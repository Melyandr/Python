class SetManager:

    def __len__(self):
        size = 0
        for obj in self.regular_manager:
            size += len(obj)
        return size

    def __iter__(self):
        for pen_obj in self.regular_manager:
            for pen_set in pen_obj:
                yield pen_set

    def __getitem__(self, pen_index):
        if pen_index < 0 or pen_index >= len(self):
            raise IndexError("index out of range")
        else:
            return self[pen_index]

    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

        self.general_list = []
        for pen_obj in self.regular_manager:

            for words in pen_obj.people_who_use:
                self.general_list.append(words)

    def __next__(self):
        if self.general_list.index >= len(self.general_list):
            raise StopIteration
        item = self.general_list[self.index]
        self.general_list.index += 1
        return item
