# KhantoImoveisAPI
This project is a Test for Seazone https://seazone.com.br/


## SetUp
Create a Env with python 3.10 and active Env

- Add libs usindg requirements.txt, run this command with Env Active:
  - ```pip install -r requirements.txt```

- Migrate project with commands:
  - ```python manage.py migrate```

- Add fixtures to your Database:
  - ```python manage.py loaddata property.json```
  - ```python manage.py loaddata ad.json```
  - ```python manage.py loaddata reservation.json```

- For initialize project run:
  - ```python manage.py runserver```


## Routes

- Property:
  - ```http://127.0.0.1:8000/api/properties/``` **(GET)**
  - ```http://127.0.0.1:8000/api/properties/<PK>/``` **(GET, PUT, PATCH, DELETE)**
  - body:
    - ```
        {
            "name": "Apartamento na Praia",
            "num_bathrooms": 2,
            "accept_animals": false,
            "cleaning_price": 120.50,
            "gest_limit": 6,
            "activate_date": "2023-01-01T00:00:00Z",
        }


- AD:
  - ```http://127.0.0.1:8000/api/ads/``` **(GET)**
  - ```http://127.0.0.1:8000/api/ads/<PK>/``` **(GET, PUT, PATCH)**
  - body:
    - ```
        {
            "property": "45414529-e862-435c-a899-150d1db4645e",
            "platform_name": "TripAdvisor",
            "platform_tax": 2.22,
        }
- Reservation:
  - ```http://127.0.0.1:8000/api/reservations/``` **(GET)**
  - ```http://127.0.0.1:8000/api/reservations/<PK>/``` **(GET, DELETE)**
  - body:
    - ```
        {
            "ad": "a948b7bb-3fc6-46a9-917e-b365b68b8be5",
            "check_in": "2023-01-01",
            "check_out": "2023-01-02",
            "guests": 2,
            "comment": "Beautiful",
            "total_price": 102.30,
        }

