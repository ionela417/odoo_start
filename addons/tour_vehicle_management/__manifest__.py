{
    'name': 'Tour Vehicle Management',
    'version': '1.0',
    'depends': ['tour_booking'],  # sostituisci 'base' con 'tour_booking' se è il nome del modulo di prenotazioni
    'data': [
        'views/tour_vehicle_view.xml',
        'views/tour_booking_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}