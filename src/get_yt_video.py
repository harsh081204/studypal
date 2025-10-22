from youtubesearchpython import VideosSearch


def get_yt_video_link(query):
    videos_search = VideosSearch(query=query, limit=3)
    result = videos_search.result()
    video_titles = [video['title'] for video in result['result']]
    video_links = [video['link'] for video in result['result']]
    return video_titles, video_links


# Example usage - uncomment to test
# user_query = "Explain Adaptive Radiation"
# video_titles, video_links = get_yt_video_link(user_query)
# print(video_titles, video_links)
