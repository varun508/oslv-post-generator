import requests
import json
import re


project = {}


def get_project_data(repo):
    _fetch_repo_meta(repo)
    _fetch(repo, 'commits')
    _fetch(repo, 'contributors')
    _fetch(repo, 'releases')
    return project


def _fetch_repo_meta(repo):
    url = 'https://api.github.com/repos/' + repo
    response = requests.get(url)
    parsed = json.loads(response.text)
    project['project_name'] = parsed['name']
    project['owner_name'] = parsed['owner']['login']
    project['stars'] = parsed['stargazers_count']
    project['issues'] = parsed['open_issues_count']
    project['forks'] = parsed['forks_count']


def _fetch(repo, to_fetch):
    url = 'https://api.github.com/repos/' + repo + '/'+to_fetch+'?per_page=1'
    response = requests.get(url)
    num = re.findall('.*"next".*page=([0-9]*).*"last".*',
                     response.headers['link'])[0]
    project[to_fetch] = num
