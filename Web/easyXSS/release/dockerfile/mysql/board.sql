DROP DATABASE IF EXISTS `board`;
CREATE DATABASE `board`;
USE `board`;

CREATE TABLE `users`(
    `uid` int unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(20) NOT NULL,
    `password` varchar(40) NOT NULL,
    PRIMARY KEY(`uid`)
)DEFAULT CHARSET=utf8 ;

CREATE TABLE `comments`(
    `cid` int unsigned NOT NULL AUTO_INCREMENT,
    `date` datetime default CURRENT_TIMESTAMP,
    `content` varchar(4096) NOT NULL DEFAULT '',
    `uid` int unsigned NOT NULL,
    PRIMARY KEY(`cid`),
    FOREIGN KEY refer_users(`uid`)
    REFERENCES users(`uid`)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)DEFAULT CHARSET=utf8;

insert into users(`uid`, `username`, `password`) values(1, "admin", md5("admin is not administrator :-)"));
insert into comments(`content`, `uid`) 
            values("As an administrator, I will check this page every 5 minutes... My password is strong enough, so it's impossible to blast my password :-)", 1);
insert into comments(`content`, `uid`)
			values("By the way, the comments will be delete each hour.", 1);
