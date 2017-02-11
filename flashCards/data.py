class Card:
    cardCount = 0
    
    def __init__(self, _id, img, artist, name, year, place, medium):
        self._id = _id
        self.img = img
        self.artist = artist
        self.name = name
        self.year = year
        self.place = place
        self.medium = medium

