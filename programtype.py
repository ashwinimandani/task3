file=open('/home/deeplearning/fashion_mnist','r')
code=file.read()
if 'keras' or 'tensorflow' in code:
	print("keras")
else:
	print("not keras")
