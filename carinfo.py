f = open('cars.info', 'w+')
fbg = open('bg.txt', 'w+')

for i in range(550):
    f.write('pos/pos-' + str(i) + '.pgm 1 0 0 100 40\n')


for i in range(500):
    fbg.write('neg/neg-' + str(i) + '.pgm\n')

for i in range(500, 512):
    fbg.write('neg/neg-' + str(i) + '.pgm\n')
