import imageio.v3 as iio

path = ['gifs/1.jpg', 'gifs/4.jpg', 'gifs/7.jpeg']
images = []

for filename in path:
    images.append(iio.imread(filename))

    iio.imwrite('hello.gif',images, duration = 500, loop = 0)