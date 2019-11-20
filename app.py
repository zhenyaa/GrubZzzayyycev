from grab import Grab
g = Grab(log_file='out.html')
g.go('https://www.zaycev.fm/today/rock/page/1')

print(g.doc.select('//*[@id="component"]/ul'))
com = g.doc.select('//*[@id="component"]/ul')
for i in g.doc.select('//*[@id="component"]/ul/li'):
    # print(i.html())
    print(i.select('.//div[@class="hitparad_artist"]').html())
    print(i.select('.//div[@class="hitparad_track"]').html())