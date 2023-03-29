import main

def test_canada():
  assert main.find_PhoneNumbers("555-555-5555")
  assert main.find_PhoneNumbers("555 555 5555")
  assert main.find_PhoneNumbers("5555555555")
  assert main.find_PhoneNumbers("555 5555555")
  assert main.find_PhoneNumbers("(555) 555-5555")
  assert main.find_PhoneNumbers("(555) 555 5555")
  assert main.find_PhoneNumbers("(555) 5555555")

  assert main.find_PhoneNumbers("+1 555-555-5555")
  assert main.find_PhoneNumbers("+1 555 555 5555")
  assert main.find_PhoneNumbers("+1 5555555555")
  assert main.find_PhoneNumbers("+1 555 5555555")
  assert main.find_PhoneNumbers("+1 (555) 555-5555")
  assert main.find_PhoneNumbers("+1 (555) 555 5555")
  assert main.find_PhoneNumbers("+1 (555) 5555555")
  
  assert main.find_PhoneNumbers("+1555-555-5555")
  assert main.find_PhoneNumbers("+1555 555 5555")
  assert main.find_PhoneNumbers("+15555555555")
  assert main.find_PhoneNumbers("+1555 5555555")
  assert main.find_PhoneNumbers("+1(555) 555-5555")
  assert main.find_PhoneNumbers("+1(555) 555 5555")
  assert main.find_PhoneNumbers("+1(555) 5555555")
  
def test_NANP():
  # USA, Bermuda, Jamaica, Dominican Republic
  assert main.find_PhoneNumbers("555 5555")
  assert main.find_PhoneNumbers("5555555")
  assert main.find_PhoneNumbers("555-5555")
  assert main.find_PhoneNumbers("(555) 5555")
  
  assert main.find_PhoneNumbers("+1 555 5555")
  assert main.find_PhoneNumbers("+1 5555555")
  assert main.find_PhoneNumbers("+1 555-5555")
  assert main.find_PhoneNumbers("+1 (555) 5555")
  
  assert main.find_PhoneNumbers("+1555 5555")
  assert main.find_PhoneNumbers("+15555555")
  assert main.find_PhoneNumbers("+1555-5555")
  assert main.find_PhoneNumbers("+1(555) 5555")

  # -----------------------------------------------
  # ANTIGUA AND BARBUDA
  
  assert main.find_PhoneNumbers("+1-268 555 5555") == ["+1-268 555 5555"]
  assert main.find_PhoneNumbers("+1-268 5555555") == ["+1-268 5555555"]
  assert main.find_PhoneNumbers("+1-268 555-5555") == ["+1-268 555-5555"]
  assert main.find_PhoneNumbers("+1-268 (555) 5555") == ["+1-268 (555) 5555"]
  
  assert main.find_PhoneNumbers("+1-(268) 555 5555") == ["+1-(268) 555 5555"]
  assert main.find_PhoneNumbers("+1-(268) 5555555") == ["+1-(268) 5555555"]
  assert main.find_PhoneNumbers("+1-(268) 555-5555") == ["+1-(268) 555-5555"]
  assert main.find_PhoneNumbers("+1-(268) (555) 5555") == ["+1-(268) (555) 5555"]
  
  assert main.find_PhoneNumbers("+1 (268) 555 5555") == ["+1 (268) 555 5555"]
  assert main.find_PhoneNumbers("+1 (268) 5555555") == ["+1 (268) 5555555"]
  assert main.find_PhoneNumbers("+1 (268) 555-5555") == ["+1 (268) 555-5555"]
  assert main.find_PhoneNumbers("+1 (268) (555) 5555") == ["+1 (268) (555) 5555"]
  
  assert main.find_PhoneNumbers("+1 268 555 5555") == ["+1 268 555 5555"]
  assert main.find_PhoneNumbers("+1 268 5555555") == ["+1 268 5555555"]
  assert main.find_PhoneNumbers("+1 268 555-5555") == ["+1 268 555-5555"]
  assert main.find_PhoneNumbers("+1 268 (555) 5555") == ["+1 268 (555) 5555"]
