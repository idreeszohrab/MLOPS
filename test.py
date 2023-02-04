from wallet import wallet
def test_getAmount():
  Obj=wallet(300)
  assert Obj.getAmount==300
