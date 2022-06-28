from app import db, MyObject

# creates all the tables
db.create_all()

laptop = MyObject('HP Laptop', 3002)
mouse = MyObject('Logitech', 4004)
cable = MyObject('Type A USB', 4003)
phone = MyObject('Android', 11.0)
bag = MyObject('Canvas', 7001)

db.session.add_all([laptop, mouse, cable, phone, bag])
db.session.commit()

print(laptop.id)
print(mouse.id)
print(bag.id)
