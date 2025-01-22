import os
import requests
from imdb import IMDb

def get_high_quality_thumbnail_url(low_res_url):
    if "_V1_" in low_res_url:
        high_res_url = low_res_url.split('_V1_')[0] + "_V1_.jpg"
        return high_res_url
    return low_res_url

def download_movie_thumbnail(movie_title, save_path):
    # Create an IMDb instance
    ia = IMDb()
    
    # Search for the movie
    search_results = ia.search_movie(movie_title)
    if not search_results:
        print("No movie found with the title:", movie_title)
        return 0
    
    # Get the first result (most relevant)
    movie = search_results[0]
    ia.update(movie)  # Fetch full movie details
    
    # Check if the movie has a cover URL
    if 'cover url' not in movie.keys():
        print("No thumbnail available for this movie.")
        return 0
    
    low_res_url = movie['cover url']
    high_res_url = get_high_quality_thumbnail_url(low_res_url)
    print("High-Quality Thumbnail URL:", high_res_url)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Download the thumbnail
    response = requests.get(high_res_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Thumbnail saved to {save_path}")
        return 1
    else:
        print("Failed to download the thumbnail.")
        return 0