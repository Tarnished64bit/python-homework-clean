from address import Address
from mailing import Mailing

from_addr = Address("101000", "Москва", "Тверская", "11", "11")
to_addr = Address("190000", "Санкт-Петербург", "Невский проспект", "11", "11")

mail = Mailing(to_addr, from_addr, 100, "1111111111")

print("Отправление " + mail.track + " из " + mail.from_address.index + ", " +
      mail.from_address.city + ", " + mail.from_address.street + ", " +
      mail.from_address.house + " - " + mail.from_address.apartment + " в " +
      mail.to_address.index + ", " + mail.to_address.city + ", " +
      mail.to_address.street + ", " + mail.to_address.house + " - " +
      mail.to_address.apartment + ". Стоимость " + str(mail.cost) + " рублей.")