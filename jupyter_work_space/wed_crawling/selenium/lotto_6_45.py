import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager


def get_lotto_6_45_hist(start: int, end: int) -> list:
    """로또 당첨 번호 이력을 조회합니다.

    Args:
        start (int): 조회 범위의 시작 회차\n
        end (int): 조회 범위의 마지막 회차

    Returns:
        list: 로또 당첨 번호 리스트들을 저장한 리스트 객체\n
        예:\n
        [[3, 11, 16, 19, 21, 27, 31],\n 
         [2, 9, 13, 21, 25, 32, 42],\n 
         [1, 10, 23, 29, 33, 37, 40]]
    """

    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://dhlottery.co.kr/gameResult.do?method=byWin")

    nums = range(end, start-1, -1)
    data = []

    for num in nums:
        driver.find_element(By.ID, "dwrNoList").click()
        dropdown = driver.find_element(By.ID, "dwrNoList")
        dropdown.find_element(By.XPATH, f"//option[. = '{num}']").click()
        driver.find_element(By.ID, "searchBtn").send_keys(Keys.ENTER)
        lotto = driver.find_element(By.CSS_SELECTOR, "#article > div:nth-child(2) > div > div.win_result > div > div.num.win").text
        row = [num]
        for token in lotto.split("\n"):
            if token.isnumeric():
                row.append(int(token))
        data.append(row)        
        driver.implicitly_wait(10)

    driver.close()
    return data

def get_info() -> str:
    """lotto_6_45 모듈에서 사용 중인 selenium, webdriver_manager의 버전 정보를 제공합니다.

    Returns:
        str: selenium와 webdriver_manager의 버전 정보
    """

    # return f"selenium: {selenium.__version__}, webdriver_manager: {webdriver_manager.__version__}"
    return "selenium: {}, webdriver_manager: {}".\
            format(selenium.__version__, webdriver_manager.__version__)
    

if __name__ == "__main__":
    print(get_info())
    print()
    data = get_lotto_6_45_hist(1, 3)
    print(len(data))
    print(data)

