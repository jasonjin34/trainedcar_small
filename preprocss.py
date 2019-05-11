import cv2 as cv
import os

def main():
	path, dirs, files = next(os.walk('cars_train/'))
	# the number of pos car images
	num_files = len(files)
	'''resize the image fit for the cascade classifier training'''
	# for index in range
	for index in range(num_files):
		index_temp = index
		image_num = index_temp + 1
		# find the letter length
		len_image_num = len(str(image_num))

		# filename string 
		filename_string = ''
		zero_index = 0
		while zero_index < (5 - len_image_num):
			filename_string = filename_string + '0'
			zero_index += 1
		filename_string = filename_string + str(index_temp + 1) + '.jpg'
		print(filename_string)
		# image resize	
		originimage = cv.imread('cars_train/' + filename_string, 0)
		pre_size = originimage.shape
		preheight = pre_size[0]
		prewidth = pre_size[1]

		# reshape the image size to width 100 height 40
		ratio = 1.0
		ratio_width = prewidth / 100.0
		ratio_height = preheight / 40.0
		
		if ratio_width >= ratio_height:
			ratio = ratio_width
		else:
			ratio = ratio_height
		
		current_height = int(preheight / ratio)
		current_width = int(prewidth / ratio)
		resize_image = cv.resize(originimage, (current_width, current_height))
		# cv.imwrite('cars_train/' + filename_string, resize_image)

		delta_height = 40 - current_height
		delta_width = 100 - current_width
		print(delta_height, delta_width)	
		top, bottom = delta_height//2, delta_height - delta_height//2
		left, right = delta_width//2, delta_width - delta_width//2
		
		#extent boarder
		outputimage = cv.copyMakeBorder(resize_image, top, bottom, left, right, cv.BORDER_CONSTANT,0)
		cv.imwrite('cars_train/' + filename_string, outputimage)

if __name__ == "__main__":
	main()
