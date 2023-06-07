lines = [line.rstrip('\n') for line in open('basecomplete.txt')]

with open('link_generator.txt', 'w') as f:
    for i in range(len(lines)):
        coords = lines[i].split('|')
        f.write(f'https://www.legacysurvey.org/viewer/cutout.fits?ra={coords[0]}&dec={coords[1]}&layer=ls-dr9&pixscale=1.00&bands=grz\n')
