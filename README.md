# generateToCSV

Генератор CSV-файла на Python по определенным правилам:
  в файле 7 столбцов: id, inn, kpp, name, color, translation_allowed, is_priority

  id - 17 случайных цифр, которые начинаются с 12
  inn - 12 случайных цифр
  kpp - 9 случайных цифр
  name - случайное значение из: STATE_SOURCES, INNER_BANK_SOURCES, COMPLIANCE, SBER_RATING_TOTAL
  color - слуайное значение из: R, G, Y, B
  translation_allowed - случайное 0 или 1
  is_priority - случайное 0 или 1

Плюсом сделат параметр, который будет отвечать за количество строк с данными, не считая шапки.
Разделителем должен быть ;
