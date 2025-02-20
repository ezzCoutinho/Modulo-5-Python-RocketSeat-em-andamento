from uuid import uuid4
from qrcode import make, save
class Pix:
  def __init__(self):
    pass

  def create_payment(self):
    bank_payment_id = uuid4

    hash_payment = f"hash_payment_{bank_payment_id}"

    img = make(hash_payment)
    img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")


    return {"bank_payment_id": "f{bank_payment_id}", "qr_code_path": f"qr_code_payment_{bank_payment_id}"}