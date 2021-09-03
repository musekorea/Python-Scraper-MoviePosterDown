import requests
from bs4 import BeautifulSoup
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

def downloadImg(year, images):
  for idx, image in enumerate(images):
    image_src = image["src"]
    if image_src.startswith("https://search1.kakaocdn.net/thumb/R232x328"):
      image_res = requests.get(image_src)    
      image_res.raise_for_status()
      print(image_res.status_code)
      with open(f"{year}-movie{idx+1}.jpg" ,mode="wb") as file:
        file.write(image_res.content)
    else:
      continue
    if idx>=4:
      break

for year in range(2016,2021):
  url=f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
  res = requests.get(url, headers=headers)
  print(res.status_code)
  res.raise_for_status()
  soup = BeautifulSoup(res.text,"lxml")
  images = soup.find_all("img",{"class":"thumb_img"})
  downloadImg(year, images)
    


