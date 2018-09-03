from datetime import datetime
import hashlib

class AirbnbEntryDTO:

    def __init__(self, title, prize, meters, rooms, url_scrapped, url_element, url_first_page, checkin, checkout):
        self.rooms = rooms
        self.title = title
        self.prize = prize
        self.meters = meters
        self.checkin = checkin
        self.checkout = checkout
        self.url_scraped = url_scrapped
        self.url_element = url_element
        self.url_first_page=url_first_page
        self.date = str(datetime.now())

        self.construct_id_and_clean()

    def construct_id_and_clean(self):
        hashed_url = self.get_hash_from_url_first()
        if(self.title=="" or self.title==None):
            self._id = hashed_url + "---"+ self.meters+"---" + self.date_from+"---" + self.date_to+"---"+self.prize
            self.title = hashed_url
        else:
            self._id = hashed_url + "---" + self.title + "---" + self.date_from+"---" + self.date_to+"---"+self.prize

    def get_hash_from_url_first(self):
        hash_object = hashlib.sha1(self.url_first_page.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        return hex_dig