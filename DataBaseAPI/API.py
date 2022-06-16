from flask import Blueprint, jsonify, request
from models import *

api = Blueprint('api', __name__)


@api.route('/add_person', methods=['POST'])
def add_person():
    person_data = request.get_json()

    new_person = Person(person_id=person_data['person_id'],
                        email=person_data['email'],
                        passwords=person_data['passwords'],
                        first_name=person_data['first_name'],
                        last_name=person_data['last_name'],
                        phone_number=person_data['phone_number'],
                        photo=person_data['photo'],
                        languages=person_data['languages'],
                        notifications=person_data['notifications'],
                        tips=person_data['tips'],
                        theme=person_data['theme'],
                        location_access=person_data['location_access'],
                        camera_access=person_data['camera_access'],
                        contact_access=person_data['contact_access'])

    db.session.add(new_person)
    db.session.commit()

    return 'Done', 201


@api.route('/get_persons')
def get_persons():
    persons_sqlalchemy_obj = Person.query.all()

    persons = []
    for person in persons_sqlalchemy_obj:
        persons.append({'person_id': person.person_id,
                        'email': person.email,
                        'passwords': person.passwords,
                        'first_name': person.first_name,
                        'last_name': person.last_name,
                        'phone_number': person.phone_number,
                        'photo': person.photo,
                        'languages': person.languages,
                        'notifications': person.notifications,
                        'tips': person.tips,
                        'theme': person.theme,
                        'location_access': person.location_access,
                        'camera_access': person.camera_access,
                        'contact_access': person.contact_access})

    return jsonify({'persons': persons})


@api.route('/add_block', methods=['POST'])
def add_block():
    block_data = request.get_json()

    new_block = Block(block_id=block_data['block_id'],
                      block_code=block_data['block_code'],
                      number_of_floors=block_data['number_of_floors'],
                      is_block_full=block_data['is_block_full'],
                      parking_lot=block_data['parking_lot'])

    db.session.add(new_block)
    db.session.commit()

    return 'Done', 201


@api.route('/get_blocks')
def get_blocks():
    block_sqlalchemy_obj = Block.query.all()

    blocks = []
    for block in block_sqlalchemy_obj:
        blocks.append({'block_id': block.block_id,
                       'block_code': block.block_code,
                       'number_of_floors': block.number_of_floors,
                       'is_block_full': block.is_block_full,
                       'parking_lot': block.parking_lot})

    return jsonify({'blocks': blocks})


@api.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    vehicle_data = request.get_json()

    new_vehicle = Vehicle(vehicle_id=vehicle_data['vehicle_id'],
                          vehicle_number=vehicle_data['vehicle_number'],
                          owner=vehicle_data['owner'])

    db.session.add(new_vehicle)
    db.session.commit()

    return 'Done', 201


@api.route('/get_vehicle')
def get_vehicle():
    vehicle_sqlalchemy_obj = Vehicle.query.all()

    vehicles = []
    for vehicle in vehicle_sqlalchemy_obj:
        vehicle.append({'vehicle_id': vehicle.vehicle_id,
                        'vehicle_number': vehicle.vehicle_number,
                        'owner': vehicle.owner})

    return jsonify({'vehicles': vehicles})


@api.route('/add_floor', methods=['POST'])
def add_floor():
    floor_data = request.get_json()

    new_floor = Floors(floor_id=floor_data['floor_id'],
                       floor_number=floor_data['floor_number'],
                       max_height_in_inch=floor_data['max_height_in_inch'],
                       number_of_wings=floor_data['number_of_wings'],
                       number_of_slots=floor_data['number_of_slots'],
                       is_floor_full=floor_data['is_floor_full'],
                       block=floor_data['block'])

    db.session.add(new_floor)
    db.session.commit()

    return 'Done', 201


@api.route('/get_floors')
def get_floors():
    floor_sqlalchemy_obj = Floors.query.all()

    floors = []
    for floor in floor_sqlalchemy_obj:
        floors.append({'floor_id': floor.floor_id,
                       'floor_number': floor.floor_number,
                       'max_height_in_inch': floor.max_height_in_inch,
                       'number_of_wings': floor.number_of_wings,
                       'number_of_slots': floor.number_of_slots,
                       'is_floor_full': floor.is_floor_full,
                       'block': floor.block})

    return jsonify({'floors': floors})


@api.route('/add_parking_pricing', methods=['POST'])
def add_parking_pricing():
    parking_pricing_data = request.get_json()

    new_parking_pricing = ParkingPricing(parking_pricing_id=parking_pricing_data['parking_pricing_id'],
                                         morning_hr_cost=parking_pricing_data['morning_hr_cost'],
                                         midday_hr_cost=parking_pricing_data['midday_hr_cost'],
                                         evening_hr_cost=parking_pricing_data['evening_hr_cost'],
                                         all_day_cost=parking_pricing_data['all_day_cost'],
                                         parking_slot=parking_pricing_data['parking_slot'])

    db.session.add(new_parking_pricing)
    db.session.commit()

    return 'Done', 201


