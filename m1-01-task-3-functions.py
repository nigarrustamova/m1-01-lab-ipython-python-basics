def to_float(value):
    try:
        return float(value)
    except:
        return None

def clean_version(text):
    if not isinstance(text, str):
        return None
    return text.strip().lower()