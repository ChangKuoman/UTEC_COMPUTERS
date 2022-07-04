from models.User import User
from models.MotherBoard import MotherBoard
from models.Component import Component
from models.Compatible import Compatible
from server.__init__ import create_app

app = create_app()

u = User(
    username='admin',
    password='aA.12345',
    role='admin'
)
u_id = u.insert()

m1 = MotherBoard(
    name='AFOX IH61-MA2',
    description='Excellent in multitasking',
    price=212.10,
    create_by=u_id
)
m1_id = m1.insert()

m2 = MotherBoard(
    name='AFOX IH81-MA2',
    description='Rambling mainstream game world',
    price=241.23,
    create_by=u_id
)
m2_id = m2.insert()

c1 = Component(
    price=169,
    name="T-FORCE VULCAN Z",
    component_type="RAM",
    description="Teamgroup, 8GB, DDR4, 3200 MHZ",
    create_by=u_id
)
c1_id = c1.insert()

c2 = Component(
    price=189,
    name="VENGEANCE LPX",
    component_type="RAM",
    description="Corsair, 8GB, DDR4, 3000 MHZ, Sin RGB, SE007",
    create_by=u_id
)
c2_id = c2.insert()

c3 = Component(
    price=130,
    name="Kingston NV1 NVMe PCIe",
    component_type="SSD",
    description="250GB (SNVS/250G)",
    create_by=u_id
)
c3_id = c3.insert()

c4 = Component(
    price=320,
    name="HP EX900 Pro M.2",
    component_type="SSD",
    description="512MB, PCIe Gen3.0 x4 NVMe 1.3",
    create_by=u_id
)
c4_id = c4.insert()

c5 = Component(
    price=500,
    name="HD TOSHIBA S300",
    component_type="HDD",
    description="2TB 3.5\" SATA",
    create_by=u_id
)
c5_id = c5.insert()

c6 = Component(
    price=510,
    name="HP SSD S650 2.5",
    component_type="HDD",
    description="960GB SATA III 6Gb/s",
    create_by=u_id
)
c6_id = c6.insert()

c7 = Component(
    price=1511.49,
    name="AMD Ryzen 9 5900X",
    component_type="CPU",
    description="4.8 GHz, 70 MB cache, Socket AM4",
    create_by=u_id
)
c7_id = c7.insert()

c8 = Component(
    price=1431.86,
    name="Intel Core i7-12700KF",
    component_type="CPU",
    description="LGA 1700",
    create_by=u_id
)
c8_id = c8.insert()

c9 = Component(
    price=1570.00,
    name="ASUS Dual Radeon RX 6500 XT OC",
    component_type="GPU",
    description="Edition 4GB GDDR6",
    create_by=u_id
)
c9_id = c9.insert()

c10 = Component(
    price=1230.00,
    name="MSI Radeon RX 6500 XT MECH 2X 4G OC",
    component_type="GPU",
    description="AMD RDNA 2",
    create_by=u_id
)
c10_id = c10.insert()

c11 = Component(
    price=44,
    name="PSU ADVANCE 600W",
    component_type="PSU",
    description="There is no description for this product",
    create_by=u_id
)
c11_id = c11.insert()

c12 = Component(
    price=150.00,
    name="COOLERMASTER ELITEV3 600W",
    component_type="PSU",
    description="There is no description for this product",
    create_by=u_id
)
c12_id = c12.insert()

c13 = Component(
    price=725.00,
    name="COOLER MSI CORELIQUID C240 EVP",
    component_type="PC Cooling",
    description="There is no description for this product",
    create_by=u_id
)
c13_id = c13.insert()

c14 = Component(
    price=935.00,
    name="LIQUID COOLER AOR WF RGB 360",
    component_type="PC Cooling",
    description="There is no description for this product",
    create_by=u_id
)
c14_id = c14.insert()

c15 = Component(
    price=230.00,
    name="MOUSE EVGA X17 GAMING USB",
    component_type="Peripheral",
    description="MOUSE EVGA X17 GAMING USB",
    create_by=u_id
)
c15_id = c15.insert()

c16 = Component(
    price=315.00,
    name="HEADSET MSI IMMERSE GH50",
    component_type="Peripheral",
    description="HEADSET MSI IMMERSE GH50",
    create_by=u_id
)
c16_id = c16.insert()

c17 = Component(
    price=305.00,
    name="WIRELESS KEYBOARD AND MOUSE",
    component_type="Peripheral",
    description="WIRELESS KEYBOARD AND MOUSE",
    create_by=u_id
)
c17_id = c17.insert()

c18 = Component(
    price=34.00,
    name="ACC HX MICROPHONE",
    component_type="Peripheral",
    description="ACC HX MICROPHONE",
    create_by=u_id
)
c18_id = c18.insert()

ce1 = Compatible(id_motherboard=m1_id, id_component=c1_id, create_by=u_id)
ce1.insert()
ce2 = Compatible(id_motherboard=m1_id, id_component=c2_id, create_by=u_id)
ce2.insert()
ce3 = Compatible(id_motherboard=m1_id, id_component=c3_id, create_by=u_id)
ce3.insert()
ce4 = Compatible(id_motherboard=m1_id, id_component=c4_id, create_by=u_id)
ce4.insert()
ce9 = Compatible(id_motherboard=m1_id, id_component=c9_id, create_by=u_id)
ce9.insert()
ce10 = Compatible(id_motherboard=m1_id, id_component=c10_id, create_by=u_id)
ce10.insert()
ce13 = Compatible(id_motherboard=m1_id, id_component=c13_id, create_by=u_id)
ce13.insert()
ce14 = Compatible(id_motherboard=m1_id, id_component=c14_id, create_by=u_id)
ce14.insert()
ce19 = Compatible(id_motherboard=m2_id, id_component=c1_id, create_by=u_id)
ce19.insert()
ce20 = Compatible(id_motherboard=m2_id, id_component=c3_id, create_by=u_id)
ce20.insert()
