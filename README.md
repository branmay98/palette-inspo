# palette-inspo

Recolors an image using the extracted color palette of a source image from L\*a\*b\* color space k-means algorithm.

perform k-means on starting image to obtain palette
	get LAB rasterization of image
		open image and rasterize
		convert to LAB
	call k-means with minibatch

