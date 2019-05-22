#Morphological transformation, Dilation
	kernal = np.ones((5 ,5), "uint8")

	red=cv2.dilate(red, kernal)
	res=cv2.bitwise_and(img, img, mask = red)

	blue=cv2.dilate(blue,kernal)
	res1=cv2.bitwise_and(img, img, mask = blue)

	yellow=cv2.dilate(yellow,kernal)
	res2=cv2.bitwise_and(img, img, mask = yellow)

	white = cv2.dilate(white, kernal)
	res3 = cv2.bitwise_and(img, img, mask=white)