import imageio.v3 as iio

path = ['team-pic1.png', 'team-pic2.png']
images = []

for filename in path:
    images.append(iio.imread(filename))

    iio.imwrite('new.gif',images,duration = 500, loop=0)