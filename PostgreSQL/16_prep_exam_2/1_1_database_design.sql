CREATE TABLE addresses (
   id SERIAL PRIMARY KEY,
   name VARCHAR(100) NOT NULL
);

CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL
);

CREATE TABLE clients (
    id SERIAL PRIMARY KEY ,
    full_name VARCHAR(50) NOT NULL ,
    phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE drivers (
    id SERIAL PRIMARY KEY ,
    first_name VARCHAR(30) NOT NULL ,
    last_name VARCHAR(30) NOT NULL ,
    age INT NOT NULL
        CHECK ( age > 0 ),
    rating NUMERIC(2) DEFAULT 5.5
);

CREATE TABLE cars (
    id SERIAL PRIMARY KEY ,
    make VARCHAR(20) NOT NULL ,
    model VARCHAR(20),
    year INT NOT NULL DEFAULT 0 CHECK ( year > 0 ),
    mileage INT DEFAULT 0 CHECK ( mileage > 0 ),
    condition CHAR(1) NOT NULL,
    category_id INT REFERENCES categories
                     ON DELETE CASCADE
                     ON UPDATE CASCADE
                     NOT NULL
    );

CREATE TABLE courses (
    id SERIAL PRIMARY KEY ,
    from_address_id INT REFERENCES addresses
                     ON DELETE CASCADE
                     ON UPDATE CASCADE
                     NOT NULL ,
    start TIMESTAMP NOT NULL ,
    bill NUMERIC (10,2) DEFAULT 10 CHECK ( bill>0 ),
    car_id INT REFERENCES cars
                     ON DELETE CASCADE
                     ON UPDATE CASCADE
                     NOT NULL ,
    client_id INT REFERENCES clients
                     ON UPDATE CASCADE
                     ON DELETE CASCADE
                     NOT NULL
);

CREATE TABLE cars_drivers (
    car_id INT REFERENCES cars
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
                    NOT NULL ,
    driver_id INT REFERENCES drivers
                          ON DELETE CASCADE
                          ON UPDATE CASCADE
                          NOT NULL
);
