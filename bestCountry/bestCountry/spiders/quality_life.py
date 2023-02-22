import scrapy


class QualityLife(scrapy.Spider):
    name = 'quality'
    start_urls = [
        'https://www.numbeo.com/quality-of-life/rankings_by_country.jsp'
    ]

    # Extract data
    def parse(self, response):

        table_data = [[] for i in range(10)]

        for i in range(10):
            header = response.xpath(
                f'//*[@id="t2"]/thead/tr/th[{i + 1}]//div/text()').get()
            table_data[i].append(header)
            for j in range(84):
                rows = response.xpath(
                    f'//*[@id="t2"]/tbody/tr[{j + 1}]/td[{i+1}]/text()').getall()
                table_data[i].append(rows)

        print(table_data)
