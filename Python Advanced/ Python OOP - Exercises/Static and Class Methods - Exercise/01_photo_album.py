from math import ceil


class PhotoAlbum:
    MAXIMUM_PHOTOS_ON_ROW = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
        self.current_row_index = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.MAXIMUM_PHOTOS_ON_ROW)
        return cls(pages)

    def add_photo(self, label: str):
        try:
            if len(self.photos[self.current_row_index]) == PhotoAlbum.MAXIMUM_PHOTOS_ON_ROW:
                self.current_row_index += 1
            self.photos[self.current_row_index].append(label)

            return f"{label} photo added successfully on page " \
                   f"{self.current_row_index + 1} slot " \
                   f"{len(self.photos[self.current_row_index])})"
        except IndexError:
            return "No more free slots"

    def display(self):
        dashes = "-" * 11
        output = [dashes]
        for row in range(len(self.photos)):
            output.append(('[] ' * len(self.photos[row])).rstrip())
            output.append(dashes)

        return "\n".join(output)
