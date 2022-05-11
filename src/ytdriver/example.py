from ytdriver import YTDriver


if __name__ == '__main__':
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
