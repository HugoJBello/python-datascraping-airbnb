from scraper.scraper_airbnb import ScraperAirbnb


def main():
    urls=['https://www.airbnb.es/s/Madrid/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJgTwKgJcpQg0RaSKMYcHeNsQ&checkin=2018-09-13&checkout=2018-09-16&adults=1&children=0&infants=0&query=Madrid&allow_override%5B%5D=&s_tag=LJgroxv1',"https://www.airbnb.es/s/Madrid/homes?refinement_paths%5B%5D=%2Fhomes&checkin=2018-09-13&checkout=2018-09-16&adults=1&children=0&infants=0&query=Madrid&allow_override%5B%5D=&ne_lat=40.43707097660165&ne_lng=-3.6467779540030905&sw_lat=40.40660592404596&sw_lng=-3.7145306153792546&zoom=13&search_by_map=true&s_tag=aQ3E3C0h&section_offset=16"]
    checkin = "2018-09-13"
    checkout = "2018-09-16"
    scraper  = ScraperAirbnb(urls,checkin,checkout)
    scraper.get_data()


if __name__ == '__main__':
	main()
