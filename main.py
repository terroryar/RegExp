from pprint import pprint
import csv
import re

contact_list_final = []
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)
pattern_tlf = r"(\+7|8)?\s*\(?\s*([4][9][5])\)?[-]?\s*(\d{3})[-]?(\d{2})[-]?(\d{2})\s*\(?([д][о][б][\.])?\s*(\d{4})?\)?"
pattern_name = r"^([А-ЯЁа-яё]+)(\s*)(,?)([А-ЯЁа-яё]+)(\s*)(,?),?([А-ЯЁа-яё]*)(,?)(,?)(,?)"
substitute_tlf = r"+7(\2)\3-\4-\5 \6\7"
substitute_name = r"\1\8\4\8\7\8"

for item in contacts_list:
  result = re.sub(pattern_name,substitute_name,(re.sub(pattern_tlf, substitute_tlf, (",".join(item)))))
  result5 = list(result.split(","))

  for item1 in contact_list_final:

    if  (",".join(item1)[:(len(item1[0])+len(item1[1])+1)]) == (",".join(result5)[:(len(result5[0])+len(result5[1])+1)]):
      count = 0

      for (item2,item3) in zip(result5,item1):

        if item3 == "":
          item3 = item2
          item1[count] = item2
        count = count + 1
      result5 = ""

    if result5 == "":
      break

  if result5 != "":
    contact_list_final.append(result5)

print("STARTTTTTTTTTT")
pprint(contact_list_final)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contact_list_final)