from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def get_token_unlock_schedule():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    service = Service("D:/TYC/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://tokenomist.ai/unlocks")
        time.sleep(5)  # 页面加载时间

        rows = driver.find_elements(By.XPATH, '//tr[contains(@class, "cursor-pointer")]')

        unlock_data = []

        for row in rows[:10]:  # 前10条
            tds = row.find_elements(By.TAG_NAME, 'td')

            token_name = tds[1].text.strip().split('\n')[0]
            price = tds[2].text.strip()
            market_cap = tds[4].text.strip()
            circulating = tds[5].text.strip()
            unlock_percent = tds[6].text.strip().split('\n')[0]
            countdown = ' '.join([
                span.text for span in tds[7].find_elements(By.TAG_NAME, 'span')
            ])
            unlock_amount = tds[8].text.strip().split('\n')[0]
            unlock_percent_now = tds[8].text.strip().split('\n')[1] if '\n' in tds[8].text else 'N/A'

            unlock_data.append({
                "token_name": token_name,
                "price": price,
                "market_cap": market_cap,
                "circulating": circulating,
                "unlock_percent": unlock_percent,
                "countdown": countdown,
                "unlock_amount": unlock_amount,
                "unlock_percent_now": unlock_percent_now
            })

        return unlock_data

    finally:
        driver.quit()


if __name__ == "__main__":
    data = get_token_unlock_schedule()
    for i, item in enumerate(data, 1):
        print(f"{i}. {item}")
