from selenium import webdriver
import time,csv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#map_toggle=false 请求时不打开地图
url = r"https://zh.airbnb.com/s/Shenzhen--China/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&map_toggle=false&s_tag=vIkSZ4i2"

path = r"C:\Users\toshiba\Desktop\python\python爬虫开发与项目实战\租房.txt"

#不加载图片
chrome_opt = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
chrome_opt.add_experimental_option('prefs',prefs)


driver = r"D:\Program Files\chromedriver\chromedriver.exe"
browser = webdriver.Chrome(driver,chrome_options=chrome_opt)


count = 0
f = open(path,"w",encoding="utf-8")

try:
    while count <= 10:
        # 找到所有class属性为_14csrlku的标签
        browser.get(url)
        house_list = WebDriverWait(browser, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,'_14csrlku')))
        for house in house_list:
            # 在找到的标签中find
            comment = house.find_element_by_class_name('_36rlri')
            # 读取comment的所有子标签的string，这里选择前6个
            comment = comment.text[:6].replace("\n", "")
            price = house.find_element_by_class_name('_1yarz4r')
            price = price.text[5:].replace("\n", "")
            name = house.find_element_by_class_name('_190019zr')
            name = name.text.replace("\n", "")
            details = house.find_element_by_class_name("_f7heglr")
            details = details.text
            house_type = details[:4].replace("\n", "")
            house_room = details[7:].replace("\n", "")
            # print(type(comment),type(price),type(name),type(house_type),type(house_room),"\n")

            # 将数据写进txt
            row_data = comment + " " + price + " " + name + " " + house_type + " " + house_room + "\n"
            # print(row_data,type(row_data))
            f.write(row_data)
            time.sleep(0.1)
        count += 1
        print(count)
        next_page = browser.find_element_by_class_name("_b8vexar")
        next_page.click()
finally:
    browser.close()