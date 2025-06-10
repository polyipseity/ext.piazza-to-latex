from json import dump
from piazza_api import Piazza
import re

def cleanhtml(raw_html: str) -> str:
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def clean(str: str) -> str:
  return  cleanhtml(str.replace('&#43;', '+').replace('&#96;', '`').replace('\\', '\\\\').replace('&#64;', '@').replace('&amp;', '&').replace('&#34;', "''").replace('&#39;', "'").replace('&gt;', "\\textgreater{}").replace('&lt;', "\\textless{}").replace('&', '\\&').replace('#', '\\#').replace('_', '\\_').replace('$', '\\$').replace('^', '\\^{}'))

login = ["", ""]
with open("login.txt", "rt") as login_file:
  idx = 0
  for line in login_file:
    login[idx] = line.rstrip()
    idx += 1
    if idx >= 2:
      break

p = Piazza()
p.user_login(*(field or None for field in login))
class_id = input("Enter class ID: ")
course_piazza = p.network(class_id)

posts = course_piazza.iter_all_posts(sleep=1)
posts = tuple(posts)
with open("piazza-export-" + class_id + ".json", "wt") as export_file:
  dump(posts, export_file)
