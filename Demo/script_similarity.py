import pandas as pd
import json, ast, requests, time, re
from datetime import datetime
from tqdm import tqdm
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Evaluation.compare_soplang_ir import compare_codes

df = pd.read_csv("./final_output_250616_filtered_result.csv", encoding='utf-8-sig')

cols = ["joi_pred_english_Qwen2.5-Coder:7B", "joi_pred_Qwen2.5-Coder:7B", "joi_pred_english_gpt-4.1-mini", "joi_pred_gpt-4.1-mini"]

def escape(raw):
    if '"code": "' not in raw:
        return raw  # 'code' 키가 없으면 이스케이프 생략
    

    try:
        before, code_and_rest = raw.split('"code": "', 1)
        code_content, after = code_and_rest.split('"}', 1)
        code_content = code_content.replace('"', '\\"')
        raw_fixed = f'{before}"code": "{code_content}"}}{after}'
        return raw_fixed
    except Exception as e:
        print(f"[escape] Parse error: {e}")
        return raw  # 또는 None/""로 대체


def fix_code_quotes(text: str) -> str:
    """
    'code' 필드의 값이 작은 따옴표로 둘러싸인 경우 이를 큰 따옴표로 교체함.
    단, 내부 따옴표는 이스케이프 처리하지 않음.
    """
    pattern = r'("code"\s*:\s*)\'(.*?)\''
    return re.sub(pattern, r'\1"\2"', text, flags=re.DOTALL)

def safe_parse(text):
    original_text = text
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        try:
            return ast.literal_eval(text)
        except Exception as e:
            text = text.replace('\\"', '"').replace('"', "'").replace("'name'", '"name"').replace("'cron'", '"cron"').replace("'period'", '"period"').replace("'code'", '"code"')
            text = text.replace('"code": \'', '"code": "')
            text = text[:-2] + '"}'
            return ast.literal_eval(text)

for i, row in tqdm(df.iterrows()):
    for col in cols:
        # print(f"[DEBUG] Row {i} GT: {row['joi_gt']}")
        gt = safe_parse(row["joi_gt"])
        if 'code' in gt:
            gt['script'] = gt.pop('code')

        if gt == {}:
            gt = {"name": "Scenario", "cron": "", "period": -1, "script": ""}
        
        gen = safe_parse(row[col])
        if len(gen)==0:
            gen = {"name": "Scenario", "cron": "", "period":-1, "script": ""}
        elif len(gen) == 1:
            gen = gen[0]
            gen['script'] = gen.pop('code')
        elif len(gen) > 1:
            gen_g = gen[0]
            gen_g['script'] = gen_g.pop('code')
            for item in gen[1:]:
                if item['cron'] == gen_g['cron'] and item['period'] == gen_g['period']:
                    gen_g['script'] += "\n" + item['code']
            gen = gen_g

        # if 'code' in gen:
        #     gen['script'] = gen.pop('code')
        # print(gt, gen)


        eval = compare_codes(gt, gen)
        total_score = eval["ast_similarity"]
        if not eval["cron_equal"]:
            total_score *= 0.5
        if not eval["period_equal"]:
            total_score *= 0.5

        print(total_score)

        num_col = col.replace("joi_pred","script_similarity")
        df.at[i, num_col] = total_score

    df.to_csv("./final_output_250616_filtered_result_all.csv", index=False, encoding='utf-8-sig')
    # # break