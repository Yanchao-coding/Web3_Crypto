from fastapi import APIRouter, Request, Body
from typing import Dict, Any
from modules.config.api_config import api_config
from importlib import import_module

router = APIRouter()

@router.post("/agent/call/{func_key}")
async def agent_call(func_key: str, data: Dict[str, Any] = Body(...)):
    uid = data.get("uid", "guest")
    config = api_config.get(func_key)

    if not config:
        return {"error": "Invalid function key."}

    try:
        module = import_module(config["package"])
        func = getattr(module, config["func_name"])

        # 构造参数
        params = {}
        for k in config["param"]:
            params[k] = data.get(k)
        for hk, hv in config.get("hidden_params", {}).items():
            if hv == "$uid":
                params[hk] = uid

        result = func(**params)
        return result

    except Exception as e:
        return {"error": f"Function call failed: {str(e)}"}

@router.get("/agent/list_all_funcs")
def list_all_funcs():
    from modules.config.api_config import api_config
    return [
        {
            "func_key": key,
            "nickname": config.get("nickname"),
            "desc_prompt_chn": config.get("desc_prompt_chn"),
            "desc_prompt_eng": config.get("desc_prompt_eng"),
            "required_params": list(config.get("param", {}).keys())
        }
        for key, config in api_config.items()
    ]


@router.get("/agent/help/{func_key}")
def get_func_help(func_key: str):
    config = api_config.get(func_key)
    if not config:
        return {"error": "Invalid func_key"}
    return {
        "function": func_key,
        "description": config["desc_prompt_chn"],
        "required_params": list(config["param"].keys()),
        "hidden_params": list(config["hidden_params"].keys()),
        "example_request_body": {
            **{k: "string" for k in config["param"].keys()},
            **{k: "系统注入" for k in config["hidden_params"].keys()}
        }
    }
