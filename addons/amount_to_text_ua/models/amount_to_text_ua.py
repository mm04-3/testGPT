
from odoo import models
from odoo.addons.base.models.res_currency import is_zero

def amount_to_text_ua(self, amount):
    # Проста реалізація для демонстрації
    units = ["", "одна", "дві", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять"]
    if is_zero(amount, self):
        return "нуль гривень 00 копійок"
    grn = int(amount)
    kop = int(round((amount - grn) * 100))
    words = []
    if grn < 10:
        words.append(units[grn])
    else:
        words.append(str(grn))
    words.append("гривень")
    words.append(f"{kop:02d} копійок")
    return " ".join(words)

models.Monetary.amount_to_text = amount_to_text_ua
