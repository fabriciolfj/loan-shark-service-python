CREATE TABLE loans (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    uuid VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    salary FLOAT NOT NULL,
    birthday DATE NOT NULL,
    loan FLOAT NOT NULL,
    document FLOAT NOT NULL,
    status VARCHAR NOT NULL
);