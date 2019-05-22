# Random
	white_lower = np.array([140, 140, 140], np.uint8)
	white_upper = np.array([255, 255, 255], np.uint8)


	#finding the range of red,blue and yellow color in the image
	red=cv2.inRange(hsv, red_lower, red_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
	white = cv2.inRange(hsv, white_lower, white_upper)
