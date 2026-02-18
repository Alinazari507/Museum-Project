class Gallery:
    def __init__(self, name):
        self.name = name
        # Composition: An internal list to manage Exhibit objects
        self._exhibits = []

    def add_exhibit(self, title, artist):
        # We store the data as a dictionary or could even store another Object
        new_exhibit = {"title": title, "artist": artist}
        self._exhibits.append(new_exhibit)
        print(f"Added '{title}' by {artist} to the {self.name}.")

    def show_all_exhibits(self):
        print(f"\n--- {self.name} Collection ---")
        for item in self._exhibits:
            print(f"Exhibit: {item['title']} | Artist: {item['artist']}")

# Testing the Gallery
my_gallery = Gallery("Modern Art Wing")
my_gallery.add_exhibit("The Starry Night", "Vincent van Gogh")
my_gallery.add_exhibit("Guernica", "Pablo Picasso")
my_gallery.show_all_exhibits()