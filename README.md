# YouTube-Driver
This package provides a high-level abstraction over selenium to allow programmatic interaction with YouTube's interface.

## Getting started
1. Install using `pip install --upgrade YouTube-Driver`.
2. The following snippet provides an overview of how to use the driver.

```
from ytdriver import YTDriver

# initialize the driver
driver = YTDriver(browser='firefox', verbose=True)

# get videos from the youtube homepage
videos = driver.get_homepage()

# play the top video from the homepage for 30 seconds
driver.play(videos[0], 30)

# get up-next video recommendations
for video in driver.get_recommendations():
  metadata = video.get_metadata()
  print(metadata['title'])

# search for a keyword
for video in driver.search_videos('sports'):
  print(video.url)
  
# close driver
driver.close()
```
