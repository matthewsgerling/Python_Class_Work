# Name: Matthew Gerling
# File: vimeoApp

import logging
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def get_video_embed_url(embed_html):
    soup = BeautifulSoup(embed_html, 'html.parser')
    return soup.iframe['src']


def clean_up_video_list(video_list):
    ret_list = []
    for video in video_list:
        video['video_id'] = video['uri'].split("/")[-1]
        ret_list.append(video['name'])
        link = get_video_embed_url(video['embed']['html'])
        ret_list.append(link)
    return ret_list


def order_by_video_description(video_list, reverse=False):
    ret_list = []
    ret_unsorted = {}
    index = 0
    datetime_fmt = "%B %d, %Y at %I:%M%p"
    timestamp_key_fmt = "%Y%m%d%H%M"
    for video in video_list:
        timestamp_key = "unknown{0}".format(index)
        try:
            timestamp_key = datetime.strptime(video['description'], datetime_fmt) \
                .strftime(timestamp_key_fmt)
        except ValueError as v:
            extra = len(v.args[0].partition('unconverted data remains: ')[2])
            if extra:
                try:
                    timestamp_key = datetime.strptime(video['description'][:-extra], datetime_fmt) \
                        .strftime(timestamp_key_fmt)
                except ValueError as e:
                    pass

        ret_unsorted[timestamp_key] = video
        index += 1

    for ts in sorted(ret_unsorted.keys(), reverse=reverse):
        ret_list.append(ret_unsorted[ts])

    return ret_list


class VimeoAPI:

    def __init__(self):
        self.vimeo_token = "cb17de8438beee54d3680b061d2b3341"
        self.video_description_time_format = "%B %d, %Y at %I:%M%p"
        self.vimeo_video_fields = "uri,name,created_time,status,description,embed.html,pictures,download"

    def vimeo_api_call(self, endpoint):
        try:
            response = requests.get("https://api.vimeo.com{0}".format(endpoint),
                                    headers={
                                        'Authorization': "bearer {0}".format(self.vimeo_token)
                                    })
        except requests.RequestException as e:
            logging.exception("Vimeo API Call Failed")
            raise e

        vimeo = response.json()
        if vimeo.get('data'):
            return vimeo.get('data')
        else:
            return vimeo

    def list_folder(self, folder_name):
        video_list = []
        try:
            folders = self.vimeo_api_call("/users/116653017/projects?fields=name,uri")
            for folder in folders:
                if folder['name'].lower() == folder_name.lower():
                    video_list = self.vimeo_api_call("{0}/videos?fields={1}".format(folder['uri'],
                                                                                    self.vimeo_video_fields))
        except Exception as e:
            logging.exception("Failed to retrieve folder information from Vimeo")
            raise e

        return clean_up_video_list(video_list)

    def get_video_list(self, order="asc", query=""):
        try:
            endpoint = "/users/{0}/videos".format(os.environ['VIMEO_USER_ID'])
            endpoint += "?sort=date&direction={0}&per_page=50".format(order)
            endpoint += "&fields={0}".format(self.vimeo_video_fields)
            if query:
                endpoint += "&query={0}".format(query)
            video_list = self.vimeo_api_call(endpoint)
        except Exception as e:
            logging.exception("Failed to retrieve videos from Vimeo")
            raise e

        return clean_up_video_list(video_list)

