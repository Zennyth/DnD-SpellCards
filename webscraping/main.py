import requests
from bs4 import BeautifulSoup
import re
import json


spells_name = ["represailles-infernales"]
spells = []

for spell_name in spells_name:
  spell = {
    "lvl": "",
    "title": "",
    "class": "",
    "properties": [],
    "description": [],
    "higher-levels": []
  }
  get = requests.get(f"https://www.aidedd.org/dnd/sorts.php?vf={spell_name}")
  html = BeautifulSoup(get.content, features="html.parser").find("div", {"class": "bloc"})

  # Title
  spell["title"] = html.find("h1").getText()

  # Ecole
  ecole = html.find("div", {"class": "ecole"}).getText()
  spell["lvl"] = [int(s) for s in ecole.split() if s.isdigit()][0]
  spell["class"] = ecole

  # Properties
  for prop in html.findAll("div", attrs={'class': None}):
    name = prop.find("strong").getText()
    spell["properties"].append({
      "name": name,
      "value": prop.getText().replace(f"{name} : ", "")
    })

  # Description
  desc = html.find("div", {"class": "description"}).getText().split("Aux niveaux supérieurs. ")
  def parse(text, res):
    line_break = re.compile("\.[^\s]")
    indexes = [(m.start(0), m.end(0)) for m in re.finditer(line_break, text)]
    prev = (0, 1)
    for index in indexes:
      res.append(text[prev[1]-1:index[0]] + ".")
      prev = index
    res.append(text[prev[1]-1:len(text)-1] + ".")



  parse(desc[0], spell["description"])
  if len(desc) > 1: parse(desc[1], spell["higher-levels"])
  spells.append(spell)


with open('spells.json', 'w', encoding='utf-8') as f:
  json.dump(spells, f, ensure_ascii=False, indent=2)