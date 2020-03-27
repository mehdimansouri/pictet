import scrapy
class NBAAttendanceSpider(scrapy.Spider):
    name = "nba_attendance_spider"
    start_urls = ['http://www.espn.com/nba/attendance/_/year/2020']
    
    def parse(self, response):
        table = '.tablehead'
        for team in response.css(table):
            row = '.tr'
            for row in team.css(row):
                cell = '.td'
                for cell in row.css(cell):
                    NAME_SELECTOR = 'h1 ::text'
                    yield {
                        'name': brickset.css().extract_first(),
                    }