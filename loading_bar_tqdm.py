from tqdm import tqdm
import time

total = 100
with tqdm(total=total, desc='Loading', ncols=100) as pbar:
    # 直接更新到80%
    pbar.update(80)