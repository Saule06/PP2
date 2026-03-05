
import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1. 
product_pattern = re.compile(r"\d+\.\s*(.+?)\n\d+,\d+\s*x\s*([\d\s]+,\d{2})", re.MULTILINE)
products = []
for match in product_pattern.findall(text):
    name = match[0].strip()
    price = match[1].replace(" ", "")  
    products.append({"name": name, "price": price})
#2
price_pattern = re.compile(r"\n([\d\s]+,\d{2})\nСтоимость", re.MULTILINE)
prices = [p.replace(" ", "") for p in price_pattern.findall(text)]

# 3.
total_pattern = re.compile(r"ИТОГО:\s*([\d\s]+,\d{2})")
total_match = total_pattern.search(text)
total = total_match.group(1).replace(" ", "") if total_match else None

# 4.
datetime_pattern = re.compile(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})")
datetime_match = datetime_pattern.search(text)
date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None

# 5.
payment_pattern = re.compile(r"Банковская карта:|Наличные:")
payment_match = payment_pattern.search(text)
payment_method = payment_match.group().replace(":", "") if payment_match else "Unknown"

# 6. 
receipt_data = {
    "products": products,
    "prices": prices,
    "total": total,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

# 7.
print(json.dumps(receipt_data, ensure_ascii=False, indent=4))