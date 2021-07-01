"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = ''
        self._playing_video = False
        self._paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        # Amazing cats (amazing_cats_video_id) [#cat #animal]       
        videos = self._video_library.get_all_videos()

        video_titles = []
        for video in videos:
            video_titles.append(video.title)

        video_titles.sort()
        print("Here's a list of all available videos:")
        for title in video_titles:
            for video in videos:
                if title == video.title:
                    print(f"  {video.title} ({video.video_id}) [{' '.join(list(video.tags))}]")


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video_obj = self._video_library.get_video(video_id)
        if (self._playing_video or self._paused) and video_obj:
            self.stop_video()

        if video_obj:
            self._current_video = video_obj.title
            self._playing_video = True
            print(f"Playing video: {self._current_video}")
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self._playing_video:
            print(f"Stopping video: {self._current_video}")
            self._current_video = ''
            self._paused = False
            self._playing_video = False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self._playing_video:
            self.stop_video()

        num_videos = len(self._video_library.get_all_videos())
        random_index = random.randint(0, num_videos - 1)
        videos = self._video_library.get_all_videos()
        random_video = videos[random_index].video_id

        self.play_video(random_video)


    def pause_video(self):
        """Pauses the current video."""
        if (self._playing_video and not self._paused):
            self._paused = True
            print(f"Pausing video: {self._current_video}")
        elif self._paused:
            print(f"Video already paused: {self._current_video}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self._paused:
            print(f"Continuing video: {self._current_video}")
        else :
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        videos = self._video_library.get_all_videos()
        if self._playing_video and not self._paused:
            for video in videos:
                if(video.title == self._current_video):
                    print(f"Currently playing: {video.title} ({video.video_id}) [{' '.join(list(video.tags))}]")
        elif self._paused:
            for video in videos:
                if(video.title == self._current_video):
                    print(f"Currently playing: {video.title} ({video.video_id}) [{' '.join(list(video.tags))}] - PAUSED")
        else:
            print("No video is currently playing")



    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
