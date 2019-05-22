#cv2.imshow("Redcolour",red)
	cv2.imshow("Color Tracking",img)
	#cv2.imshow("red",res)
	if cv2.waitKey(10) & 0xFF == ord('q'):
			cap.release()
			cv2.destroyAllWindows()
			break