def test_Mexico():
  # Unlike the previous ones, this test is not completely robust as there are simply too many formats a user could enter a number
  assert main.find_PhoneNumbers("4444 4444") == ["4444 4444"]
  assert main.find_PhoneNumbers("22 4444 4444") == ["22 4444 4444"]
  assert main.find_PhoneNumbers("(22) 4444-4444") == ["(22) 4444-4444"]
  assert main.find_PhoneNumbers("333 22-22") == ["333 22-22"]
  assert main.find_PhoneNumbers("333 22 22") == ["333 22 22"]
  assert main.find_PhoneNumbers("333 333 4444") == ["333 333 4444"]
  assert main.find_PhoneNumbers("(333) 333-22-22") == ["(333) 333-22-22"]
  
  assert main.find_PhoneNumbers("+52 4444 4444") == ["+52 4444 4444"]
  assert main.find_PhoneNumbers("+52 22 4444 4444") == ["+52 22 4444 4444"]
  assert main.find_PhoneNumbers("+52 (22) 4444-4444") == ["+52 (22) 4444-4444"]
  assert main.find_PhoneNumbers("+52 333 22-22") == ["+52 333 22-22"]
  assert main.find_PhoneNumbers("+52 333 22 22") == ["+52 333 22 22"]
  assert main.find_PhoneNumbers("+52 333 333 4444") == ["+52 333 333 4444"]
  assert main.find_PhoneNumbers("+52 (333) 333-22-22") == ["+52 (333) 333-22-22"]
def test_Emergency():
  assert main.find_PhoneNumbers("911")
  assert main.find_PhoneNumbers("1122") # Paksitan- Ambulance
  assert main.find_PhoneNumbers("2251-4242") # Chad- Ambulance
  assert main.find_PhoneNumbers("2251 4242") # Chad- Ambulance
  assert main.find_PhoneNumbers("772-03-73") # Comoros- Ambulance
  assert main.find_PhoneNumbers("772 03 73") # Comoros- Ambulance
  assert main.find_PhoneNumbers("442-020") # Guinea- Fire
  assert main.find_PhoneNumbers("442 020") # Guinea- Fire

def test_India():
  assert main.find_PhoneNumbers("333-7777777")
  assert main.find_PhoneNumbers("333 7777777")
  assert main.find_PhoneNumbers("55555-55555")
  assert main.find_PhoneNumbers("55555 55555")
  
  assert main.find_PhoneNumbers("(333)-7777777")
  assert main.find_PhoneNumbers("(333) 7777777")
  assert main.find_PhoneNumbers("(55555)-55555")
  assert main.find_PhoneNumbers("(55555) 55555")
  
  assert main.find_PhoneNumbers("(333)-(7777777)")
  assert main.find_PhoneNumbers("(333) (7777777)")
  assert main.find_PhoneNumbers("(55555)-(55555)")
  assert main.find_PhoneNumbers("(55555) (55555)")
  
  assert main.find_PhoneNumbers("+91 (333)-7777777")
  assert main.find_PhoneNumbers("+91 (333) 7777777")
  assert main.find_PhoneNumbers("+91 (55555)-55555")
  assert main.find_PhoneNumbers("+91 (55555) 55555")
  
  assert main.find_PhoneNumbers("+91 (333)-(7777777)")
  assert main.find_PhoneNumbers("+91 (333) (7777777)")
  assert main.find_PhoneNumbers("+91 (55555)-(55555)")
  assert main.find_PhoneNumbers("+91 (55555) (55555)")
  
  assert main.find_PhoneNumbers("+91 333-7777777")
  assert main.find_PhoneNumbers("+91 333 7777777")
  assert main.find_PhoneNumbers("+91 55555-55555")
  assert main.find_PhoneNumbers("+91 55555 55555")
def test_email():
  assert main.find_Email("plum+4535@go_mail-3.jkdirt22~~") == ["plum+4535@go_mail-3.jkdirt22~~"]