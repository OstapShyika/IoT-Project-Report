from extensions import db


class Person(db.Model):
    __table_args__ = {'schema': 'person'}
    __tablename__ = 'person'

    person_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.VARCHAR(30), unique=True, nullable=False)
    passwords = db.Column(db.VARCHAR(30), unique=False, nullable=False)
    first_name = db.Column(db.VARCHAR(20), unique=False)
    last_name = db.Column(db.VARCHAR(20), unique=False)
    phone_number = db.Column(db.VARCHAR(13), unique=False)
    photo = db.Column(db.VARCHAR(50), unique=False)
    languages = db.Column(db.Enum('Ukrainian', 'English', name="language_types"), default='Ukrainian')
    notifications = db.Column(db.Boolean, default=True)
    tips = db.Column(db.Boolean, default=True)
    theme = db.Column(db.Enum('black', 'white', 'blue', 'green', name="theme_type"), default='blue')
    location_access = db.Column(db.Boolean, default=False)
    camera_access = db.Column(db.Boolean, default=False)
    contact_access = db.Column(db.Boolean, default=False)

    vehicles = db.relationship("Vehicle", "owner")
    slot_comments = db.relationship("SlotComments", "comment_by")
    parking_slots = db.relationship("ParkingSlot", "person")
    parking_reservations = db.relationship("ParkingReservation", "person")

    def __repr__(self):
        return '<User %r>' % self.person_id


class Vehicle(db.Model):
    __table_args__ = {'schema': 'person'}
    __tablename__ = 'vehicle'

    vehicle_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    vehicle_number = db.Column(db.VARCHAR(20), nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False, ondelete='CASCADE')


class Block(db.Model):
    __table_args__ = {'schema': 'parking_lot'}
    __tablename__ = 'block'

    block_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    block_code = db.Column(db.VARCHAR(3), nullable=False)
    number_of_floors = db.Column(db.Integer, nullable=False)
    is_block_full = db.Column(db.Boolean, default=False)

    parking_lot_id = db.Column(db.Integer, db.ForeignKey('parking_lot.parking_lot_id', ondelete='CASCADE'),
                               nullable=False)

    floors = db.relationship("Floors", "block")


class Floors(db.Model):
    __table_args__ = {'schema': 'parking_lot'}
    __tablename__ = 'floors'

    floor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    floor_number = db.Column(db.Integer, nullable=False)
    max_height_in_inch = db.Column(db.Integer, nullable=False)
    number_of_wings = db.Column(db.Integer, nullable=False)
    number_of_slots = db.Column(db.Integer, nullable=False)
    is_floor_full = db.Column(db.Boolean, default=False)

    block_id = db.Column(db.Integer, db.ForeignKey('block.block_id', ondelete="CASCADE"), nullable=False)

    parking_slots = db.relationship("ParkingSlot", "floor")


class ParkingPricing(db.Model):
    __table_args__ = {'schema': 'parking_lot'}
    __tablename__ = 'parking_pricing'

    parking_pricing_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    morning_hr_cost = db.Column(db.Integer, nullable=False)
    midday_hr_cost = db.Column(db.Integer, nullable=False)
    evening_hr_cost = db.Column(db.Integer, nullable=False)
    all_day_cost = db.Column(db.Integer, nullable=False)

    parking_slot_id = db.Column(db.Integer, db.ForeignKey('parking_slot.parking_slot_id', ondelete="CASCADE"),
                                nullable=False)


class PricingException(db.Model):
    __table_args__ = {'schema': 'parking_lot'}
    __tablename__ = 'pricing_exception'

    pricing_exception_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    day_of_week = db.Column(db.ARRAY(db.Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
                                             'Sunday')), nullable=False)
    morning_hr_cost = db.Column(db.Integer, nullable=False)
    midday_hr_cost = db.Column(db.Integer, nullable=False)
    evening_hr_cost = db.Column(db.Integer, nullable=False)
    all_day_cost = db.Column(db.Integer, nullable=False)

    parking_slot_id = db.Column(db.Integer, db.ForeignKey('parking_slot.parking_slot_id', ondelete="CASCADE"),
                                nullable=False)


class SlotComments(db.Model):
    __table_args__ = {'schema': 'parking_lot'}
    __tablename__ = 'slot_comments'

    slot_comments_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    slot_comment = db.Column(db.VARCHAR(1000), nullable=False)

    parking_slot = db.Column(db.Integer, db.ForeignKey('parking_slot.parking_slot_id',
                                                       ondelete="CASCADE"), nullable=False)
    writer_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete="CASCADE"), nullable=False)


class ParkingSlot(db.Model):
    __table_args__ = {'schema': 'parking_lot'}
    __tablename__ = 'parking_slot'

    parking_slot_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    slot_number = db.Column(db.Integer, nullable=False)
    wing_code = db.Column(db.CHAR(1), nullable=False)
    ownership_documents = db.Column(db.VARCHAR(255))

    floor_id = db.Column(db.Integer, db.ForeignKey('floors.floor_id', ondelete="CASCADE"), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete="CASCADE"), default=None)

    parking_pricings = db.relationship("ParkingPricing", backref="parking_slot")
    pricing_exceptions = db.relationship("PricingException", backref="parking_slot")
    slot_comments = db.relationship("SlotComments", backref="parking_slot")
    offers = db.relationship("Offers", "parking_slot")
    parking_reservations = db.relationship("ParkingReservation", "parking_slot")


class ParkingLot(db.Model):
    __table_args__ = {'schema': 'parking_lot'}
    __tablename__ = 'parking_lot'

    parking_lot_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    number_of_blocks = db.Column(db.Integer, nullable=False)
    is_slot_available = db.Column(db.Boolean, default=True)
    address = db.Column(db.VARCHAR(255), nullable=False)
    operating_company_name = db.Column(db.VARCHAR(100), default=None)
    is_reentry_allowed = db.Column(db.Boolean, default=False)
    operating_in_night = db.Column(db.Boolean, default=False)

    blocks = db.relationship("Block", "parking_lot")


class ParkingSlip(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'parking_slip'

    parking_slip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    actual_entry_time = db.Column(db.TIMESTAMP, nullable=False)
    actual_exit_time = db.Column(db.TIMESTAMP, nullable=False)
    basic_cost = db.Column(db.Integer, nullable=False)
    penalty = db.Column(db.Integer, nullable=False)
    total_cost = db.Column(db.Integer, nullable=False)
    is_paid = db.Column(db.Boolean, default=False)

    parking_reservation_id = db.Column(db.Integer, db.ForeignKey('parking_reservation.parking_reservation_id',
                                                                 ondelete="CASCADE"))


class ParkingReservation(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'parking_reservation'

    parking_reservation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_timestamp = db.Column(db.TIMESTAMP, nullable=False)
    duration_in_minutes = db.Column(db.Integer, nullable=False)
    booking_date = db.Column(db.DATE, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), ondelete='CASCADE')
    parking_slot_id = db.Column(db.Integer, db.ForeignKey('parking_slot.parking_slot_id'), ondelete='CASCADE')

    parking_slips = db.relationship("ParkingSlip", "parking_reservation")


class Offers(db.Model):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'offers'

    offers_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    issued_on = db.Column(db.DATE, nullable=False)
    vallied_till = db.Column(db.DATE, nullable=False)
    days_of_week = db.Column(db.ARRAY(db.Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
                                              'Sunday')), nullable=False)
    start_time = db.Column(db.TIME)
    end_time = db.Column(db.TIME)

    parking_slot_id = db.Column(db.Integer, db.ForeignKey('parking_slot.parking_slot_id'))