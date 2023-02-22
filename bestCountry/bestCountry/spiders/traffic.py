import scrapy


class QualityLife(scrapy.Spider):
    name = 'traffic'
    start_urls = [        'https://www.numbeo.com/traffic/rankings_by_country.jsp'
    ]

    # Extract data
    def parse(self, response):

        table_data = [[] for i in range(7)]

        for i in range(7):
            header = response.xpath(
                f'//*[@id="t2"]/thead/tr/th[{i + 1}]//div/text()').get()
            table_data[i].append(header)
            for j in range(84):
                rows = response.xpath(
                    f'//*[@id="t2"]/tbody/tr[{j + 1}]/td[{i+1}]/text()').getall()
                table_data[i].append(rows)

        print(table_data)
