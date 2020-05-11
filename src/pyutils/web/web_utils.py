import requests

def post_request(url, data):
    return requests.post(url, data)


def put_request(url, data):
    return requests.put(url, data)


def get_request(url, data):
    return requests.get(url, data)


def delete_request(url):
    return requests.post(url)


def patch_request(url, data):
    return requests.patch(url, data)
