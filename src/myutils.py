import re

def preprocess_text(text):
    # 去除特殊字符
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # 修复编码
    try:
        cleaned_text = cleaned_text.encode('iso-8859-1').decode('utf-8')
    except Exception:
        pass  # 如果编码修复失败，不进行任何更改
    
    # 去除多余的空格
    cleaned_text = ' '.join(cleaned_text.split())
    
    # 转换为小写
    cleaned_text = cleaned_text.lower()
    
    return cleaned_text

# print(preprocess_text('iuank djaoid &#@'))