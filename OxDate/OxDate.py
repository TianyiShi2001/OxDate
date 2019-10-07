#!/usr/bin/env python

import requests
import lxml.etree as le
from datetime import datetime, timedelta
import math
from dateutil.parser import parse

class OxDate(object):
    _terms = {
        'Michaelmas': {
            'months': (10, 11, 12),
            'vac': 'Christmas'},
        'Hilary': {
            'months': (1, 2, 3),
            'vac': 'Easter'},
        'Trinity': {
            'months': (4, 5, 6),
            'vac': 'long'}
    }
    def __init__(self, date = datetime.now()):
        if date:
            if isinstance(date, str):
                self.date = parse(date)
            elif isinstance(date, datetime):
                self.date = date
        self.term = self.get_term()
        self.startDate, self.endDate = self.get_term_dates()
        self.vac_next = OxDate._terms[self.term]['vac']
        self.days_till_vac = self.get_days_till_vac()
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        fmt = '%A %d %B %Y'
        return f"""
            {self.date.strftime(fmt)}, week {self.wterm} of {self.term} term.
            Term starts: {self.startDate.strftime(fmt)}
            Term ends: {self.endDate.strftime(fmt)}
            Next vac: {self.vac_next} vac in {self.days_till_vac} days
        """
    def get_term(self):
        for termName, termInfo in OxDate._terms.items():
            if self.date.month in termInfo['months']:
                return termName
    def get_term_dates(self):
        html = le.HTML(requests.get('https://www.ox.ac.uk/about/facts-and-figures/dates-of-term').text)
        start, end = html.xpath(f'(//*[text()="{self.term.title()} {self.date.year}"])[1]/following-sibling::*/text()')
        def term_date_parse(date):
            return datetime.strptime(date, '%A %d %B').replace(year=self.date.year)
        start, end = term_date_parse(start), term_date_parse(end)
        return start, end
    def get_week_of_term(self):
        week = math.ceil((self.date - self.startDate)/timedelta(weeks=1)) 
        return week
    def get_days_till_vac(self):
        return (self.endDate - self.date).days


