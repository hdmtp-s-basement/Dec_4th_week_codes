#!/usr/bin/env python3
from github_contributions import GithubUser
from datetime import datetime, date
import pytz

tz_NY = pytz.timezone('Asia/Kolkata')
datetime_NY = str(datetime.now(tz_NY))
print(datetime_NY)

user = GithubUser('hdmtp')
contribs = user.contributions()

contribs_2021 = user.contributions(
    start_date='2021-12-14', end_date=str(date.today()))

sc = f"**{datetime_NY[:10]}** | **{datetime_NY[11:26]}** | **{sum([day.count for day in contribs_2021.days])}**"

f = open("README.md", "a")
f.write(sc)
f.close()
