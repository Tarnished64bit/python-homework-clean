from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Samsung", "Galaxy S23", "+76948576455"))
catalog.append(Smartphone("Apple", "iPhone 15 Pro", "+79768573544"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79877600054"))
catalog.append(Smartphone("Google", "Pixel 8", "+79130888876"))
catalog.append(Smartphone("OnePlus", "11", "+79888888888"))

print("Каталог смартфонов:")

for phone in catalog:
    print(phone.brand + " - " + phone.model + ". " + phone.number)