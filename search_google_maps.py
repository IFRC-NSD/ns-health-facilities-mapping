"""
Get the locations of Red Cross locations in Germany from Google Maps API.
"""
import os
import pandas as pd
import requests_cache
import google_maps_grid_searcher

# Set up a requests cache to avoid re-running the requests
requests_cache.install_cache('google_maps_red_cross_search')

# Initialize the class, setting the country to 'Albania'
searcher = google_maps_grid_searcher.GoogleMapsGridSearcher(
    country='Germany'
)

# Display the grid generated over the search area
#searcher.display_grid('results/germany_red_cross_search/grid.html')

# Run the search, searching for 'red cross'
# 'search_type' can be 'nearby' or 'text'. 'text' provides more results.
searched_circles, results, total_requests = searcher.search(
    query='Rotes Kreuz', # Used Google translate to get 'Red Cross' in Albanian
    search_type='nearby',
    api_key=os.environ.get('GOOGLE_MAPS_API_KEY'),
)

# Display the results
searcher.display_results('results/germany_red_cross_search/results.html')

# Save the results
results_df = pd.DataFrame(results.values())
results_df.to_csv('results/germany_red_cross_search/results.csv')