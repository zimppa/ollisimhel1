-- Helenen taulu joka löytyy Azuressa
CREATE TABLE time_management (
  id SERIAL PRIMARY KEY,
  startTime TIMESTAMP NOT NULL,
  endTime TIMESTAMP NOT NULL,
  lunchBreak INTEGER,
  consultantName VARCHAR(50) NOT NULL,
  customerName VARCHAR(50) NOT NULL
);

insert into time_management (startTime, endTime, lunchBreak, consultantName, customerName) values ('2024-06-02T10:00:00', '2024-06-02T18:00:00', 45, 'Jane Smith', 'Beta Inc');