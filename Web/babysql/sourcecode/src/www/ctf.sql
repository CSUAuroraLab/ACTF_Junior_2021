/*
 Navicat Premium Data Transfer

 Source Server         : local_mysql_phpstudy
 Source Server Type    : MySQL
 Source Server Version : 50553
 Source Host           : localhost:3306
 Source Schema         : ctf

 Target Server Type    : MySQL
 Target Server Version : 50553
 File Encoding         : 65001

 Date: 4/02/2021 14:01:02
*/

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `ctf` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `ctf`;


SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for flag
-- ----------------------------
DROP TABLE IF EXISTS `f1Ag`;
CREATE TABLE `f1Ag`  (
  `flag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flag
-- ----------------------------

INSERT INTO `f1Ag` VALUES ('ACTF{Auroraeasyeasyeasysql!}');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'Aurora', 'wuhu');
INSERT INTO `users` VALUES (2, 'QAQ', 'QWQ');
INSERT INTO `users` VALUES (3, 'stdout', 'yyds');
INSERT INTO `users` VALUES (4, '0xDktb', 'yyds');
INSERT INTO `users` VALUES (5, 'Cxlover', 'yyds');
INSERT INTO `users` VALUES (6, 'Las', 'yyds');
INSERT INTO `users` VALUES (7, 'Gstalker', 'yyds');

SET FOREIGN_KEY_CHECKS = 1;

