import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import math


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

url = 'https://www.statmuse.com/nba'

driver.get(url)

print('\n')
name = input('What Player: ')
print('\n\n')

driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[3]/div/astro-island/form/div[2]/div[1]/textarea').send_keys(name + " 2023 regular season games stats") 
driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[3]/div/astro-island/form/div[2]/div[1]/input').click()
time.sleep(10)
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
stats = soup.find_all(attrs={"class": "grid grid-cols-[1fr_min(1250px,_100%)_1fr] w-full px-3 md:px-[75px] [&>*]:col-span-1 [&>*]:col-start-2"})


nums = soup.find_all("tr")

counter=0
ratingList = []

for num in nums:
    if counter==25:
        break
    row_content = num.find_all("td")
    if len(row_content)==0:
        continue
    pts = float(row_content[7].text.strip())
    reb = float(row_content[8].text.strip())
    ast = float(row_content[9].text.strip())
    stl = float(row_content[10].text.strip())
    blk = float(row_content[11].text.strip())
    tov = float(row_content[12].text.strip())
    fgMakes = float(row_content[13].text.strip())
    fga = float(row_content[14].text.strip())
    fgm = float(fga-fgMakes)
    ftMakes = float(row_content[19].text.strip())
    fta = float(row_content[20].text.strip())
    ftm = float(fta-ftMakes)
    rating = pts+reb+ast+stl+blk-fgm-ftm-tov
    ratingList.append(rating)
    counter+=1

post = input('Did the player play in the post season? (True/False) ')


if post:
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/a').click()
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[3]/div/astro-island/form/div[2]/div[1]/textarea').send_keys(name + " 2023 post season game stats") 
    driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[3]/div/astro-island/form/div[2]/div[1]/input').click()
    time.sleep(10)

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    index=0
    nums = soup.find_all("tr")
    count = len(nums)-27
    index=0
    for num in nums:
        row_content = num.find_all("td")
        if index==0:
            index+=1
            continue
        if index==count:
            break
        if str(row_content[5].text.strip())=="MIL":
            index+=1
            continue
        pts = float(row_content[7].text.strip())
        reb = float(row_content[8].text.strip())
        ast = float(row_content[9].text.strip())
        stl = float(row_content[10].text.strip())
        blk = float(row_content[11].text.strip())
        tov = float(row_content[12].text.strip())
        fgMakes = float(row_content[13].text.strip())
        fga = float(row_content[14].text.strip())
        fgm = float(fga-fgMakes)
        ftMakes = float(row_content[19].text.strip())
        fta = float(row_content[20].text.strip())
        ftm = float(fta-ftMakes)
        rating = pts+reb+ast+stl+blk-fgm-ftm-tov
        ratingList.append(rating)
        index+=1

print('\n')
print(ratingList)
print('\n')

mean=sum(ratingList)/len(ratingList)
variance = sum([((x - mean) ** 2) for x in ratingList]) / len(ratingList) 
sd = variance ** 0.5

#Jimmy Butler Game 4 Player Efficeny Rating is 55.0

Zscore= (55.0-mean)/sd
Zscore = math.ceil(Zscore*100)/100
print(Zscore)
