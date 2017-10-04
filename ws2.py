import bs4 as bs
import urllib

sauce = urllib.urlopen('http://www.imdb.com/chart/boxoffice').read()

soup = bs.BeautifulSoup(sauce, 'lxml')
charts = soup.findAll("table", {"class": "chart full-width"})
print charts



filename = "Movies.csv"
f = open(filename, "w")

headers = "title, weekend, gross, weeks\n"

f.write(headers)

for chart in charts:

    title_container = chart.findAll("td", {"class": "titleColumn"})
    title = title_container[0].text
    title1 = title_container[1].text
    title2 = title_container[2].text
    title3 = title_container[3].text
    title4 = title_container[4].text
    title5 = title_container[5].text
    title6 = title_container[6].text
    title7 = title_container[7].text
    title8 = title_container[8].text
    title9 = title_container[9].text

    weekend_container = chart.findAll("td", {"class": "ratingColumn"})
    weekend = weekend_container[0].text
    gross = weekend_container[1].text
    weekend1 = weekend_container[2].text
    gross1 = weekend_container[3].text
    weekend2 = weekend_container[4].text
    gross2 = weekend_container[5].text
    weekend3 = weekend_container[6].text
    gross3 = weekend_container[7].text
    weekend4 = weekend_container[8].text
    gross4 = weekend_container[9].text
    weekend5 = weekend_container[10].text
    gross5 = weekend_container[11].text
    weekend6 = weekend_container[12].text
    gross6 = weekend_container[13].text
    weekend7 = weekend_container[14].text
    gross7 = weekend_container[15].text
    weekend8 = weekend_container[16].text
    gross8 = weekend_container[17].text
    weekend9 = weekend_container[18].text
    gross9 = weekend_container[19].text

    weeks_container = chart.findAll("td", {"class": "weeksColumn"})
    weeks = weeks_container[0].text
    weeks1 = weeks_container[1].text
    weeks2 = weeks_container[2].text
    weeks3 = weeks_container[3].text
    weeks4 = weeks_container[4].text
    weeks5 = weeks_container[5].text
    weeks6 = weeks_container[6].text
    weeks7 = weeks_container[7].text
    weeks8 = weeks_container[8].text
    weeks9 = weeks_container[9].text

    print ("title:" + title + title1 + title2 + title3 + title4 + title5 + title6 + title7 + title8 + title9)
    print ("weekend:" + weekend + weekend1 + weekend2 + weekend3 + weekend4 + weekend5 + weekend6 + weekend7 + weekend8 + weekend9)
    print ("gross:" + gross + gross1 + gross2 + gross3 + gross4 + gross5 + gross6 + gross7 + gross8 + gross9)
    print ("weeks:" + weeks + weeks1 + weeks2 + weeks3 + weeks4 + weeks5 + weeks6 + weeks7 + weeks8 + weeks9)

    f.write(title +","+ weekend.replace(" ", "") +","+ gross +","+ weeks +"\n")
    f.write(title1 +","+ weekend1.replace(" ", "") +","+ gross1 +","+ weeks1 +"\n")
    f.write(title2 +","+ weekend2.replace(" ", "") +","+ gross2 +","+ weeks2 + "\n")
    f.write(title3 +","+ weekend3.replace(" ", "") +","+ gross3 +","+ weeks3 +"\n")
    f.write(title4 +","+ weekend4.replace(" ", "") +","+ gross4 +","+ weeks4 +"\n")
    f.write(title5 +","+ weekend5.replace(" ", "") +","+ gross5 +","+ weeks5 +"\n")
    f.write(title6 +","+ weekend6.replace(" ", "") +","+ gross6 +","+ weeks6 +"\n")
    f.write(title7 +","+ weekend7.replace(" ", "") +","+ gross7 +","+ weeks7 +"\n")
    f.write(title8 +","+ weekend8.replace(" ", "") +","+ gross8 +","+ weeks8 +"\n")
    f.write(title9 +","+ weekend9.replace(" ", "") +","+ gross9 +","+ weeks9 +"\n")

f.close()
