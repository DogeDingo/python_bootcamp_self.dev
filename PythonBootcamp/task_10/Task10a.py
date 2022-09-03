import requests
import time
from bs4 import BeautifulSoup
import json

url = "https://theselfdev.com/community/"

# thing needed from the website:
# - Name
# - Category
# - One-line Pitch / summary
# - Image URL

def website_req():
    url = "https://theselfdev.com/community/"
    time.sleep(1)
    print(url)
    r = requests.get(url)
    # print(r.text)
    self_dev_document = BeautifulSoup(r.text, "html.parser")

    specific_member = []
    for ele_in_ccw in self_dev_document.select(".creator-card-wrapper"):
        member_dict = {}
        ele_class_name = ele_in_ccw.select_one(".name").text.strip()
        # select_one() used b/c there is only one name tag in the creator-card-wrapper
        ele_class_category = ele_in_ccw.select_one(".category").text.strip()
        ele_class_summary = ele_in_ccw.select_one(".summary").text.strip()
        # ele_class_image = ele_in_ccw.select_one("img").attrs[src]
        # for line 29 please read image_explanation.txt

        member_dict["name"] = ele_class_name
        member_dict["category"] = ele_class_category
        member_dict["summary"] = ele_class_summary

        specific_member.append(member_dict)

    return specific_member


def write_into_json(x):
    with open("community_members.json", "w", encoding="utf-8") as file:
        jsonString = json.dumps(x, indent=3)
        file.write(jsonString)



print(website_req())
write_into_json(website_req())




