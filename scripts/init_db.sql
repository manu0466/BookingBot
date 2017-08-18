CREATE DATABASE booking;
CREATE USER 'booking-bot'@'localhost' IDENTIFIED BY 'botpassword';
GRANT ALL PRIVILEGES ON booking.* to 'booking-bot'@'localhost';
FLUSH PRIVILEGES;


