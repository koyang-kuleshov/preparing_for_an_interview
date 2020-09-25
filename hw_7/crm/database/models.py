from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Categories(Base):
    """Category"""
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column('category_name',
                           String(50), nullable=False)
    category_description = Column('category_description', String(250),
                                  nullable=False)

    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description

    def __repr__(self):
        return f'{self.category_name} - {self.category_description}'


class Units(Base):
    """Units"""
    __tablename__ = 'units'
    unit_id = Column(Integer, primary_key=True)
    unit = Column('unit', String(10), nullable=False)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return self.unit


class Positions(Base):
    """Positions"""
    __tablename__ = 'positions'
    position_id = Column(Integer, primary_key=True)
    position = Column('position', String(20), nullable=False)

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return self.position


class Goods(Base):
    """Goods"""
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column('good_name', String(50), nullable=False)
    good_unit = Column('good_unit', Integer, ForeignKey('units.unit_id'))
    good_category = Column('good_category', Integer,
                           ForeignKey('categories.category_id'))

    def __init__(self, good_name):
        self.good_name = good_name

    def __repr__(self):
        return self.good_name


class Vendors(Base):
    """Vendors"""
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column('vendor_name', String(50), nullable=False)
    vendor_owner_chip_form = Column('vendor_owner_chip_form',
                                    String(50), nullable=False)
    vendor_address = Column('vendor_address', String(200), nullable=False)
    vendor_phone = Column('vendor_phone', String(20), nullable=False)
    vendor_email = Column('vendor_email', String(20), nullable=False)

    def __init__(self, vendor_name, vendor_owner_chip_form, vendor_address,
                 vendor_phone, vendor_email):
        self.vendor_name = vendor_name
        self.vendor_owner_chip_form = vendor_owner_chip_form
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_email

    def __repr__(self):
        return self.vendor_name
