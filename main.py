import os
import re

def remove_console_log(file_path):
  with open(file_path, 'r+') as f:
    lines = f.readlines()
    lines_updated = []
    for line in lines:
      if re.search(r'console\.[a-z]+(.+)', line):
        continue
      lines_updated.append(line)
    f.seek(0)
    f.truncate()
    f.writelines(lines_updated)

def analyze_item(folder_path):
  for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if item.endswith('.tsx') and os.path.isfile(item_path):
      print("Analizando:", item_path)
      remove_console_log(item_path)
    elif os.path.isdir(item_path):
      print("Entrando en la carpeta:", item_path)
      analyze_item(item_path)
      
def main_function():
  input_path = input("\n------------\nIntroduce la ruta de la carpeta del proyecto: ")
  analyze_item(input_path)

main_function()