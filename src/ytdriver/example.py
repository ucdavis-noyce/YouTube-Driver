from ytdriver import YTDriver


if __name__ == '__main__':
  # initialize the driver
  driver = YTDriver(browser='chrome', verbose=True)

  input()
  # search for a keyword
  for video in driver.search_videos('sports')[:1]:
    driver.play(video)
    input()

  # get upnext
  for _ in range(3):
    video = driver.get_upnext_recommendations(1)[0]
    metadata = video.get_metadata()
    print(metadata.title)
    driver.play(video)

  # get videos from the youtube homepage
  videos = driver.get_homepage_recommendations()

  # check if any videos found
  if len(videos) > 0:
    # play the top video from the homepage for 30 seconds
    driver.play(videos[0], 30)
    
  # close driver
  driver.close()
