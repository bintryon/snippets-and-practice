class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_in_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        seen_songs = set()  # To keep track of songs encountered
        current_song = self  # Start from the current song
        
        while current_song:
            if current_song in seen_songs:
                return True  # If the current song is already in the set, playlist is repeating
            
            seen_songs.add(current_song)  # Add the current song to the set
            current_song = current_song.next  # Move to the next song
        
        return False  # If no repeating pattern found, playlist is not repeating
# This modified is_in_repeating_playlist method uses a set seen_songs to track the songs encountered while traversing the playlist. It starts from the current song and iterates through the playlist by following the next attribute of each song until it finds a repeating song (indicating a loop) or reaches the end of the playlist.

# The key idea here is to keep track of the songs encountered and detect a loop by checking if the current song has already been seen. If it encounters a song that it has seen before, it returns True, indicating that the playlist is repeating. If it reaches the end of the playlist without encountering any repeats, it returns False.

# You can test this by creating a playlist and checking if it's repeating:

# Example usage
first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Another Song")

first.next_song(second)
second.next_song(third)
third.next_song(first)  # Creating a loop to test repetition

print(first.is_in_repeating_playlist())  # Output will be True, as the playlist has a repeating pattern
