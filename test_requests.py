import requests
from bs4 import BeautifulSoup

def get_project_slug_dict() -> dict:
    """
    抓取项目名称和对应的 slug 字典，如 {"Bondex": "bondex", ...}
    """
    url = "https://chainbroker.io/projects/list/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": f"请求失败，状态码：{response.status_code}"}

    soup = BeautifulSoup(response.text, "html.parser")
    project_links = soup.select("a.style_cell-name__body__QGvIk")

    project_dict = {}
    for link in project_links:
        slug = link.get("href").split("/")[-2]  # /projects/bondex/ -> bondex
        name_div = link.select_one("div > div.style_cell-name__sub__LHMAg")
        if name_div:
            name = name_div.get_text(strip=True)
            project_dict[name] = slug

    return project_dict


import requests
from bs4 import BeautifulSoup

def get_funding_info_by_slug(slug: str) -> list:
    """
    给定项目 slug（如 'bondex'），返回该项目的融资信息（从 Vesting Description 表格中提取）
    """
    url = f"https://chainbroker.io/projects/{slug}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": f"请求失败，状态码：{response.status_code}"}

    soup = BeautifulSoup(response.text, "html.parser")

    # 精确定位到包含 "Stage" 表头的表格
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
            continue  # 跳过无效行

        # 提取字段
        stage = cols[0].get_text(strip=True)
        price = cols[1].get_text(strip=True)
        total_raise = cols[2].get_text(strip=True)
        valuation = cols[3].get_text(strip=True)
        vesting = cols[4].get_text(strip=True)

        result.append({
            "stage": stage,
            "price": price,
            "total_raise": total_raise,
            "valuation": valuation,
            "vesting": vesting
        })

    return result



if __name__ == "__main__":
    data = get_funding_info_by_slug("bondex")
    for entry in data:
        print(entry)

