from modules.apis import api_funcs

api_config = {
    "get_wallet_balance": {
        "id": "a002",
        "package": "modules.apis.api_funcs",
        "func_name": "get_wallet_balance",
        "param": {"address": ""},
        "hidden_params": {"uid": "$uid"},
        "desc_prompt_eng": "Get the SOL balance of a wallet.",
        "desc_prompt_chn": "获取该钱包的sol链上余额。",
        "pretify_func": None,
        "auth_require_level": 1,
        "make_sure_notice": ["是", "否", "取消"],
        "nickname": "财务管家(智能体)"
    },
    "get_fear_greed_index": {
        "id": "a003",
        "package": "modules.apis.api_funcs",
        "func_name": "get_fear_greed_index",
        "param": {},  # 不需要用户传参
        "desc_prompt_eng": "Check current crypto fear & greed index.",
        "desc_prompt_chn": "查询当前加密市场的贪婪与恐惧指数。",
        "pretify_func": None,
        "hidden_params": {},  # 无需 uid
        "auth_require_level": 0,
        "make_sure_notice": [],
        "nickname": "情绪指数助手"
    },
    "get_token_unlock_schedule": {
        "id": "a004",
        "package": "modules.apis.api_funcs",
        "func_name": "get_token_unlock_schedule",
        "param": {"token": ""},
        "desc_prompt_eng": "Get token unlock schedule by token symbol.",
        "desc_prompt_chn": "根据币种符号查询未来的解锁时间表。",
        "pretify_func": None,
        "hidden_params": {},
        "auth_require_level": 0,
        "make_sure_notice": [],
        "nickname": "代币解锁助手"
    },
    "get_funding_info": {
        "id": "a005",
        "package": "modules.apis.api_funcs",
        "func_name": "get_funding_info",
        "param": {"project_name": ""},
        "desc_prompt_eng": "Get funding history of a crypto project.",
        "desc_prompt_chn": "查询加密项目的融资历史记录。",
        "pretify_func": None,
        "hidden_params": {},
        "auth_require_level": 0,
        "make_sure_notice": [],
        "nickname": "融资信息助手"
    }




}
