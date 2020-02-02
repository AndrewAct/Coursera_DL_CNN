##########  Module 1  ##########
# Convolutional Neural Network #
##          1/31/2020          #

# Deep Learninng On Large Images #

# Edge Detection Example #
# Matrix -> Filter 

# A 6 X 6 matrix 
# Operation with 1, 0, -1

# More Edge Detection #

# In summary 
# Different filter allow you to find vertical and horizontal edges 

# The folling code of Sobel Filter is from Wikipedia 
function sobel(A : as two dimensional image array)
	Gx = [-1 0 1; -2 0 2; -1 0 1]
	Gy = [-1 -2 -1; 0 0 0; 1 2 1]
	
	rows = size(A, 1)
	columns = size(A, 2)
	mag = zeros(A)

	for i=1:rows-2
		for j=1:columns-2
			S1 = sum(sum(Gx.*A(i:i+2,j:j+2)))
			S2 = sum(sum(Gy.*A(i:i+2,j:j+2)))

			mag(i+1, j+1) = sqrt(S1.^2+S2.^2)
		end for
	end for
	
	threshold = 70 %varies for application [0 255]
	output_image = max(mag, threshold)
	output_image(output_image == round(threshold)) = 0;
	return output_image
end function

# Padding #

# Shrinking output 
# Throw away information 

# Valid and same convolutions 

# Strided Convoultions # 

# Floor of Z #

# Summary of concolutions 
# n X n image 
# f X f filter 
# padding p 
# stride s 
# Output size: [(n+2p-f)/s + 1] X [(n+2p-f)/s + 1] 

# In summary 
# In concoultion n.n 
# We usually do not bother with this skipping operation 
# and technically this operation is maybe better called cross-correlation 
# but most of deep learning literature just calls it the convoultion operator 

# One Layer of Concolutional Neural Network #
# Remember: parameters and bias 
# f[l] = filter size 
# p[l] = padding 
# s[l] = stride 

# Input: n[H](l-1) X n[w]*(l-1) X n[c](l-1)
# Output: n[H](l) X n[w]*(l) X n[c](l)

# Types pf layers in a convolutional network 
# - COncolution 
# - Pooling 
# - Fully connected 

# Pooling Layers #
# Max pooling 
# Reduce number of parameters 
# Provide translation invariance 

# Average pooling 
# Summarzie the presence of features in an input image 
# <A gentle Introduction to Pooling Layers of Concolutional Neural Networks>
# (https://machinelearningmastery.com/pooling-layers-for-convolutional-neural-networks/)
# General Procedure:
# Input -> CONV 1 -> Pooling -> CONV 2 -> Pooling -> FC -> FC -> Softmax 

# Why Use CNN ? #

# parameter sharing: 
# A feature detector that is useful in one part of the image is probably useful in another part of the image 
# Sparsity of connections: 
# In each layer, each output value depends only on a small number of inputs 
