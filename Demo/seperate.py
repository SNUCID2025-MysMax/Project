import pandas as pd
import ast


df = pd.read_csv("./Cloud_similarity/final_output_250616_filtered_result.csv", encoding='utf-8-sig')

lst = [len(ast.literal_eval(i)) for i in list(df["joi_pred_english_Qwen2.5-Coder:7B"])]
print(sum([1 for i in lst if i > 1]))
lst = [len(ast.literal_eval(i)) for i in list(df["joi_pred_Qwen2.5-Coder:7B"])]
print(sum([1 for i in lst if i > 1]))
lst = [len(ast.literal_eval(i)) for i in list(df["joi_pred_english_gpt-4.1-mini"])]
print(sum([1 for i in lst if i > 1]))
lst = [len(ast.literal_eval(i)) for i in list(df["joi_pred_gpt-4.1-mini"])]
print(sum([1 for i in lst if i > 1]))

# print(lst)