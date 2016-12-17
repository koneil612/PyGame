DROP TABLE IF EXISTS `phonebook`;
CREATE TABLE `phonebook` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstname` TEXT NULL,
  `lastname` TEXT NULL,
  `address` TEXT NULL,
  `address2` TEXT NULL,
  `city` TEXT NULL,
  `state` TEXT NULL,
  `zip` TEXT NULL,

  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
