import httpx
from datetime import datetime
import requests
from fastapi import APIRouter
from bs4 import BeautifulSoup
from modules.config.request_config import BASE_URL, PROJECT_LIST_URL, HEADERS, TOKEN_UNLOCK_URL



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


def get_token_unlock_schedule():
    # url = "https://token.unlocks.app/"
    # headers = {
    #     "User-Agent": "Mozilla/5.0"
    # }

    try:
        response = requests.get(TOKEN_UNLOCK_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # 获取所有 token 数据行
        rows = soup.find_all("tr", class_="group cursor-pointer border-b-[1px] border-background-secondary bg-background hover:bg-[#F6E8ED] dark:border-background-dark-secondary dark:bg-background-dark hover:dark:bg-[#351226]")

        result = []
        for row in rows:
            cols = row.find_all("td")
            texts = [col.get_text(strip=True) for col in cols]

            if len(texts) >= 9:
                item = {
                    "name": texts[0],
                    "price": texts[1],
                    "24h_change": texts[2],
                    "market_cap": texts[3],
                    "circulating_supply": texts[4],
                    "released_percentage": texts[5],
                    "upcoming_unlock": texts[6],
                    "next_7d_emission": texts[7],
                }
                result.append(item)

        return {"status": "success", "data": result}

    except Exception as e:
        return {"status": "error", "message": str(e)}



def get_project_slug_dict() -> dict:
    """
    获取所有项目的名称和对应的 slug（英文路径）
    返回示例：{"Bondex": "bondex", "Sui": "sui"}
    """
    response = requests.get(PROJECT_LIST_URL, headers=HEADERS)
    if response.status_code != 200:
        return {"error": f"请求失败，状态码：{response.status_code}"}

    soup = BeautifulSoup(response.text, "html.parser")
    project_links = soup.select("a.style_cell-name__body__QGvIk")

    project_dict = {}
    for link in project_links:
        slug = link.get("href").split("/")[-2]
        name_div = link.select_one("div > div.style_cell-name__sub__LHMAg")
        if name_div:
            name = name_div.get_text(strip=True)
            project_dict[name] = slug

    return project_dict

def get_funding_info_by_slug(slug: str) -> list:
    """
    给定项目 slug（如 'bondex'），返回该项目的融资信息（从 Vesting Description 表格中提取）
    """
    url = f"{BASE_URL}/projects/{slug}/"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return {"error": f"请求失败，状态码：{response.status_code}"}

    soup = BeautifulSoup(response.text, "html.parser")

    # 精确定位包含融资信息的表格
    target_table = None
    for table in soup.find_all("table"):
        if "Stage" in table.get_text() and "Vesting Period" in table.get_text():
            target_table = table
            break

    if not target_table:
        return {"error": "未找到融资信息表格"}

    result = []
    rows = target_table.find("tbody").find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        result.append({
            "stage": cols[0].get_text(strip=True),
            "price": cols[1].get_text(strip=True),
            "total_raise": cols[2].get_text(strip=True),
            "valuation": cols[3].get_text(strip=True),
            "vesting": cols[4].get_text(strip=True)
        })

    return result
