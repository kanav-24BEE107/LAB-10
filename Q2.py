print("Name : Kanav ShahPatel , Roll No.: 24BEE107")
import vobject

def create_vcard(name, email, phone, address):
    vcard = vobject.vCard()
    vcard.add('fn').value = name
    vcard.add('email').value = email
    vcard.add('tel').value = phone
    vcard.add('adr').value = vobject.vcard.Address(address)
    return vcard.serialize()

name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
address = input("Enter your address: ")

vcard_data = create_vcard(name, email, phone, address)
with open('contact.vcf', 'w') as f:
    f.write(vcard_data)
    print("Done")
