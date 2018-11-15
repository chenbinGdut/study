from selenium import webdriver
import time,csv,os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def house_crawler():
    # 不加载图片
    chrome_opt = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images': 2}
    chrome_opt.add_experimental_option('prefs', prefs)

    driver_path = r"D:\Program Files\chromedriver\chromedriver.exe"
    browser = webdriver.Chrome(driver_path, chrome_options=chrome_opt)

    count = 1
    try:
        while count <= 17:
            # 找到所有class属性为_14csrlku的标签
            browser.get(url)
            # 等待获取标签，最长等待时间为20s
            house_list = WebDriverWait(browser, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, '_14csrlku')))
            for house in house_list:
                # 找class属性为_36rlri的标签
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

                # 将数据写进csv
                row_data = [comment,price,name,details,house_type]
                writer.writerow(row_data)
                time.sleep(0.1)
            print("第%s页" % count)
            count += 1

            #点击下一页
            next_page = browser.find_element_by_class_name("_b8vexar")
            next_page.click()
    finally:
        browser.close()

if __name__ == "__main__":
    # map_toggle=false 请求时不打开地图
    url = r"https://zh.airbnb.com/s/Shenzhen--China/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&map_toggle=false&s_tag=vIkSZ4i2"

    path = os.getcwd() + "\\租房信息.csv"

    f = open(path,"w",encoding="utf-8")
    #写入csv
    writer = csv.writer(f)
    title = ["评价","价格","名字","细节","房子类型"]
    writer.writerow(title)
    house_crawler()
    f.close()

