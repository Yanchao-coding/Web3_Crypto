
# Web3_Crypto

A modular FastAPI-based backend for retrieving Web3 crypto project information from public data sources like [ChainBroker.io](https://chainbroker.io) and [Token Unlocks](https://token.unlocks.app).

## 🚀 Features

- ✅ Get all crypto project slugs from ChainBroker
- ✅ Fetch detailed funding information for any crypto project by slug
- ✅ Modular FastAPI design for scalability
- ✅ Centralized configuration for clean and maintainable codebase
- ✅ Function-level dispatch system for flexible API control

---

## 📁 Project Structure

```
Web3_Crypto/
│
├── modules/
│   ├── apis/                     # All business logic (core functions)
│   │   └── api_funcs.py
│   ├── config/                   # Configuration files
│   │   ├── api_config.py         # Function registry
│   │   └── request_config.py     # Request headers & URLs
│   └── core/                     # FastAPI routing logic
│       └── router.py
│
├── main.py                       # FastAPI app entry
├── test_requests.py              # [Ignored] Manual test script
├── test.py                       # [Ignored] Another test script
```

---

## 🛠️ API Usage

### 🔧 Function Calling (Dynamic Dispatcher)

**Endpoint**:  
```
POST /agent/call/{func_key}
```

### 📌 Example: Get Funding Info by Slug

```bash
POST /agent/call/get_funding_info_by_slug
Content-Type: application/json

{
  "slug": "bondex"
}
```

**Example Result:**

```json
[
  {
    "stage": "Seed Round",
    "price": "$0.05",
    "total_raise": "$2.75M",
    "valuation": "$50M",
    "vesting": "2.5% tge, 12 months cliff, 18 months vesting"
  },
  {
    "stage": "Public Round",
    "price": "$0.08",
    "total_raise": "$6.4M",
    "valuation": "$80M",
    "vesting": "25% tge, 12 months vesting"
  }
]
```

---

## 🔧 Local Development

### 🐍 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶ Run FastAPI App

```bash
uvicorn main:app --reload
```

Then visit:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Testing

Unit test files (`test.py`, `test_requests.py`) are **excluded from Git tracking** via `.gitignore`, but useful for manual validation.

---

## 📌 TODO

- [ ] Add caching for slug dictionary
- [ ] Add interface for Token Unlock Schedule
- [ ] Add CLI tool for batch fetching
- [ ] Add more data sources (e.g., CoinMarketCap, DeFiLlama)

---

## 📮 Contact

Maintained by **Jimi**  
Powered by 🧠 and FastAPI ⚡

---

## 📄 License

MIT License
