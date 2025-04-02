import sys
import time

def progress_bar(progress, total=100):
    bar_length = 50
    filled_length = int(bar_length * progress / total)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    percentage = progress / total * 100
    
    sys.stdout.write('\r[%s] %.1f%%' % (bar, percentage))
    sys.stdout.flush()

# 设置进度为80%
progress_bar(80)