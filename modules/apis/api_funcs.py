import httpx
from datetime import datetime
import requests


HELIUS_API_KEY = "38a192c2-ea6e-49e9-a177-e3b124d7b026"

def get_wallet_balance(uid: str, address: str):
    try:
        url = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"
        payload = {
            "jsonrpc": "2.0",
            "id": "1",
            "method": "getBalance",
            "params": [address]
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()
        lamports = data.get("result", {}).get("value", 0)
        sol_balance = lamports / 1e9

        return {
            "status": "success",
            "balance": sol_balance,
            "uid": uid,
            "address": address
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }




def get_fear_greed_index():
    try:
        response = httpx.get("https://api.alternative.me/fng/")
        response.raise_for_status()

        data = response.json()
        item = data["data"][0]

        # 转换时间戳为 ISO 格式时间
        timestamp = datetime.utcfromtimestamp(int(item["timestamp"])).isoformat() + "Z"

        return {
            "status": "success",
            "index": int(item["value"]),
            "classification": item["value_classification"],
            "timestamp": timestamp
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time

# 你的 ChromeDriver 路径
CHROME_DRIVER_PATH = r"D:\TYC\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# 映射 token 到 URL path
TOKEN_URL_MAP = {
    "ARB": "arbitrum",
    "APT": "aptos",
    "OP": "optimism",
    "SUI": "sui",
    "DYDX": "dydx",
    "BLUR": "blur",
    "APE": "apecoin"
}


def get_token_unlock_schedule(token: str):
    try:
        symbol = token.upper()
        if symbol not in TOKEN_URL_MAP:
            return {
                "status": "error",
                "message": f"暂不支持 {symbol}，请尝试 ARB、APT、OP 等主流项目"
            }

        token_path = TOKEN_URL_MAP[symbol]
        url = f"https://tokenomist.ai/{token_path}"

        # 初始化 selenium 浏览器（无头模式）
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)

        # 等待页面加载数据
        time.sleep(5)

        # 查找 unlock schedule 表格
        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        unlock_schedule = []

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) < 3:
                continue

            date_str = cols[0].text.strip()
            amount_str = cols[2].text.strip().replace(",", "").replace("$", "")

            try:
                unlock_date = datetime.strptime(date_str, "%b %d, %Y")
                if unlock_date.date() < datetime.today().date():
                    continue
            except:
                continue

            try:
                amount = float(amount_str)
            except:
                continue

            unlock_schedule.append({
                "date": unlock_date.strftime("%Y-%m-%d"),
                "amount": round(amount, 2)
            })

            if len(unlock_schedule) >= 5:
                break

        driver.quit()

        return {
            "status": "success",
            "token": symbol,
            "unlock_schedule": unlock_schedule
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }



def get_funding_info(project_name: str):
    return {
        "status": "success",
        "project": project_name,
        "funding_rounds": [
            {
                "round": "Seed",
                "amount": "2M USD",
                "date": "2021-08-01",
                "investors": ["a16z", "Binance Labs"]
            },
            {
                "round": "Series A",
                "amount": "10M USD",
                "date": "2022-06-15",
                "investors": ["Sequoia", "Paradigm"]
            }
        ]
    }


