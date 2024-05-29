from math import ceil


class PhotoAlbum:
    PHOTO_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / cls.PHOTO_PER_PAGE))

    def add_photo(self, label):

        for page in range(len(self.photos)):

            if len(self.photos[page]) < self.PHOTO_PER_PAGE:

                self.photos[page].append(label)

                return f'{label} photo added successfully on page {page + 1} slot {len(self.photos[page])} '

        return 'No more free slots'

    def display(self):
        result = 11 * '-' + '\n'
        for pages in self.photos:
            result += ('[] ' * len(pages)).rstrip()
            result += '\n'
            result += 11 * '-' + '\n'

        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
