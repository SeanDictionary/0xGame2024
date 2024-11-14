/*
 Navicat Premium Data Transfer

 Source Server         : 1
 Source Server Type    : SQLite
 Source Server Version : 3035005 (3.35.5)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3035005 (3.35.5)
 File Encoding         : 65001

 Date: 06/09/2024 20:45:55
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for flag
-- ----------------------------
DROP TABLE IF EXISTS "flag";
CREATE TABLE "flag" (
  "flag" TEXT
);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS "users";
CREATE TABLE "users" (
  "id" INTEGER,
  "username" TEXT,
  "email" TEXT,
  "phone" TEXT,
  "address" TEXT
);

-- ----------------------------
-- Records of users
-- ----------------------------
BEGIN;
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (1, '常杰宏', 'jiehong72@icloud.com', '330-072-6292', '58 Ridgewood Road');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (2, '郑宇宁', 'yzheng1983@icloud.com', '52-286-6723', '3 4-20 Kawagishicho, Mizuho Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (3, '區力申', 'auls2@gmail.com', '80-8868-5211', '4 3-803 Kusunokiajima, Kita Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (4, '小山陽太', 'koyamayota@hotmail.com', '213-536-2672', '229 Wall Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (5, '溫霆鋒', 'wtingfung@gmail.com', '10-128-4559', '171 East Wangfujing Street, Dongcheng District ');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (6, '内田陸', 'uchida7@mail.com', '(121) 213 2511', '366 Stephenson Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (7, '佐藤大地', 'sdai@mail.com', '5623 670077', '654 Osney Mead');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (8, '坂本紗良', 'sarasakamoto@hotmail.com', '7419 686846', '324 Volac Park, Grantchester Rd');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (9, '野口拓哉', 'takuyanog71@outlook.com', '212-255-5307', '261 Fifth Avenue');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (10, '侯安琪', 'houanq701@icloud.com', '145-9003-0660', '809 3rd Section Hongxing Road, Jinjiang District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (11, '橋本葵', 'hashimotoaoi1@gmail.com', '330-337-0675', '696 Collier Road');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (12, '徐天榮', 'tstinwing@icloud.com', '80-9944-7802', '1-1-7 Deshiro, Nishinari Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (13, '池田聖子', 'seikoike@gmail.com', '21-026-6595', '193 Ganlan Rd, Pudong');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (14, '韩子韬', 'hzitao3@gmail.com', '212-698-1469', '492 Wooster Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (15, '韩岚', 'lanhan@gmail.com', '760-996-3930', '304 Daxin S Rd, Daxin Shangquan, Tianhe Qu');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (16, '姜詠詩', 'chanws67@hotmail.com', '330-851-8446', '675 Ridgewood Road');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (17, '渡辺紗良', 'ssato20@icloud.com', '(121) 414 9947', '345 Stephenson Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (18, '顾安琪', 'anqi1958@gmail.com', '11-117-6627', '2-1-14 Kaminopporo 1 Jo, Atsubetsu Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (19, '陆杰宏', 'jiehlu1948@gmail.com', '330-025-7960', '629 Fern Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (20, '安藤百花', 'momokando@icloud.com', '(1865) 62 0612', '260 Little Clarendon St');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (21, '汤云熙', 'tyunxi71@outlook.com', '212-825-3676', '369 Fifth Avenue');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (22, '梁睿', 'liang7@mail.com', '838-985-6603', '319 Central Avenue');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (23, '许杰宏', 'jiehoxu@hotmail.com', '66-369-0869', '1-1-8 Deshiro, Nishinari Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (24, '陶秀英', 'tao55@gmail.com', '718-132-1547', '943 Nostrand Ave');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (25, '钟詩涵', 'szh@gmail.com', '(1223) 07 3414', '931 The Pavilion, Lammas Field, Driftway');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (26, '野村和真', 'kazuma1963@mail.com', '11-328-7515', '2-1-16 Kaminopporo 1 Jo, Atsubetsu Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (27, '前田葵', 'aoimaeda@gmail.com', '755-8141-6868', '382 Xue Yuan Yi Xiang, Longgang');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (28, '千葉絢斗', 'ayato6@icloud.com', '330-767-6759', '96 Collier Road');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (29, '苗家玲', 'miu2@outlook.com', '183-7569-3926', '136 Jiangnan West Road, Haizhu District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (30, '村田美咲', 'mism5@gmail.com', '769-5199-4540', '854 Shanhu Rd');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (31, '邱霆鋒', 'tingfungyau1017@hotmail.com', '838-320-3587', '420 State Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (32, '工藤美羽', 'kudo2@icloud.com', '213-612-9037', '166 Figueroa Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (33, '菅原七海', 'nanasugawara@yahoo.com', '3-5212-1315', '3-15-17 Ginza, Chuo-ku');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (34, '斉藤葉月', 'hazuki8@outlook.com', '28-320-3113', 'No.754, Dongsan Road, Erxianqiao, Chenghua District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (35, '薛宇宁', 'yuning2@outlook.com', '7783 573742', '20 Papworth Rd, Trumpington');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (36, '石宇宁', 'ysh1963@yahoo.com', '10-1877-2502', '632 68 Qinghe Middle St, Haidian District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (37, '叶璐', 'luye@icloud.com', '212-298-0399', '76 West Houston Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (38, '萧杰宏', 'xiaoj@hotmail.com', '330-083-2371', '775 Fern Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (39, '工藤葉月', 'hazukikudo94@yahoo.com', '5530 355960', '918 Hanover St');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (40, '野口舞', 'main@gmail.com', '11-437-2042', '2-1-3 Kaminopporo 1 Jo, Atsubetsu Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (41, '蘇慧儀', 'sowaiyee@mail.com', '213-809-9932', '125 Alameda Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (42, '吕岚', 'lu2@icloud.com', '5852 470432', '540 Earle Rd');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (43, '钟致远', 'zhong1021@gmail.com', '213-903-8448', '457 Figueroa Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (44, '中村大和', 'nakamyamato@icloud.com', '614-976-5136', '993 Wicklow Road');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (45, '金詩涵', 'js2@gmail.com', '5307 099901', '650 Papworth Rd, Trumpington');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (46, '赵宇宁', 'yuningzhao919@mail.com', '70-1511-2397', '2-3-4 Yoyogi, Shibuya-ku');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (47, '朱云熙', 'yuz@gmail.com', '(1865) 75 0913', '683 Little Clarendon St');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (48, '向頴璇', 'hewingsuen@outlook.com', '177-3061-1555', '203 Huaxia St, Jinghua Shangquan');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (49, '于晓明', 'yu1024@hotmail.com', '189-0184-3015', '674 Binchuan Rd, Minhang District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (50, '伊藤美咲', 'mito17@gmail.com', '20-092-5600', '986 Xiaoping E Rd, Baiyun ');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (51, '常震南', 'chz@outlook.com', '21-293-4937', '222 Hongqiao Rd., Xu Hui District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (52, '島田結翔', 'yuitosh5@icloud.com', '718-319-4352', '923 1st Ave');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (53, '阿部美咲', 'abmisak@outlook.com', '(1223) 71 9817', '665 Silver St, Newnham');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (54, '謝思妤', 'tseszeyu@gmail.com', '131-1510-7233', '223 W Ring Rd, Buji Town, Longgang');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (55, '武安琪', 'wanq9@hotmail.com', '90-8057-5161', '5 3-803 Kusunokiajima, Kita Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (56, '松本陽菜', 'hinamats@hotmail.com', '7837 083300', '347 The Pavilion, Lammas Field, Driftway');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (57, '韓淑怡', 'sukyeeha@icloud.com', '5074 340831', '561 Redfern St');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (58, '劉永發', 'wingfatlau1949@gmail.com', '7525 521533', '270 Lower Temple Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (59, '邹嘉伦', 'zou1993@icloud.com', '186-1302-5814', '200 Sanlitun Road, Chaoyang District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (60, '姚杰宏', 'jiehongyao2@icloud.com', '(121) 846 7709', '578 Lower Temple Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (61, '范璐', 'lufan1@mail.com', '(151) 152 6421', '480 Trafalgar Square, Charing Cross');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (62, '韩璐', 'halu2019@yahoo.com', '70-2327-3812', '2-5-20 Chitose, Atsuta Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (63, '周慧珊', 'chwaisan@mail.com', '838-282-9121', '891 Broadway');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (64, '松井瑛太', 'eitam409@mail.com', '90-6656-8141', '5-4-17 Kikusui 3 Jo, Shiroishi Ward,');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (65, '方頴思', 'wingszefo@outlook.com', '70-8721-3631', '2-5-9 Chitose, Atsuta Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (66, '戴云熙', 'daiyun7@icloud.com', '90-7874-0096', '3-15-17 Ginza, Chuo-ku');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (67, '今井舞', 'mima8@gmail.com', '838-312-9644', '732 Central Avenue');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (68, '林拓哉', 'takuyah@hotmail.com', '330-513-7162', '581 Riverview Road');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (69, '坂本大地', 'daichsakamoto@yahoo.com', '212-622-6497', '759 Fifth Avenue');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (70, '金子异', 'jinziyi@icloud.com', '3-6522-0423', '1-5-17, Higashi-Shimbashi, Minato-ku');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (71, '池田架純', 'ikekasu@icloud.com', '185-1371-2831', '994 East Wangfujing Street, Dongcheng District ');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (72, '新井美羽', 'aramiu1217@icloud.com', '5641 183314', '174 Papworth Rd, Trumpington');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (73, '傅國賢', 'fuky9@mail.com', '213-733-1949', '845 Grape Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (74, '藤原明菜', 'akinf416@icloud.com', '7956 788105', '69 Trafalgar Square, Charing Cross');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (75, '新井凛', 'arrin1125@gmail.com', '80-6825-1188', '2 3-803 Kusunokiajima, Kita Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (76, '原田美羽', 'miu1@outlook.com', '(116) 071 4848', '113 Edward Ave, Braunstone Town');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (77, '元德華', 'twyuen@yahoo.com', '70-9511-4491', '3-27-7 Higashitanabe, Higashisumiyoshi Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (78, '木下陸', 'kr1019@icloud.com', '80-6509-0385', '2-3-13 Yoyogi, Shibuya-ku');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (79, '谷裕玲', 'koyl49@gmail.com', '136-1553-4733', '115 East Wangfujing Street, Dongcheng District ');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (80, '严詩涵', 'yashihan618@yahoo.com', '138-5439-1633', 'No.425, Dongsan Road, Erxianqiao, Chenghua District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (81, '甘惠敏', 'kwaiman@gmail.com', '(151) 249 6869', '252 49/50 Strand, Charing Cross');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (82, '文詠詩', 'wsm10@icloud.com', '(1223) 23 2054', '435 Volac Park, Grantchester Rd');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (83, '薛思妤', 'sit86@icloud.com', '90-2261-3552', '1-7-5 Saidaiji Akodacho');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (84, '市川美羽', 'ichikawa2@outlook.com', '7124 962948', '366 Abingdon Rd, Cumnor');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (85, '唐安琪', 'tanganqi@outlook.com', '90-7903-1124', '1-6-18, Marunouchi, Chiyoda-ku');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (86, '吴子异', 'zwu@yahoo.com', '614-045-2277', '733 East Alley');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (87, '中島健太', 'nakajimakent@outlook.com', '154-8971-7397', '297 Daxin S Rd, Daxin Shangquan, Tianhe Qu');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (88, '刘晓明', 'lixiaom7@gmail.com', '154-2020-1100', '809 Jingtian East 1st St, Futian District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (89, '傅宇宁', 'fuyuning@gmail.com', '213-222-6339', '454 Sky Way');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (90, '郭岚', 'gulan@icloud.com', '312-161-6822', '611 North Michigan Ave');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (91, '上野蒼士', 'uenoao@icloud.com', '838-758-6835', '878 Lark Street');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (92, '尹梓軒', 'yth@gmail.com', '614-195-4815', '558 East Alley');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (93, '楊國權', 'yeungkwokk415@gmail.com', '7368 982495', '225 Portland St');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (94, '苏宇宁', 'suyuni@mail.com', '80-2916-4028', '3-19-3 Shimizu, Kita Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (95, '冯子韬', 'zitao88@gmail.com', '11-068-7158', '5-19-11 Shinei 4 Jo, Kiyota Ward');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (96, '梁震南', 'liangzhenn@mail.com', '132-8947-2866', '308 Yueliu Rd, Fangshan District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (97, '和田陸', 'rikuwad@outlook.com', '162-4285-1116', '257 68 Qinghe Middle St, Haidian District');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (98, '藤嘉欣', 'kyt112@outlook.com', '718-816-4415', '556 Nostrand Ave');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (99, '元頴璇', 'wsyuen@icloud.com', '614-588-0200', '465 Wicklow Road');
INSERT INTO "users" ("id", "username", "email", "phone", "address") VALUES (100, '梁璐', 'liangl1018@hotmail.com', '213-087-0838', '991 S Broadway');
COMMIT;

PRAGMA foreign_keys = true;
