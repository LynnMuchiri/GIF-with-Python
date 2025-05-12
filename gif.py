import imageio.v3 as iio

filenames = ['1.jpg', '4.jpg', '7.jpeg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

    iio.imwrite('hello.gif',images, duration = 500, loop = 0)