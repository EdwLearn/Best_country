import scrapy


class QualityLife(scrapy.Spider):
    name = 'africa'
    start_urls = [
        # Africa: 'https://www..com/cost-of-living/rankings_by_country.jsp?title=2023&region=002'
        # America: 'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2023&region=019'
        # asia: 'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2023&region=142'
        # Europe: 'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2023&region=150'
        'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2023&region=009'
    ]

    # Extract data
    def parse(self, response):
        header = response.xpath('//*[@id="t2"]/tbody/tr/td[2]/text()').getall()

        print(header)