@api.route('/get_parking_pricing')
def get_parking_pricing():
    parking_pricing_sqlalchemy_obj = ParkingPricing.query.all()

    parking_pricings = []
    for parking_pricing in parking_pricing_sqlalchemy_obj:
        parking_pricings.append({'parking_pricing_id': parking_pricing.parking_pricing_id,
                                 'morning_hr_cost': parking_pricing.morning_hr_cost,
                                 'midday_hr_cost': parking_pricing.midday_hr_cost,
                                 'evening_hr_cost': parking_pricing.evening_hr_cost,
                                 'all_day_cost': parking_pricing.all_day_cost,
                                 'parking_slot': parking_pricing.parking_slot})

    return jsonify({'parking_pricings': parking_pricings})


@api.route('/add_pricing_exception', methods=['POST'])
def add_pricing_exception():
    pricing_exception_data = request.get_json()

    new_pricing_exception = PricingException(pricing_exception_id=pricing_exception_data['pricing_exception_id'],
                                             day_of_week=pricing_exception_data['day_of_week'],
                                             morning_hr_cost=pricing_exception_data['morning_hr_cost'],
                                             midday_hr_cost=pricing_exception_data['midday_hr_cost'],
                                             evening_hr_cost=pricing_exception_data['evening_hr_cost'],
                                             all_day_cost=pricing_exception_data['all_day_cost'],
                                             parking_slot=pricing_exception_data['parking_slot'])

    db.session.add(new_pricing_exception)
    db.session.commit()

    return 'Done', 201


@api.route('/get_pricing_exception')
def get_pricing_exception():
    pricing_exception_sqlalchemy_obj = PricingException.query.all()

    pricing_exceptions = []
    for pricing_exception in pricing_exception_sqlalchemy_obj:
        pricing_exceptions.append({'pricing_exception_id': pricing_exception.pricing_exception_id,
                                   'day_of_week': pricing_exception.day_of_week,
                                   'morning_hr_cost': pricing_exception.morning_hr_cost,
                                   'midday_hr_cost': pricing_exception.midday_hr_cost,
                                   'evening_hr_cost': pricing_exception.evening_hr_cost,
                                   'all_day_cost': pricing_exception.all_day_cost,
                                   'parking_slot': pricing_exception.parking_slot})

    return jsonify({'pricing_exceptions': pricing_exceptions})


@api.route('/add_slot_comments', methods=['POST'])
def add_slot_comments():
    slot_comment_data = request.get_json()

    new_slot_comment = SlotComments(slot_comments_id=slot_comment_data['slot_comments_id'],
                                    person=slot_comment_data['person'],
                                    slot_comment=slot_comment_data['slot_comment'],
                                    parking_slot=slot_comment_data['parking_slot'])

    db.session.add(new_slot_comment)
    db.session.commit()

    return 'Done', 201


@api.route('/get_slot_comments')
def get_slot_comments():
    slot_comments_sqlalchemy_obj = SlotComments.query.all()

    slot_comments = []
    for slot_comment in slot_comments_sqlalchemy_obj:
        slot_comments.append({'slot_comments_id': slot_comment.slot_comments_id,
                              'person': slot_comment.person,
                              'slot_comment': slot_comment.slot_comment,
                              'parking_slot': slot_comment.parking_slot})

    return jsonify({'slot_comments': slot_comments})


@api.route('/add_parking_slot', methods=['POST'])
def add_parking_slot():
    parking_slot_data = request.get_json()

    new_parking_slot = ParkingSlot(parking_slot_id=parking_slot_data['parking_slot_id'],
                                   floor=parking_slot_data['floor'],
                                   slot_number=parking_slot_data['slot_number'],
                                   wing_code=parking_slot_data['wing_code'],
                                   person=parking_slot_data['person'],
                                   ownership_documents=parking_slot_data['ownership_documents'])

    db.session.add(new_parking_slot)
    db.session.commit()

    return 'Done', 201


@api.route('/get_parking_slot')
def get_parking_slot():
    parking_slot_sqlalchemy_obj = ParkingSlot.query.all()

    parking_slots = []
    for parking_slot in parking_slot_sqlalchemy_obj:
        parking_slots.append({'parking_slot_id': parking_slot.parking_slot_id,
                              'floor': parking_slot.floor,
                              'slot_number': parking_slot.slot_number,
                              'wing_code': parking_slot.wing_code,
                              'person': parking_slot.person,
                              'ownership_documents': parking_slot.ownership_documents})

    return jsonify({'parking_slots': parking_slots})


@api.route('/add_parking_lot', methods=['POST'])
def add_parking_lot():
    parking_lot_data = request.get_json()

    new_parking_lot = ParkingLot(parking_lot_id=parking_lot_data['parking_lot_id'],
                                 number_of_blocks=parking_lot_data['number_of_blocks'],
                                 is_slot_available=parking_lot_data['is_slot_available'],
                                 address=parking_lot_data['address'],
                                 operating_company_name=parking_lot_data['operating_company_name'],
                                 is_reentry_allowed=parking_lot_data['is_reentry_allowed'],
                                 operating_in_night=parking_lot_data['operating_in_night'])

    db.session.add(new_parking_lot)
    db.session.commit()

    return 'Done', 201


