-- Insert a user : 

INSERT INTO users
  (firstName, lastName, userName, age, email, phone, password,
   city, street, gender, isConfirmed, confirmationCode, profileImage)
VALUES
  ('anis', 'mokhtari', 'anismokh', 20, 'anis.mokhtari2005@gmail.com', '0540199226',
   'anis123',  /* replace with your hashed password */
   'Batna', '123 Main St', 'male',
   1,                                 /* isConfirmed = true */
   '213548',                              /* no confirmation code needed */
   'default_profile.png');


-- SQL seed file for payment_methods table

INSERT INTO payment_methods (name) VALUES
('CCP'),
('Bank transfer'),
('PayPal'),
('Bank Card');

