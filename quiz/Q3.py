def song_playlist(songs, max_size):
    """
    You decide the best way to achieve your goal is to start with the first song in the given song list.
    If the first song doesn't fit on disk, return an empty list. If there is enough space for this song,
    add it to the playlist.

    For subsequent songs, you choose the next song such that its size on disk is smallest and that
    the song hasn't already been chosen. You do this until you cannot fit any more songs on the disk.

    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    playList = []
    songsCopy = songs[:]
    currentSize = 0

    if songsCopy[0][2] > max_size:
        return playList
    else:
        playList.append(songsCopy[0][0])
        currentSize += songsCopy[0][2]
        del songsCopy[0]

    while max_size > currentSize:
        if not songsCopy:
            break
        smallestSong = min(songsCopy, key=lambda x: x[2])
        if currentSize + smallestSong[2] > max_size:
            break
        playList.append(smallestSong[0])
        currentSize += smallestSong[2]
        songsCopy.remove(smallestSong)

    return playList
