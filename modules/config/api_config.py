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
        "package": "modules.apis.api_funcs",
        "func_name": "get_token_unlock_schedule",
        "param": {},  # 无需传参
        "nickname": "Token 解锁信息查询",
        "desc_prompt_chn": "获取近期的 Token 解锁数据",
        "desc_prompt_eng": "Fetch token unlock schedule data"
    },
    "get_project_slug_dict": {
        "id": "a006",
        "package": "modules.apis.api_funcs",
        "func_name": "get_project_slug_dict",
        "param": {},
        "desc_prompt_eng": "Get all crypto project slugs.",
        "desc_prompt_chn": "获取所有加密项目的 slug 列表。",
        "pretify_func": None,
        "hidden_params": {},
        "auth_require_level": 0,
        "make_sure_notice": [],
        "nickname": "项目 slug 列表"
    },
    "get_funding_info_by_slug": {
        "id": "a007",
        "package": "modules.apis.api_funcs",
        "func_name": "get_funding_info_by_slug",
        "param": {"slug": ""},
        "desc_prompt_eng": "Get funding info by slug.",
        "desc_prompt_chn": "通过 slug 获取融资信息。",
        "pretify_func": None,
        "hidden_params": {},
        "auth_require_level": 0,
        "make_sure_notice": [],
        "nickname": "融资详情查 slug"
    }




}
