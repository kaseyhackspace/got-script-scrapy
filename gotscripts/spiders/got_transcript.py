# -*- coding: utf-8 -*-
import scrapy
import re


class GOTTranscriptSpider(scrapy.Spider):
    name = 'gottranscript'
    download_delay = 1
    # startig URLS for season 1 to 7
    start_urls = ['https://genius.com/albums/Game-of-thrones/Season-'+str(page)+'-scripts/' for page in range(1,8)]

    def parse(self, response):
        # get a list of eppisodes
        episodes = response.css('div.chart_row-content')
        for episode in episodes:
            href = episode.css('a').attrib['href']
            # per episode, open a new request and parse it with parse_episode
            yield response.follow(href, self.parse_episode)

    def parse_episode(self, response):
        # retrieve all lines in transcript and divide per line
        lines = response.css('div.lyrics').css('p').getall()[0].split('<br>')
        # declare html-tag, parenthesis and square-parenthesis regex
        tag_cleaner = re.compile('<.*?>')
        paren_cleaner = re.compile(r'\(.*?\)')
        sqparen_cleaner = re.compile(r'\[.*?\]')
        for line in lines:
            # remove new lines
            line = line.replace('\n','')
            # remove HTML tags
            line = re.sub(tag_cleaner, '', line)
            # remove parenthesis
            line = re.sub(paren_cleaner, '', line)
            # remove square-parenthesis
            line = re.sub(sqparen_cleaner, '', line)
            # split line into character and speech
            line = line.split(':')
            if len(line) == 2:
                # yield dictionary in form {character: speech}
                yield { ' '.join(line[0].lower().split()): line[1] }

    