CREATE DATABASE astro_feedback_portal;

CREATE TABLE `astro_feedback_portal`.`user` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `user_id` VARCHAR(1024) NULL,
    `email` VARCHAR(1024) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `astro_feedback_portal`.`review` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `review_id` VARCHAR(1024) NULL,
    `user_id` VARCHAR(1024) NULL,
    `title` VARCHAR(1024) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `astro_feedback_portal`.`review` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `review_id` VARCHAR(1024) NULL,
    `user_id` VARCHAR(1024) NULL,
    `title` VARCHAR(1024) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `astro_feedback_portal`.`review_type` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `description` VARCHAR(45) NULL,
    PRIMARY KEY (`id`)
);

INSERT INTO
    `astro_feedback_portal`.`review_type` (`description`)
VALUES
    ('Technical');

INSERT INTO
    `astro_feedback_portal`.`review_type` (`description`)
VALUES
    ('User');

INSERT INTO
    `astro_feedback_portal`.`review_type` (`description`)
VALUES
    ('Management Related');

INSERT INTO
    `astro_feedback_portal`.`review_type` (`description`)
VALUES
    ('Competitor Related');

INSERT INTO
    `astro_feedback_portal`.`review_type` (`description`)
VALUES
    ('Pricing Issue');

INSERT INTO
    `astro_feedback_portal`.`review_type` (`description`)
VALUES
    ('Customer Case Issue');