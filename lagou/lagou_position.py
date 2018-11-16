import requests,random
import json,os
import time,csv
from setting import Settings

def get_info():
    """获取职位信息"""
    try:
        html = requests.post(url,data=params,headers=headers)
        json_data = json.loads(html.text)
        #获取json数据里面的职位信息
        results = json_data["content"]["positionResult"]["result"]
        
        for result in results:
            company_name = result["companyFullName"]
            position_name = result["positionName"]
            company_size = result["companySize"]
            finance_stage = result["financeStage"]
            company_position = result["district"]
            work_year = result["workYear"]
            education = result["education"]
            industry = "".join(result["industryLables"])
            salary = result["salary"]
            
            info = [company_name, position_name,industry,company_size,finance_stage,company_position,work_year,education,salary]
            #写入csv文件
            writer.writerow(info)
            time.sleep(0.05)

    except requests.exceptions.ConnectionError:
        pass

if __name__ == "__main__":
    city_name = "深圳"
    #文件保存地址
    path = os.getcwd() + r"\lagou{}.csv".format(city_name)
    f = open(path, "w",encoding="utf-8")
    writer = csv.writer(f)
    title = ["name","position","industry","company_size","finance_stage","location","experience","education","salary"]
    writer.writerow(title)

    #构造请求头
    headers = Settings.headers
    url = r"https://www.lagou.com/jobs/positionAjax.json?city=" + city_name

    for i in range(1,31):
        params = {
            'first':'false',
            'pn':str(i),
            'kd':'python'
        }
        get_info()
        t = random.choice([1,1.1,1.2]) + random.random()
        time.sleep(t)
        print("第%d页"%i)
    f.close()