@api.route('/get_parking_lot')
def get_parking_lot():
    parking_lot_sqlalchemy_obj = ParkingLot.query.all()

    parking_lots = []
    for parking_lot in parking_lot_sqlalchemy_obj:
        parking_lots.append({'parking_lot_id': parking_lot.parking_lot_id,
                             'number_of_blocks': parking_lot.number_of_blocks,
                             'is_slot_available': parking_lot.is_slot_available,
                             'address': parking_lot.address,
                             'operating_company_name': parking_lot.operating_company_name,
                             'is_reentry_allowed': parking_lot.is_reentry_allowed,
                             'operating_in_night': parking_lot.operating_in_night})

    return jsonify({'parking_lots': parking_lots})


@api.route('/add_parking_slip', methods=['POST'])
def add_parking_slip():
    parking_slip_data = request.get_json()

    new_parking_slip = ParkingSlip(parking_slip_id=parking_slip_data['parking_slip_id'],
                                   parking_reservation=parking_slip_data['parking_reservation'],
                                   actual_entry_time=parking_slip_data['actual_entry_time'],
                                   actual_exit_time=parking_slip_data['actual_exit_time'],
                                   basic_cost=parking_slip_data['basic_cost'],
                                   penalty=parking_slip_data['penalty'],
                                   total_cost=parking_slip_data['total_cost'],
                                   is_paid=parking_slip_data['is_paid'])

    db.session.add(new_parking_slip)
    db.session.commit()

    return 'Done', 201


@api.route('/get_parking_slip')
def get_parking_slip():
    parking_slip_sqlalchemy_obj = ParkingSlip.query.all()

    parking_slips = []
    for parking_slip in parking_slip_sqlalchemy_obj:
        parking_slips.append({'parking_slip_id': parking_slip.parking_slip_id,
                              'parking_reservation': parking_slip.parking_reservation,
                              'actual_entry_time': parking_slip.actual_entry_time,
                              'actual_exit_time': parking_slip.actual_exit_time,
                              'basic_cost': parking_slip.basic_cost,
                              'penalty': parking_slip.penalty,
                              'total_cost': parking_slip.total_cost,
                              'is_paid': parking_slip.is_paid})

    return jsonify({'parking_slips': parking_slips})


@api.route('/add_parking_reservation', methods=['POST'])
def add_parking_reservation():
    parking_reservation_data = request.get_json()

    new_parking_reservation = ParkingReservation(parking_reservation_id=parking_reservation_data['parking_reservation_id'],
                                 person=parking_reservation_data['person'],
                                 parking_slot=parking_reservation_data['parking_slot'],
                                 start_timestamp=parking_reservation_data['start_timestamp'],
                                 duration_in_minutes=parking_reservation_data['duration_in_minutes'],
                                 booking_date=parking_reservation_data['booking_date'])

    db.session.add(new_parking_reservation)
    db.session.commit()

    return 'Done', 201


@api.route('/get_parking_reservation')
def get_parking_reservation():
    parking_reservation_sqlalchemy_obj = ParkingReservation.query.all()

    parking_reservations = []
    for parking_reservation in parking_reservation_sqlalchemy_obj:
        parking_reservations.append({'parking_reservation_id': parking_reservation.parking_reservation_id,
                             'person': parking_reservation.person,
                             'parking_slot': parking_reservation.parking_slot,
                             'start_timestamp': parking_reservation.start_timestamp,
                             'duration_in_minutes': parking_reservation.duration_in_minutes,
                             'booking_date': parking_reservation.booking_date})

    return jsonify({'parking_reservations': parking_reservations})


@api.route('/add_offers', methods=['POST'])
def add_offers():
    offers_data = request.get_json()

    new_offers = ParkingReservation(
        offers_id=offers_data['offers_id'],
        parking_slot=offers_data['parking_slot'],
        issued_on=offers_data['issued_on'],
        vallied_till=offers_data['vallied_till'],
        days_of_week=offers_data['days_of_week'],
        start_time=offers_data['start_time'],
        end_time=offers_data['end_time'])

    db.session.add(new_offers)
    db.session.commit()

    return 'Done', 201


@api.route('/get_offers')
def get_offers():
    offers_sqlalchemy_obj = Offers.query.all()

    offers = []
    for offer in offers_sqlalchemy_obj:
        offers.append({'offers_id': offer.offers_id,
                       'parking_slot': offer.parking_slot,
                       'issued_on': offer.issued_on,
                       'vallied_till': offer.vallied_till,
                       'days_of_week': offer.days_of_week,
                       'start_time': offer.start_time,
                       'end_time': offer.end_time})

    return jsonify({'offers': offers})

