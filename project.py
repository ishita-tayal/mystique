###############################IMPORTING MODULES################################################
from tkinter import * #for creating a GUI platform
import mysql.connector, bcrypt #for connecting to sql and encryption of passwords
from tkcalendar import DateEntry #to accept dates using a dropdown calendar
from functools import partial #to use a for loop to create buttons with unique ids
from PIL import ImageTk, Image #to display images on the tkinter window
from forex_python.converter import CurrencyRates #to convert currencies into one another
import datetime #to get the date
c = CurrencyRates() #getting lates currency rates
today = datetime.date.today() #getting today's date
mySalt = bcrypt.gensalt() #creating salt to encrypt passwords

##########################CONNECTING SQL AND PYTHON#############################################
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()

###########################MAKING SQL DATABASE AND TABLES#######################################
mycursor.execute("create database IF NOT EXISTS mystique")
mycursor.execute("use mystique")
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (NAME CHAR(30),DOB DATE,GENDER CHAR(1),EMAILID CHAR(60) PRIMARY KEY,ADDRESS VARCHAR(300),PASSWORD VARCHAR(128))")
mycursor.execute("CREATE TABLE IF NOT EXISTS customercart (PCODE INT(4), PNAME VARCHAR(80), SIZE VARCHAR(10), QUANTITY INT(10),AMOUNT INT(10),CUSTMAIL VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS customerorders (PCODE INT(4), PNAME VARCHAR(80), SIZE VARCHAR(10),QUANTITY INT(10), AMOUNT INT(10), DOP DATE,DELIVERY DATE,CUSTMAIL VARCHAR(255))")
#adding product records in the database using for loop
productcodes=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,
              1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,
              1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,
              1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,
              1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,
              1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,
              1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,
              2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,
              2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,
              2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,
              2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,
              2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,
              2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,
              2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,
              3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,
              3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,
              3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,
              3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,
              3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,
              3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,
              3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,
              4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,
              4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,
              4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,
              4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,
              4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,
              4051,4052,4053,4054,4055,4056,4057,4058,4059,4060,
              4061,4062,4063,4064,4065,4066,4067,4068,4069,4070,
              5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,
              5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,
              5021,5022,5023,5024,5025,5026,5027,5028,5029,5030,
              5031,5032,5033,5034,5035,5036,5037,5038,5039,5040,
              5041,5042,5043,5044,5045,5046,5047,5048,5049,5050,
              5051,5052,5053,5054,5055,5056,5057,5058,5059,5060,
              5061,5062,5063,5064,5065,5066,5067,5068,5069,5070,
              6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,
              6011,6012,6013,6014,6015,6016,6017,6018,6019,6020,
              6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,
              6031,6032,6033,6034,6035,6036,6037,6038,6039,6040,
              6041,6042,6043,6044,6045,6046,6047,6048,6049,6050,
              6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,
              7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,
              7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,
              7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,
              7031,7032,7033,7034,7035,7036,7037,7038,7039,7040,
              7041,7042,7043,7044,7045,7046,7047,7048,7049,7050,
              7051,7052,7053,7054,7055,7056,7057,7058,7059,7060,
              7061,7062,7063,7064,7065,7066,7067,7068,7069,7070,
              8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,
              8011,8012,8013,8014,8015,8016,8017,8018,8019,8020,
              8021,8022,8023,8024,8025,8026,8027,8028,8029,8030,
              8031,8032,8033,8034,8035,8036,8037,8038,8039,8040]

productnames=["mBlack Tshirt","mWhite Tshirt","mPrinted Tshirt","mStriped Tshirt","mBlue Tshirt","mSage Green Tshirt","mGreen Tshirt","mGray Tshirt","mYellow Hoodie","mOlive Green Tshirt",
              "mBlack Shirt","mGray Shirt","mBlue Shirt","mOlive Green Shirt","mStriped Shirt","mWhite Shirt","mChecked Shirt","mGray Checked Shirt","mGreen Khaki Shirt","mB&W Shirt",
              "mFaded Jeans","mBlack Jeans","mRipped Jeans","mBlack Jeans - 2","mGrey Jeans","mLight Blue Jeans","mRipped Jeans - 2","mDark Blue Jeans","mRipped Loose Fit","mSkinny Jeans",
              "mBrown Pants","mBlack Pants","mGray Pants","mWhite Pants","mBlue Trousers","mBlack Trouser","mOlive Pants","mOff-White Pants","mBlue Pants","mBlack Trouser 2",
              "mRed Kurta Set","mWhite Kurta Set","mMaroon Kurta Set","mTeal Kurta Set","mStriped Kurta Set","mBlue Kurta Set","mPink Kurta Set","mRed Kurta Set 2","mGreen Kurta Set","mWhite Kurta",
              "mGreen Shoes","mBlack Nike","mWhite Shoes","mBlack Shoes","mB&W Shoes","mStriped Shoes","mBlue Shoes","mGray Shoes","mRed Shoes","mMaroon Shoes",
              "mSilver Chain","mBelt&Wallet Set","mRed Tie Set","mBlack Shades","mSmart Watch","mGold Chain","mSilver Chain 2","mBlue Watch","mGold Rim Shades","mWhite Watch",
              "wBlack Dress","wFloral Dress","wBlazer Dress","wShirt Dress","wMaxi Dress","wGreen Dress","wWhite Dress","wPink Dress","wBlue Dress","wRed Dress",
              "wTie Dye Top","wOlive Top","wKnitted Top","wRed Top","wPlaid Shirt","wGrey Crop Top","wRed Dress","wWhite Top","wBlack Crop Top","wBlue Satin Top",
              "wFloral Anarkali","wBlue Kurta Set","wGreen Kurta Set","wYellow Kurta Set","wRed Kurta Set","wGrey Anarkali","wBlue Lehenga","wYellow Kurta Set 2","wGreen Kurta Set 2","wWhite Anarkali",
              "wRipped, Slimfit","wWide, Ripped","wWide, Black","wWide, Dark Blue","wStraight, Brown","wSlimfit, Dark","wWide, Dark Gray","wStraight, White","wWide, Purple","wStraight, Blue",
              "wPink Sneakers","wWhite Shoes","wBlue Shoes","wPink Shoes","wBlue Shoes 2","wBrown Shoes","wB&W Shoes","wWhite Shoes 2","wBlack Shoes","wGray Shoes",
              "wFloral Flats","wBlack Boots","wBeige Heels","wPurple Sandals","wPink Heels","wBrown Sandals","wFloral Sandals","wStrappy Heels","wBlack Heels","wBlack Flats",
              "wLeaves Suit Set","wMilkshakes Suit","wFloral Suits Set","wBallerinas Set","wPups Suit Set","wCastle Suit Set","wRed Suit Set","wGiraffe Suit Set","wBerries Suit Set","wYellow Suit Set",
              "kWhite Tee","kGray Tee","kBlack Tee","kPurple Tee","kFrilled Tee","kBlue Tee","kBrown Tee","kTeddy Sweatshirt","kPrinted Tee","kCropped Tee",
              "kBrown Pants","kBrown Pants 2","kDenim Pants","kWide Jeans","kStriped Lowers","kBlack Pants","kGreen Pants","kChecked Bottoms","kPink Trousers","kDenim Bottoms",
              "kDhoti Kurta","kRed Kurta Set","kPeach Kurti","kMint Kurta Set","kFloral Kurta Set","kYellow Kurta Set","kGrey Kurta Set","kBlue Kurta Set","kPatterns Set","kPink Dhoti Kurta",
              "kWhite Outfit","kLight Grey Outfit","kBlue Outfit","kGirls Denim Outfit","kOrange Outfit","kBoys Denim Outfit","kBrown Outfit","kGrey Outfit","kPink Outfit","kGreen Dress",
              "kBlack Outfit","kDino Onesie","kWhite Dress","kPink Onesie","kGreen Onesie","kGrey Tunic Outfit","kGrey Outfit","kDenim Onesie","kPrinted Onesie","kFloral Outfit",
              "kGreen Nikes","kBlue Shoes","kFloral Shoes","kBrown Sandals","kUnicorn Slippers","kBrown Shoes","kWhite Shoes","kBlack Shoes","kWhite Boots","kBlue Flats",
              "kShampoo Set","kBaby Blanket","kCrib Set","kBowl&Spoon Set","kCar Seat","kCream Set","kBabycare Set","kBlue Diaper Bag","kPink Diaper Bag","kBlack Bag",
              "aGold Drop Earrings","aSilver Feather Earrings","aRain Earrings","aNight & Day Earrings","aButterfly Earrings","aSnowflake Earrings","aBee Earrings","aStarry Shower Earrings","aPearl Drops Earrings","aQuirky Eye Earrings",
              "aSilver Camera Pendant","aGold V Necklace","aQuirky Rainbow Rings","aGold Toned Bracelets","aBracelets Set of 4","a Layered Necklace","aButterfly Layers","aVivid Blooms Chain","aRing Set of 4","aRings Set",
              "aBlack Formal Sling","aWhite Floral Sling","aPastel Bag Set","aPink Chained Sling","aBaby Blue Bagpack","aBeige Handbag","aSee Through Bagpack","aBlack Belted Bagpack","aDaisy Tote Bag","aTote Bag Set of 3",
              "aGreen Watch","aBaby Pink Watch","aRed Watch","aWorld Map Watch","aRose Gold Watch","aWhite Watch","aGrey Watch","aGold Watch","aBlack Dial Watch","aCrystal Dial Watch",
              "aWhite Belt","aSkinny Knot Belt","aCircle&Bar Toggle Belt","aSkinny Knot Belt 2","aThin Brown Belt","aCorset Belt","aCream Belt","aPink Belt","aBlack Belt","aPearls Belt",
              "aBlue Scrunchy Set of 2","aHair Ties Set of 4","aClaw Clips Set of 3","aHair Clips Set of 8","aScrunchy Set of 2","aScrunchy Set of 3","aButterfly Claw Clip","aPink Claw Clip","aClaw Clip Set of 4","aHair Clips Set of 4",
              "aPink Shades","aDark Brown Shades","aBlack Shades","aPink Panto Shades","aAnimal Print Shades","aBlack Gold Rim Shades","aRed Shades","aGreen Shades","aBlack Wayfarer Shades","aDark Grey Shades",
              "eGalaxy S22 Ultra 5G","eGalaxy Z Flip 4","eiPhone 14 Pro","eiPhone 14","eiPhone 14 Plus - Red","eVivo T1 Pro 5G","eRealme Narzo 50i","eMi 12 Pro 5G","eiPhone 14 Pro Max","eiPhone 14 Plus - Blue",
              "eGalaxy Tab A8 Black","eApple iPad 9th Gen","eGalaxy Tab S6 Lite","eGalaxy Tab A8 Pink","eSamsung Galaxy Tab S8+","eOppo Pad Air Grey","eGalaxy Tab A7 Black","eGalaxy Tab A7 White","eNokia T20","eRealme Pad Mini",
              "eEnvy 13 Convertible","eGalaxy Book 2 Pro 360","ePavilion x360 Convertible","eDell Inspiron 16","eLenevo Legion 5 Pro","eLenevo Ideapad 3","eLenevo Thinkpad L13","eLenevo Yoga Slim","eHP Pavilion","eASUS VivoBook Flip 14",
              "eSamsung Neo QLED","eMi Qled UHD Smart Tv","eSony Bravia UHD TV","eRedmi Smart TV","eXiaomi Smart TV","eSamsung Series 7","eSony X80K Series TV","eSamsung The Frame Qled","eRealme Smart TV","eLG HD Ready Smart TV",
              "eboAt Rockerz 650 Teal","eboAt Nirvanaa 751 ANC","eboAt Rockerz 450 Pro","eboAt Superior Rockerz ","eboAt Rockerz 650 Red","eboAt Rockerz 550","eApple AirPods Max","eboAt Rockerz 370","eboAt Immortal","eboAt Rockerz 450",
              "eboAt Stone 350 T","eboAt Stone SpinX 2.0","eboAt Stone 1500","eJBL Flip Essential ","eboAt stone 1350","eboAt Stone 350 T","eJBL Go 3","eMarshall Willen Wireless","eJBL Flip 5","eboAt Stone 1010",
              "eMiniso Type-C Cable","eMiniso Power Bank","eLogitech POP Mouse ","eHP 32 GB Flash drive ","eMi LED Light Blue","eMiniso Type-C Cable 2","eOnePlus Power Bank","eLogitech POP Keyboard","eHP Wireless Mouse","eHDMI Cable 10 M",
              "bPink Liquid Lipstick","bMousse Foundation","bLiquid Eyeliner","bMARS Blush+ Palette","bMatte Compact","bIconic Red Lipstick","bFit Me Foundation","bWaterproof Eyeliner","bMaybelline Mascara","bEyeshadow Palatte",
              "bNiacinamide 10% Serum","bRetinol Serum","bFace Roller&Gua Sha(RQ)","bPlum Moisturizer","bMicellar Cleansing Water","bPlum Vitamin C Serum","bHyaluronic Acid Serum","bJade Face Roller ","bPlum Night Gel","bLakme Cleansing Milk",
              "bRose Perfume","bScent Tulip","bFresh Perfume","bBloom Perfume","bFreeland Perfume","bGlam Perfume","bPerfume Set","bWhite Perfume ","bRose Gold Perfume","bHoney Perfume",
              "bOnion Hair Oil","bmCaffeine Hair Mask","bL’oreal Hair Serum","bVega Round Brush","bVega Paddle Brush","bCastor Oil for Hair","bTRESemme Hair Mask","bMatrix Hair Serum ","bVega Cushion Brush","bVega Hair Comb",
              "bDyson Hair Dryer","bPhillips Straigthener","bDyson Corrale","bVega Hair Styling Kit","bDyson Straightener","bPhillips Hair Dryer","bPhils Straightening Comb","bVega 3 in 1 Hair Styler","bPhillips Advanced","bVega Wet&Dry Styler",
              "bSea Salt Shower Gel","bBritish Rose Shower Gel","bHyalurone Shampoo","bWOW Vit-C Face Wash","bmCaffeine Body Scrub","bLavender Conditioner","bTRESemme Shampoo","bL’OREAL Shampoo","bNivea Milk Face Wash","bFace & Body Scrub",
              "hSquares Sheet Set","hGradient Sheet Set","hPink Sheet Set","hDual Color Comforter","hLeaves Sheet Set","hWhite Bedding Set","hReversible Bed Cover","hSpace Sheet Set","hCotton Woven Cover","hBlue Bed Linen",
              "hDeer Showpieces","hDecorative Tree","hPineapple Decor","hReindeer Clock","hPeacock Wall Art","hWall Frame Set","hMetal Art","hTree of Life","hTabletop Bell","hPeach Globe",
              "hWorld Map Lights","hBrass Study Lamp","hShelf Floor Lamp","hCeramic Table Lamp","hTripod Floor Lamp","hPhotoclip LED String Light","hLantern String Lights","hBamboo Fairy Lights","hFlower Fairy Lights","hDreamy Fairy Lights",
              "hMarble Flooring","hFloor Decking","hTimber Flooring","hNatural Wooden Flooring","hLaminate Flooring","hRio Wood Tiles","hMoroccan Ceramic Tiles","hJute Fibre Flooring","hCarpet Tiles","hFloor Carpet",
              "hWooden Study Table","hBrown Coffee Table","hWalnut Coffee Table","hCenter Table","hConference Table","hCrockery Rack","hChimney Hood","hInduction Cooktop","hKitchen Blenders","hDining Table Set",
              "hBlue Towels Set of 4","hBlack Designer Bath Set","hFrench Scented Candles","hHandmade Soaps","hBathroom Plant","hBrown Striped Towel","hSoap Dispenser Set of 4","hScented Candles Set","hLeaf Soap Stand","hSucculents Set of 4",
              "hHandwoven Cushions","hRed Cushion Set (5)","hBlue Cushion Set(4)","hSheer Curtains Set","hBlue Gradient Curtains","hGreen Cushion Set (5)","hThrow & Cushion Set","hPatterned Cushion Set(5)","hGrey Curtain","hVelvet White Curtains",
              "lFloral Print Skater Dress","lWool Wrap Coat","lEllaine Dress","lCopper Dress","lBelong Womens Top","lJonas Luxury Dress","lFifth Ave Feathers Dress","lSea Breeze Shirt","lA.L.C. Alexis Dress","lHandkerchief Dress",
              "lVanilla Jet Set Pouch","lCream Casual Belt","lFossil Ceramic Watch","lVersace, V-Motif Series","lReversible Leather Belt","lFrench Crossbody Bag","lMK Shoulder Bag","lMK Jodie","lCarlie Rose Gold","lGancini Leather Belt",
              "lBlue Slimfit Shirt","lLO-FI Regular Fit","lMid-Wash Denim Shirt","lSpotter Slim Fit Shirt","lFloral Bowling Shirt","lHotaka Slim Fit Jacket","lClifton Trucker Jacket","lBlack Shirt","lDunes Oversized Hoodie","lTropical Print Shirt",
              "lReversible Gancini Belt","lRectangular Buckle Belt","lBrown Leather Watch","lChronograph Watch","lAutomatic Watch","lLeather Belt","lLeather Bi-Fold Wallet","lMK Bi-Fold Wallet","lBonnet Leather Wallet","lTriangular Belt"]

productcategories=["tshirts","tshirts","tshirts","tshirts","tshirts","tshirts","tshirts","tshirts","tshirts","tshirts",
                   "shirts","shirts","shirts","shirts","shirts","shirts","shirts","shirts","shirts","shirts",
                   "jeans","jeans","jeans","jeans","jeans","jeans","jeans","jeans","jeans","jeans",
                   "trousers and pants","trousers and pants","trousers and pants","trousers and pants","trousers and pants","trousers and pants","trousers and pants","trousers and pants","trousers and pants","trousers and pants",
                   "traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear",
                   "shoes","shoes","shoes","shoes","shoes","shoes","shoes","shoes","shoes","shoes",
                   "accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories",
                   "dresses","dresses","dresses","dresses","dresses","dresses","dresses","dresses","dresses","dresses",
                   "tops and tshirts","tops and tshirts","tops and tshirts","tops and tshirts","tops and tshirts","tops and tshirts","tops and tshirts","tops and tshirts","tops and tshirts","tops and tshirts",
                   "traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear",
                   "bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear",
                   "shoes","shoes","shoes","shoes","shoes","shoes","shoes","shoes","shoes","shoes",
                   "heels and flats","heels and flats","heels and flats","heels and flats","heels and flats","heels and flats","heels and flats","heels and flats","heels and flats","heels and flats",
                   "sleepwear","sleepwear","sleepwear","sleepwear","sleepwear","sleepwear","sleepwear","sleepwear","sleepwear","sleepwear",
                   "tshirts","tshirts","tshirts","tshirts","tshirts","tshirts","tshirts","tshirts","tshirts","tshirts",
                   "bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear","bottomwear",
                   "traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear","traditional wear",
                   "preteens collection","preteens collection","preteens collection","preteens collection","preteens collection","preteens collection","preteens collection","preteens collection","preteens collection","preteens collection",
                   "newborn collection","newborn collection","newborn collection","newborn collection","newborn collection","newborn collection","newborn collection","newborn collection","newborn collection","newborn collection",
                   "footwear","footwear","footwear","footwear","footwear","footwear","footwear","footwear","footwear","footwear",
                   "babycare","babycare","babycare","babycare","babycare","babycare","babycare","babycare","babycare","babycare",
                   "earrings","earrings","earrings","earrings","earrings","earrings","earrings","earrings","earrings","earrings",
                   "jewelry","jewelry","jewelry","jewelry","jewelry","jewelry","jewelry","jewelry","jewelry","jewelry",
                   "bags","bags","bags","bags","bags","bags","bags","bags","bags","bags",
                   "watches","watches","watches","watches","watches","watches","watches","watches","watches","watches",
                   "belts","belts","belts","belts","belts","belts","belts","belts","belts","belts",
                   "hair accessories","hair accessories","hair accessories","hair accessories","hair accessories","hair accessories","hair accessories","hair accessories","hair accessories","hair accessories",
                   "sunglasses","sunglasses","sunglasses","sunglasses","sunglasses","sunglasses","sunglasses","sunglasses","sunglasses","sunglasses",
                   "phones","phones","phones","phones","phones","phones","phones","phones","phones","phones",
                   "tablets","tablets","tablets","tablets","tablets","tablets","tablets","tablets","tablets","tablets",
                   "laptops","laptops","laptops","laptops","laptops","laptops","laptops","laptops","laptops","laptops",
                   "tv/television","tv/television","tv/television","tv/television","tv/television","tv/television","tv/television","tv/television","tv/television","tv/television",
                   "headphones","headphones","headphones","headphones","headphones","headphones","headphones","headphones","headphones","headphones",
                   "speakers","speakers","speakers","speakers","speakers","speakers","speakers","speakers","speakers","speakers",
                   "accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories",
                   "makeup","makeup","makeup","makeup","makeup","makeup","makeup","makeup","makeup","makeup",
                   "skincare","skincare","skincare","skincare","skincare","skincare","skincare","skincare","skincare","skincare",
                   "perfumes","perfumes","perfumes","perfumes","perfumes","perfumes","perfumes","perfumes","perfumes","perfumes",
                   "haircare","haircare","haircare","haircare","haircare","haircare","haircare","haircare","haircare","haircare",
                   "appliances","appliances","appliances","appliances","appliances","appliances","appliances","appliances","appliances","appliances",
                   "bath and body","bath and body","bath and body","bath and body","bath and body","bath and body","bath and body","bath and body","bath and body","bath and body",
                   "bed linen and furnishing","bed linen and furnishing","bed linen and furnishing","bed linen and furnishing","bed linen and furnishing","bed linen and furnishing","bed linen and furnishing","bed linen and furnishing","bed linen and furnishing","bed linen and furnishing",
                   "home decor","home decor","home decor","home decor","home decor","home decor","home decor","home decor","home decor","home decor",
                   "lamps and lighting","lamps and lighting","lamps and lighting","lamps and lighting","lamps and lighting","lamps and lighting","lamps and lighting","lamps and lighting","lamps and lighting","lamps and lighting",
                   "flooring","flooring","flooring","flooring","flooring","flooring","flooring","flooring","flooring","flooring",
                   "kitchen and table","kitchen and table","kitchen and table","kitchen and table","kitchen and table","kitchen and table","kitchen and table","kitchen and table","kitchen and table","kitchen and table",
                   "bath","bath","bath","bath","bath","bath","bath","bath","bath","bath",
                   "cushions and curtains","cushions and curtains","cushions and curtains","cushions and curtains","cushions and curtains","cushions and curtains","cushions and curtains","cushions and curtains","cushions and curtains","cushions and curtains",
                   "clothes","clothes","clothes","clothes","clothes","clothes","clothes","clothes","clothes","clothes",
                   "accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories",
                   "clothes","clothes","clothes","clothes","clothes","clothes","clothes","clothes","clothes","clothes",
                   "accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories","accessories"]

productcosts=[765,835,699,699,859,590,759,899,1299,1035,
              1195,835,999,799,859,1390,1399,799,1090,999,
              1995,1635,2599,1799,1999,990,1575,1135,1516,1035,
              2295,1180,1999,2699,1859,1390,1575,1835,1516,1035,
              1295,835,999,699,859,1390,1575,835,1516,1035,
              2199,1660,1999,1950,1859,1390,2499,1835,1799,1555,
              1295,835,999,699,859,1390,835,1575,1516,1035,
              1691,835,999,699,859,1390,1575,835,1516,1035,
              799,877,767,550,879,635,835,890,618,687,
              4355,1198,3249,4799,1079,3599,3875,2585,2859,4999,
              1023,1189,1259,1123,1323,1390,1192,1463,1192,1035,
              1295,899,999,859,759,1390,1575,835,1516,1035,
              1295,1835,999,999,859,1390,1290,1305,1516,1035,
              1295,1835,999,699,859,1390,1575,835,1516,1035,
              799,835,699,699,859,690,855,999,1516,1035,
              799,835,949,699,859,1390,675,715,890,1099,
              1295,835,999,859,859,890,1575,835,1516,935,
              1295,835,999,699,859,990,1575,835,1516,1035,
              1295,835,999,699,859,1390,1575,835,1516,1035,
              1295,835,999,699,859,1390,1575,835,1516,1035,
              1295,835,999,699,859,1390,1575,835,1516,1035,
              799,835,699,699,859,690,855,999,616,1035,
              799,835,999,2099,859,690,855,599,716,1035,
              2799,2835,4099,1519,959,1690,1125,999,816,2035,
              3999,1199,2999,7100,3859,2790,3550,2999,1516,1110,
              1099,565,899,699,859,1599,765,999,1260,762,
              40,50,120,80,40,60,60,75,250,50,
              2010,1935,2699,1549,1369,2190,1855,1599,1516,1035,
              108999,101999,129300,79990,89990,24999,9990,54999,139900,89990,
              14999,29900,25999,14900,11990,16999,12990,37999,18499,10990,
              83499,125000,85999,85999,140690,29999,83690,75990,139900,32990,
              98499,59999,380000,59999,13999,47990,85490,75990,39900,15990,
              1799,3999,1800,1299,1799,1999,59900,1999,2642,3990,
              1699,3999,6990,5299,4799,1999,3699,9999,6538,2690,
              800,1099,2499,329,99,999,1030,9785,899,525,
              578,136,187,299,299,428,224,299,295,660,
              800,388,1049,355,4799,711,363,1999,188,290,
              580,499,580,499,799,580,3699,580,6538,580,
              347,509,413,299,499,215,595,500,358,240,
              34900,2699,32900,5299,24799,2542,3699,1299,1438,2690,
              300,309,299,299,499,260,150,699,120,269,
              2231,1099,1990,2999,1799,3600,1277,9999,1990,1299,
              199,360,299,1879,7499,499,6000,11700,3650,1499,
              4999,2221,3667,699,4118,399,499,2800,169,800,
              2968,2450,347,1780,1894,1271,1199,2010,1500,4399,
              5719,1199,5426,3000,69550,14831,17900,2010,12571,69699,
              2659,4450,990,899,799,799,2699,1299,538,2690,
              2715,1099,3990,899,1299,1999,3699,1999,999,1090,
              24500,30099,14800,15299,7799,10999,27699,6999,64238,7750,
              13500,8099,16990,91099,14799,27299,52000,12999,26538,35000,
              8054,6099,22990,12299,32799,16999,18699,10800,18938,9690,
              32750,17099,11990,13499,16799,12999,19699,13999,22000,45000]
mycursor.execute("CREATE TABLE IF NOT EXISTS products (PCODE INT(4) PRIMARY KEY,PNAME VARCHAR(80),PCATEGORY VARCHAR(100),PCOST INT(10))")
for i in range(0,len(productcodes)):
    mycursor.execute("INSERT IGNORE INTO products VALUES({},'{}','{}',{})".format(productcodes[i],productnames[i],productcategories[i],productcosts[i]))
    mydb.commit()
    

#####################CREATING TKINTER WINDOW############################
window = Tk()
window.title('Mystique: Online Shopping App')
window.geometry("1000x600")
window.configure(bg = "#c0cafb")
######################CREATING A FUNTION FOR CANVAS##############################
def canvasdefinition():
    global canvas
    canvas = Canvas(window,bg = "#c0cafb",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
#######################DEFINING OTHER USEFUL FUNCTIONS########################    
def clear_frame(): #function to clear frame
   for widgets in window.winfo_children():
      widgets.destroy()
def closewindows(): #function to destroy all popup windows when a new screen is visited
    global signout,cart,error,orderplaced,orders,changeaddress,pwchanged,delacc,customerrecords,searchcustomer,productrecords,searchproducts,productinfo
    try:
        signout.destroy()
    except Exception:
        pass
    try:
        cart.destroy()
    except Exception:
        pass
    try:
        error.destroy()
    except Exception:
        pass
    try:
        orderplaced.destroy()
    except Exception:
        pass
    try:
        orders.destroy()
    except Exception:
        pass
    try:
        searchcustomer.destroy()
    except Exception:
        pass
    try:
        changeaddress.destroy()
    except Exception:
        pass
    try:
        pwchanged.destroy()
    except Exception:
        pass
    try:
        delacc.destroy()
    except Exception:
        pass
    try:
        customerrecords.destroy()
    except Exception:
        pass
    try:
        productrecords.destroy()
    except Exception:
        pass
    try:
        searchproducts.destroy()
    except Exception:
        pass
    try:
        productinfo.destroy()
    except Exception:
        pass
###############################LOGIN AND SIGNUP FUNCTIONS#################################################
def loginprocess(mail,pw): #matching records from sql table
    global string,accmail
    accmail=mail
    string=mail
    mycursor.execute("select PASSWORD from customers where EMAILID='{}'".format(mail))
    x=mycursor.fetchall()
    if len(x)==0:
        loginscreen(0)
    elif bcrypt.checkpw(pw.encode('utf-8'),x[0][0].encode('utf-8')):
        homepage()
    else:
        loginscreen(2)
    
    
def signupprocess(name,dob,gender,mail,pw,cpw,address):
    global string,accmail
    mycursor.execute("Select emailid from customers")
    emails=mycursor.fetchall()
    specialchar=["\"","[","!","#","$","%","^","&","*","(",")","<",">","?","/","|","}","{","~",":","]"]
    EMAIL=True
    for i in specialchar:
        if i in mail:
            EMAIL=False
    NAME=True
    for i in specialchar:
        if i in name:
            NAME=False        
    B=False
    for i in emails:
        if i[0]==mail:
            B=True
    if name=="" or dob=="" or gender=="" or mail=="" or pw=="" or cpw=="" or address=="":
        errorscreens("All fields are mandatory.")
    elif "@" not in mail or "." not in mail or EMAIL==False: 
        errorscreens("Enter valid Email ID.")
    elif B==True:
        errorscreens("Account already exists, login instead.")
    elif NAME==False or "@" in name or "." in name:
        errorscreens("Enter valid name.")
    elif pw!=cpw:
        errorscreens("Passwords don't match.")
    elif pw==cpw:
        try:
            error.destroy()
        except Exception:
            pass
        homepage()
        accmail=mail
        accnam=name
        accdob=dob
        bytePwd=pw.encode('utf-8')
        hashed = bcrypt.hashpw(bytePwd, mySalt)
        mycursor.execute("INSERT INTO customers VALUES('{}','{}','{}','{}','{}','{}')".format(name,dob,gender,mail,address,hashed.decode()))
        mydb.commit()
        string=mail

def adminloginprocess(username,apw):
    if username=="admin" and apw=="admin":
        adminoptionsscreen()
    else:
        adminloginscreen(0)

###########################FUNCTION FOR WELCOME SCREEN##########################
def welcomescreen():
    global welcomescreenimg,custbtn,exebtn
    closewindows()
    clear_frame()
    canvasdefinition()
    welcomescreenimg = PhotoImage(file = f"images\\welcomescreen.png")
    background = canvas.create_image(494.0, 300.0,image=welcomescreenimg)
    custbtn = PhotoImage(file = f"images\\custbtn.png")
    customer = Button(image = custbtn,borderwidth = 0,highlightthickness = 0,command = lambda:loginscreen(1),relief = "flat",cursor="hand2")
    customer.place(x = 578, y = 249,width = 276,height = 64)
    exebtn = PhotoImage(file = f"images\\executivebtn.png")
    executive = Button(image = exebtn,borderwidth = 0,highlightthickness = 0,command = lambda:adminloginscreen(1),relief = "flat",cursor="hand2")
    executive.place(x = 578, y = 348,width = 276,height = 64)


###########################CREATING CUSTOMER PART OF THE APP####################################
def loginscreen(B):
    global loginscreenimg,loginbtn,loginsignupbtn,backbtn,showpwbtn
    clear_frame()
    closewindows()
    canvasdefinition()
    if B==0: 
        loginscreenimg=PhotoImage(file=f"images\\loginscreenusernotreg.png")
    elif B==2:
        loginscreenimg=PhotoImage(file=f"images\\loginscreennotmatch.png")
    else:
        loginscreenimg = PhotoImage(file = f"images\\loginscreen.png")
    background = canvas.create_image(494.0, 300.0,image=loginscreenimg)
    loginmailentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    loginmailentry.place(x = 668, y = 245,width = 247,height = 44)
    loginpwentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    loginpwentry.default_show_val=loginpwentry['show']
    loginpwentry['show']="●" #will show "●" instead of the entered characters
    loginpwentry.place(x = 668, y = 318,width = 247,height = 44)
    loginbtn = PhotoImage(file = f"images\\loginbtn.png")
    login = Button(image = loginbtn,borderwidth = 0,highlightthickness = 0,command = lambda:loginprocess(loginmailentry.get(),loginpwentry.get()),relief = "flat",cursor="hand2")
    login.place(x = 678, y = 385,width = 88,height = 39)
    loginsignupbtn = PhotoImage(file = f"images\\loginsignupbtn.png")
    loginsignup = Button(image = loginsignupbtn,borderwidth = 0,highlightthickness = 0,command = signupscreen,relief = "flat",cursor="hand2")
    loginsignup.place(x = 771, y = 440,width = 88,height = 39)
    backbtn= PhotoImage(file = f"images\\backbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command = welcomescreen,relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 54,height = 62)
    def showpassword():
        global hidepwbtn,hidepw
        loginpwentry['show']=""
        showpw.place_forget()
        hidepwbtn= PhotoImage(file = f"images\\hidepwbtn.png")
        hidepw = Button(image = hidepwbtn,borderwidth=0,highlightthickness = 0,command = hidepassword,relief = "flat",cursor="hand2")
        hidepw.place(x = 872, y = 323,width = 33,height = 33)
    def hidepassword():
        loginpwentry['show']="●"
        hidepw.place_forget()
        showpw.place(x = 872, y = 323,width = 33,height = 33) 
    showpwbtn= PhotoImage(file = f"images\\showpwbtn.png")
    showpw = Button(image = showpwbtn,borderwidth=0,highlightthickness = 0,command = showpassword,relief = "flat",cursor="hand2")
    showpw.place(x = 872, y = 323,width = 33,height = 33)
    
def signupscreen():
    global signupscreenimg,signupbtn,backbtn,showpwbtn,hidepwbtn,showpwbtn2,showpwbtn1
    clear_frame()
    closewindows()
    canvasdefinition()
    signupscreenimg = PhotoImage(file = f"images\\signupscreen.png")
    background = canvas.create_image(494.0, 300.0,image=signupscreenimg)
    signupnameentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    signupnameentry.place(x = 717, y = 154,width = 206,height = 28)
    cal=DateEntry(selectmode='day',maxdate=today)
    cal.place(
        x = 717, y = 194,
        width = 206,
        height = 28)
    def my_upd(*args): # triggered when value of string variable changes
        d=cal.get_date()
        return d.strftime("%Y-%m-%d")
    def shortform(choice):
        choice=clicked.get()
        if choice=="Female":
            g="F"
        elif choice=="Male":
            g="M"
        else:
            g="N"
        return g
    options=["Female", "Male","Rather Not Disclose"]
    clicked=StringVar()
    clicked.set("Rather Not Disclose")
    drop= OptionMenu(canvas,clicked,*options,command=shortform)
    drop.configure(anchor='w')
    drop.place(x=717,y=234,width = 206,height = 28)
    drop.config(bg="WHITE", fg="BLACK")
    drop["menu"].config(bg="white")
    signupmailentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    signupmailentry.place(x = 717, y = 274,width = 206,height = 28)
    signuppwentry = Entry(bd = 0,bg = "#ffffff", highlightthickness = 0)
    signuppwentry['show']="●"
    signuppwentry.place(x = 717, y = 319,width = 206,height = 28)
    signuppwentry.bind('<Control-x>', lambda e: 'break') #disable cut
    signuppwentry.bind('<Control-c>', lambda e: 'break') #disable copy
    signuppwentry.bind('<Control-v>', lambda e: 'break') #disable paste
    signuppwentry.bind('<Button-3>', lambda e: 'break')  #disable right-click
    def showpassword1():
        global hidepwbtn1,hidepw1 
        signuppwentry['show']=""
        showpw1.place_forget()
        hidepwbtn1= PhotoImage(file = f"images\\hidepwsmall1.png")
        hidepw1= Button(image = hidepwbtn1,borderwidth=0,highlightthickness = 0,command = hidepassword1,relief = "flat",cursor="hand2")
        hidepw1.place(x = 897, y = 323,width = 18,height = 18)
    def hidepassword1():
        signuppwentry['show']="●"
        hidepw1.place_forget()
        showpw1.place(x = 897, y = 323,width = 18,height = 18)
    #button to show password
    showpwbtn1= PhotoImage(file = f"images\\showpwsmall1.png")
    showpw1 = Button(image = showpwbtn1,borderwidth=0,highlightthickness = 0,command = showpassword1,relief = "flat",cursor="hand2")
    showpw1.place(x = 897, y = 323,width = 18,height = 18)
    #PASSWORD FIELD 2
    signupcpwentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    signupcpwentry.place(x = 717, y = 365,width = 206,height = 28)
    signupcpwentry['show']="●"
    signupcpwentry.bind('<Control-x>', lambda e: 'break') #disable cut
    signupcpwentry.bind('<Control-c>', lambda e: 'break') #disable copy
    signupcpwentry.bind('<Control-v>', lambda e: 'break') #disable paste
    signupcpwentry.bind('<Button-3>', lambda e: 'break')  #disable right-click
    def showpassword2():
        global hidepwbtn2
        global hidepw2
        signupcpwentry['show']=""
        showpw2.place_forget()
        hidepwbtn2= PhotoImage(file = f"images\\hidepwsmall.png")
        hidepw2= Button(image = hidepwbtn2,borderwidth=0,highlightthickness = 0,command = hidepassword2,relief = "flat",cursor="hand2")
        hidepw2.place(x = 897, y = 369,width = 18,height = 18)

    def hidepassword2():
        signupcpwentry['show']="●"
        hidepw2.place_forget()
        showpw2.place(x = 897, y = 369,width = 18,height = 18)

    #button to show password
    showpwbtn2= PhotoImage(file = f"images\\showpwsmall.png")
    showpw2 = Button(window,image = showpwbtn2,borderwidth=0,highlightthickness = 0,
                     command = showpassword2,
                     relief = "flat",cursor="hand2")
    showpw2.place(x = 897, y = 369,width = 18,height = 18)
    
    signupaddressentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    signupaddressentry.place(x = 717, y = 419,width = 206,height = 28)
    signupbtn = PhotoImage(file = f"images\\signupbtn.png")
    signup = Button(image = signupbtn,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command =lambda:signupprocess(signupnameentry.get().upper(),my_upd(),shortform(""),signupmailentry.get().upper(),signuppwentry.get(),signupcpwentry.get(),signupaddressentry.get().upper()),
                    relief = "flat",cursor="hand2")
    signup.place(x = 679, y = 469,width = 147,height = 39.07)
    backbtn= PhotoImage(file = f"images\\backbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command = lambda:loginscreen(1),relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 54,height = 62)

def homepage():
    global homepagescreen,switchbtn,Ordersbtn,Accountbtn,Privacypolicybtn,Categoriesbtn,Cartbtn,wbackbtn
    closewindows()
    clear_frame()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    homepagescreen=PhotoImage(file=f"images\\homepagescreen.png")
    background = canvas.create_image(500.0, 300.0,image=homepagescreen)

    Ordersbtn= PhotoImage(file = f"images\\Ordersbtn.png")
    Orders = Button( image = Ordersbtn, borderwidth=0, highlightthickness = 0, command = lambda:[seeorders(string),change_image(0,"stop")], relief = "flat",cursor="hand2")
    Orders.place( x = 38, y = 440, width = 173, height = 134)

    Accountbtn= PhotoImage(file = f"images\\Accountbtn.png")
    Account = Button( image = Accountbtn, borderwidth=0, highlightthickness = 0, command = lambda:[profilescreen(),change_image(0,"stop")], relief = "flat",cursor="hand2")
    Account.place( x = 225, y = 440, width = 172, height = 132)

    Privacypolicybtn= PhotoImage(file = f"images\\Privacypolicybtn.png")
    Privacypolicy = Button( image = Privacypolicybtn, borderwidth=0, highlightthickness = 0, command = lambda:[privpolscreen(),change_image(0,"stop")], relief = "flat",cursor="hand2")
    Privacypolicy.place( x = 412.5, y = 440, width = 172, height = 132)

    Categoriesbtn= PhotoImage(file = f"images\\Categoriesbtn.png")
    Categories = Button( image = Categoriesbtn, borderwidth=0, highlightthickness = 0, command = lambda:[searchscreen(),change_image(0,"stop")], relief = "flat",cursor="hand2")
    Categories.place( x = 600, y = 440, width = 172, height = 132)

    Cartbtn= PhotoImage(file = f"images\\Cartbtn.png")
    Cart = Button( image = Cartbtn, borderwidth=0, highlightthickness = 0, command = lambda:[cartoptionsscreen(),change_image(0,"stop")], relief = "flat",cursor="hand2")
    Cart.place( x = 787, y = 440, width = 172, height = 132)

    wbackbtn = PhotoImage(file = f"images\\homepageback.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[signoutconfirm(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wback.place(x =20, y = 22,width = 58,height = 56)

    #the banners will change time to time
    banner1 = ImageTk.PhotoImage(Image.open("images\\homepagebanner1.png"))
    banner2 = ImageTk.PhotoImage(Image.open("images\\homepagebanner2.png"))
    banner3 = ImageTk.PhotoImage(Image.open("images\\homepagebanner3.png"))
    banner4 = ImageTk.PhotoImage(Image.open("images\\homepagebanner4.png"))
    banner5 = ImageTk.PhotoImage(Image.open("images\\homepagebanner5.png"))

    l=Label()
    l.place(x=20,y=179,height=227,width=960)
    banners=[banner1,banner2,banner3,banner4,banner5]
    def change_image(nextindex,value):
        global change
        if value=="continue":
            l.configure(image=banners[nextindex])
            change=window.after(2000, lambda: change_image((nextindex+1) % len(banners),"continue"))
        else:
            window.after_cancel(change)
        
    change_image(0,"continue")

def privpolscreen():
    global privacypolicybg,backbtn
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    privacypolicybg=PhotoImage(file=f"images\\privacypolicyscreen.png")
    background = canvas.create_image(500.0, 300.0,image=privacypolicybg)
    backbtn= PhotoImage(file = f"images\\pbackbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command = homepage,relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 58,height = 66)
    

def cartoptionsscreen():
    global cartoptionsbg,switchbtn,viewcartbtn,checkoutbtn,wbackbtn
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    cartoptionsbg=PhotoImage(file=f"images\\cartoptionsscreen.png")
    background = canvas.create_image(500.0, 300.0,image=cartoptionsbg)

    viewcartbtn= PhotoImage(file = f"images\\viewcartbtn.png")
    viewcart = Button( image = viewcartbtn, borderwidth=0, highlightthickness = 0, command = seecart, relief = "flat",cursor="hand2")
    viewcart.place( x = 174, y = 286, width = 290, height = 269)

    checkoutbtn= PhotoImage(file = f"images\\checkoutbtn.png")
    checkout = Button( image = checkoutbtn, borderwidth=0, highlightthickness = 0, command = checkoutscreen, relief = "flat",cursor="hand2")
    checkout.place( x = 534, y = 286, width = 290, height = 269)

    wbackbtn = PhotoImage(file = f"images\\bluebackbtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = homepage,relief = "flat",cursor="hand2")
    wback.place(x =20, y = 22,width = 54,height = 62)

def checkoutscreen():
    global checkoutscreenbg,placeorderbtn,wbackbtn
    mycursor.execute("SELECT sum(QUANTITY),sum(AMOUNT*QUANTITY) from customercart where custmail='{}'".format(string))
    codetails=mycursor.fetchall()
    
    if codetails[0][0]==None:
        errorscreens("No product in cart.")
    else:
        clear_frame()
        closewindows()
        canvasdefinition()
        canvas.configure(bg="#151435")
        checkoutscreenbg=PhotoImage(file=f"images\\checkoutscreen.png")
        background = canvas.create_image(500.0, 300.0,image=checkoutscreenbg)

        totalnolabel=Label(text=codetails[0][0],anchor='w',bg="#151435",fg="white")
        totalnolabel.config(font=('Helvetica bold', 26))
        totalnolabel.place(x=193,y=310)

        options=["INR", "USD","EUR","GBP","KRW","SEK"]
        currency=StringVar()
        currency.set("INR")


        def currencychange(i):
            global amountlabel,newamount
            try:
                newamount=c.convert('INR',currency.get(),codetails[0][1])
            except Exception:
                errorscreens("Sorry, rates unavailable momentarily")
                currency.set("INR")
            try:
                amountlabel.destroy()
            except Exception:
                pass

            amountlabel=Label(text=round(newamount,2),anchor='w',bg="#151435",fg="white")
            amountlabel.config(font=('Helvetica bold', 26))
            amountlabel.place(x=740,y=310)


        currencychange(1)

        drop1= OptionMenu(canvas,currency,*options,command=currencychange)
        drop1.configure(anchor='w')
        drop1.place(x=428,y=320,width = 218,height = 40)
        drop1.config(bg="WHITE", fg="BLACK")
        drop1["menu"].config(bg="white")
        
        placeorderbtn= PhotoImage(file = f"images\\placeorderbtn.png")
        placeorder = Button( image = placeorderbtn, borderwidth=0, highlightthickness = 0, command = orderprocess, relief = "flat",cursor="hand2")
        placeorder.place( x = 345, y = 448, width = 310, height = 97)
        
        wbackbtn = PhotoImage(file = f"images\\bluebackbtn.png")
        wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = cartoptionsscreen,relief = "flat",cursor="hand2")
        wback.place(x =20, y = 22,width = 54,height = 62)

def orderprocess():
    global orderplaced
    mycursor.execute("SELECT PCODE,PNAME,SIZE,QUANTITY,AMOUNT from customercart where custmail='{}' GROUP BY PCODE,SIZE ORDER BY PCODE".format(string))
    orderproducts=mycursor.fetchall()
    fivedays = today + datetime.timedelta(days=5)
    deliverydate=fivedays.strftime("%A,%d %B, %Y")
    deliverytabledate=fivedays.strftime("%Y-%m-%d")
    for i in orderproducts:
        mycursor.execute("insert into customerorders values({},'{}','{}',{},{},'{}','{}','{}')".format(i[0],i[1],i[2],i[3],i[4],today.strftime("%Y-%m-%d"),deliverytabledate,string))
        mydb.commit()
    mycursor.execute("delete from customercart where custmail='{}'".format(string))
    mydb.commit()
    try:
        orderplaced.destroy()
    except Exception:
        pass
    homepage()
    orderplaced = Tk()
    orderplaced.title('Woohoo!')
    orderplaced.geometry("400x100")
    orderplaced.resizable(False, False)
    
    fivedays = today + datetime.timedelta(days=5)
    deliverydate=fivedays.strftime("%A,%d %B, %Y")
    e=Label(orderplaced,text='Your order has been placed.',anchor='w',fg="black")
    e.pack(side = "top",expand="yes")
    e=Label(orderplaced,text='It will be delivered on {}.'.format(deliverydate),anchor='w',fg="black")
    e.pack(expand="yes")
    oplaced = Button(orderplaced,text="OKAY THANKS!",borderwidth = 2,highlightthickness = 0,command = lambda:orderplaced.destroy(),cursor="hand2")
    oplaced.pack(side = "bottom",expand="yes")

def seecart():
    global cart,removebtn
    try:
        cart.destroy()
    except Exception:
        pass
    mycursor.execute("SELECT PCODE,PNAME,SIZE,AMOUNT,QUANTITY,AMOUNT*QUANTITY FROM customercart where custmail='{}' GROUP BY PCODE,SIZE ORDER BY PCODE".format(string))
    records=mycursor.fetchall()
    if len(records)==0:
        errorscreens("Nothing in cart.")
    else:
        cart = Toplevel()
        cart.geometry("1000x600")
        cart.configure(bg = "#c0cafb")
        cart.title('Cart')
        canvas = Canvas(cart,bg = "#c0cafb",bd = 0,highlightthickness = 0,relief = "ridge")
        frame = Frame(canvas)
        e=Label(frame,height=3,width=21,text='Product Code',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=0)
        e=Label(frame,height=3,width=21,text='Product Name',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=1)
        e=Label(frame,height=3,width=21,text='Size',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=2)
        e=Label(frame,height=3,width=21,text='Cost Per Unit',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=3)
        e=Label(frame,height=3,width=21,text='Quantity',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=4)
        e=Label(frame,height=3,width=21,text='Amount',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=5)
        e=Label(frame,height=3,width=3,text='X',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=6)
        
        buttonlist=[]
        rowno=2
        for u in range(len(records)):
                b = Button(frame,height=2,width=21, text=records[u][0],borderwidth=2, anchor="w",bg='#ffffff',command=partial(prodinfo,records[u][0]),relief='ridge',cursor="hand2")
                buttonlist.append(b)
                b.grid(row=rowno, column=0)
                rowno+=1
        
        i=2
        for r in records:
            for j in range(1,len(r)):
                e = Label(frame,height=2,width=21, text=r[j],
            borderwidth=2,relief='ridge', anchor="w",bg='#ffffff') 
                e.grid(row=i, column=j) 
            i=i+1
        buttonlist2=[]
        rowno=2
        removebtn = ImageTk.PhotoImage(Image.open("images\\removeicon.png"))
        for v in range(len(records)):
                
                b = Button(frame,image=removebtn,height=26,width=26,borderwidth=2, anchor="w",bg='#ffffff',command=partial(removeprod,records[v][0],records[v][2]),relief='ridge',cursor="hand2")
                buttonlist2.append(b)
                b.grid(row=rowno, column=j+1)
                rowno+=1
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        scrollbar = Scrollbar(cart, orient='vertical', command=canvas.yview)
        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
        canvas.pack(fill='both', expand=True, side='left')
        scrollbar.pack(fill='y', side='right')
        cart.resizable(False,False)
        cart.mainloop()

def seeorders(mail):
    global orders,removebtn,string

    try:
        orders.destroy()
    except Exception:
        pass
    
    string=mail
    mycursor.execute("SELECT PCODE,PNAME,SIZE,AMOUNT,QUANTITY,DOP,DELIVERY FROM customerorders where custmail='{}' GROUP BY PCODE,DOP,SIZE ORDER BY DOP".format(string))
    records=mycursor.fetchall()
    if len(records)==0:
        errorscreens("No orders yet.")
    else:
        orders = Toplevel()
        orders.geometry("1000x600")
        orders.configure(bg = "#c0cafb")
        orders.title('Orders')
        canvas = Canvas(orders,bg = "#c0cafb",bd = 0,highlightthickness = 0,relief = "ridge")
        frame = Frame(canvas)
        e=Label(frame,height=3,width=20,text='Product Code',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=0)
        e=Label(frame,height=3,width=20,text='Product Name',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=1)
        e=Label(frame,height=3,width=20,text='Size',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=2)
        e=Label(frame,height=3,width=20,text='Cost',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=3)
        e=Label(frame,height=3,width=20,text='Quantity',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=4)
        e=Label(frame,height=3,width=20,text='Date of Purchase',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=5)
        e=Label(frame,height=3,width=20,text='Date of Delivery',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=6)
        
        buttonlist=[]
        rowno=2
        for u in range(len(records)):
                b = Button(frame,height=2,width=20, text=records[u][0],borderwidth=2, anchor="w",bg='#ffffff',command=partial(prodinfo,records[u][0]),relief='ridge',cursor="hand2")
                buttonlist.append(b)
                b.grid(row=rowno, column=0)
                rowno+=1
        
        i=2
        for r in records:
            for j in range(1,len(r)):
                e = Label(frame,height=2,width=20, text=r[j],
            borderwidth=2,relief='ridge', anchor="w",bg='#ffffff') 
                e.grid(row=i, column=j) 
            i=i+1
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        scrollbar = Scrollbar(orders, orient='vertical', command=canvas.yview)
        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
        canvas.pack(fill='both', expand=True, side='left')
        scrollbar.pack(fill='y', side='right')
        orders.resizable(False,False)
        orders.mainloop()

def removeprod(a,b):
        if b==None:
            mycursor.execute("SELECT QUANTITY FROM customercart where CUSTMAIL='{}' and PCODE={}".format(string,a))
            prods=mycursor.fetchall()
            if prods[0][0]==1:
                mycursor.execute("DELETE FROM customercart where custmail='{}' and PCODE={}".format(string,a))
            else:
                mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY-1 where PCODE={} AND CUSTMAIL='{}'".format(a,string))
            mydb.commit() 

        else:
            mycursor.execute("SELECT QUANTITY FROM customercart where CUSTMAIL='{}' and PCODE={} and SIZE='{}'".format(string,a,b))
            prods=mycursor.fetchall()
            if prods[0][0]==1:
                mycursor.execute("DELETE FROM customercart where custmail='{}' and PCODE={} AND SIZE='{}'".format(string,a,b))
            else:
                mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY-1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(a,b,string))
        mydb.commit()
        seecart()
    
def signoutconfirm():
    global signout
    try:
        signout.destroy()
    except Exception:
        pass
    signout= Tk()
    signout.title('Confirm Signout')
    signout.geometry("250x100")
    signout.resizable(False, False)
    e=Label(signout,text='Sign Out?',anchor='w',fg="black")
    e.place(x=100,y=23)
    yes = Button(signout,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[signout.destroy(),loginscreen(1)],cursor="hand2")
    yes.place(x = 50, y = 56,width = 55,height =21)
    no = Button(signout,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:signout.destroy(),cursor="hand2")
    no.place(x = 144, y = 56,width = 55,height =21)

def searchscreen():
    global searchscreenimg,categorymenbtn,categorywomenbtn,categorykidsbtn,categoryelectbtn,categoryaccbtn,categorybeautybtn,categoryhnlbtn,categoryluxebtn,mystiquebtn,searchbtn
    clear_frame()
    closewindows()
    canvasdefinition()
    searchscreenimg = PhotoImage(file = f"images\\searchscreen.png")
    background = canvas.create_image( 500.0, 300.0, image=searchscreenimg)
    categorymenbtn= PhotoImage(file = f"images\\categorymenbtn.png")
    categorymen = Button( image = categorymenbtn, borderwidth=0, highlightthickness = 0, command = mencategoryscreen, relief = "flat",cursor="hand2")
    categorymen.place( x = 145, y = 168, width = 173, height = 173)
    categorywomenbtn= PhotoImage(file = f"images\\categorywomenbtn.png")
    categorywomen = Button( image = categorywomenbtn, borderwidth=0, highlightthickness = 0, command = womencategoryscreen, relief = "flat",cursor="hand2")
    categorywomen.place( x = 324, y = 168, width = 173, height = 173)   
    categorykidsbtn= PhotoImage(file = f"images\\categorykidsbtn.png")
    categorykids = Button( image = categorykidsbtn, borderwidth=0, highlightthickness = 0, command = kidscategoryscreen, relief = "flat",cursor="hand2")
    categorykids.place( x = 500, y = 166, width = 173, height = 173)
    categoryaccbtn= PhotoImage(file = f"images\\categoryaccbtn.png")
    categoryacc = Button( image = categoryaccbtn, borderwidth=0, highlightthickness = 0, command = acccategoryscreen, relief = "flat",cursor="hand2")
    categoryacc.place( x = 676, y = 166, width = 173, height = 173)
    categoryelectbtn= PhotoImage(file = f"images\\categoryelectbtn.png")
    categoryelect = Button( image = categoryelectbtn, borderwidth=0, highlightthickness = 0, command = electronicscategoryscreen, relief = "flat",cursor="hand2")
    categoryelect.place( x = 145, y = 346, width = 173, height = 173)
    categorybeautybtn= PhotoImage(file = f"images\\categorybeautybtn.png")
    categorybeauty = Button( image = categorybeautybtn, borderwidth=0, highlightthickness = 0, command = beautycategoryscreen, relief = "flat",cursor="hand2")
    categorybeauty.place( x = 325, y = 343, width = 173, height = 173)
    categoryhnlbtn= PhotoImage(file = f"images\\categoryhnlbtn.png")
    categoryhnl = Button( image = categoryhnlbtn, borderwidth=0, highlightthickness = 0, command =hnlcategoryscreen, relief = "flat",cursor="hand2")
    categoryhnl.place( x = 500, y = 340, width = 172, height = 173)
    categoryluxebtn= PhotoImage(file = f"images\\categoryluxebtn.png")
    categoryluxe = Button( image = categoryluxebtn, borderwidth=0, highlightthickness = 0, command = luxecategoryscreen, relief = "flat",cursor="hand2")
    categoryluxe.place( x = 679, y = 343, width = 173, height = 173)
    mystiquebtn= PhotoImage(file = f"images\\mystiquebtn.png")
    mystique = Button(image = mystiquebtn,borderwidth=0,highlightthickness = 0,command = homepage,relief = "flat",cursor="hand2")
    mystique.place(x = 17, y = 14,width = 150,height = 85)



######################################MEN'S SECTION##########################################
def mencategoryscreen():
    global switchbtn,menscreen,tshirtsbtn,shirtsbtn,mjeansbtn,trousersandpantsbtn,mshoesbtn,traditionalwearbtn,maccessoriesbtn,wbackbtn,background
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    menscreen=PhotoImage(file=f"images\\menscreen.png")
    background = canvas.create_image(500.0, 300.0,image=menscreen)

    tshirtsbtn = PhotoImage(file = f"images\\tshirtsbtn.png")
    tshirts = Button(image = tshirtsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[mtshirts(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    tshirts.place(x = 27, y = 379,width = 115,height = 170)

    shirtsbtn = PhotoImage(file = f"images\\shirtsbtn.png")
    shirts = Button(image = shirtsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[mshirts(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    shirts.place(x = 165, y = 379,width = 115,height = 170)

    mjeansbtn = PhotoImage(file = f"images\\mjeansbtn.png")
    mjeans = Button(image = mjeansbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[mjeansscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    mjeans.place(x = 304, y = 379,width = 115,height = 170)

    trousersandpantsbtn = PhotoImage(file = f"images\\trousersandpantsbtn.png")
    trousersandpants = Button(image = trousersandpantsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[mpants(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    trousersandpants.place(x =443, y = 379,width = 114,height = 170)

    traditionalwearbtn = PhotoImage(file = f"images\\traditionalwearbtn.png")
    traditionalwear = Button(image = traditionalwearbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[mtraditionalwear(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    traditionalwear.place(x =580, y = 379,width = 118,height = 170)

    mshoesbtn = PhotoImage(file = f"images\\mshoesbtn.png")
    mshoes = Button(image = mshoesbtn,borderwidth = 0,highlightthickness = 0,command =lambda:[mshoesscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    mshoes.place(x =719, y = 379,width = 115,height = 169)

    maccessoriesbtn = PhotoImage(file = f"images\\maccessoriesbtn.png")
    maccessories = Button(image = maccessoriesbtn,borderwidth = 0,highlightthickness = 0,command =lambda:[maccessoriesscreen(),change_image(0,"stop")] ,relief = "flat",cursor="hand2")
    maccessories.place(x =856, y = 379,width = 115,height = 169)

    wbackbtn = PhotoImage(file = f"images\\wbackbtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[searchscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wback.place(x =17, y = 26,width = 54,height = 62)


    banner1 = ImageTk.PhotoImage(Image.open("images\\menscreenbanner1.png"))
    banner2 = ImageTk.PhotoImage(Image.open("images\\menscreenbanner2.png"))
    banner3 = ImageTk.PhotoImage(Image.open("images\\menscreenbanner3.png"))
    banner4 = ImageTk.PhotoImage(Image.open("images\\menscreenbanner4.png"))
    banner5 = ImageTk.PhotoImage(Image.open("images\\menscreenbanner5.png"))

    l=Label()
    l.place(x=20,y=103,height=227,width=960)
    banners=[banner1,banner2,banner3,banner4,banner5]
    def change_image(nextindex,value):
        global change
        if value=="continue":
            l.configure(image=banners[nextindex])
            change=window.after(2000, lambda: change_image((nextindex+1) % len(banners),"continue"))
        else:
            window.after_cancel(change)
        
    change_image(0,"continue")
    

def mtshirts():
    global mtshirtsbg,cartbtn,wbackbtn
    mtshirtscodes=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
    mtshirtsproducts=["mBlack Tshirt","mWhite Tshirt","mPrinted Tshirt","mStriped Tshirt","mBlue Tshirt","mSage Green Tshirt","mGreen Tshirt","mGray Tshirt","mYellow Hoodie","mOlive Green Tshirt"]
    
    mtshirtsprices=[765,835,699,699,859,590,759,899,1299,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    mtshirtsbg=PhotoImage(file=f"images\\mtshirts.png")
    background = canvas.create_image(500.0, 300.0,image=mtshirtsbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mtshirtscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(mtshirtscodes[i],mtshirtsproducts[i],clicked[i],mtshirtsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mtshirtscodes[i],clicked[i],string))
        mydb.commit()
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = mencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def mshirts():
    global mshirtsbg,cartbtn,wbackbtn
    mshirtscodes=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020]
    mshirtsproducts=["mBlack Shirt","mGray Shirt","mBlue Shirt","mOlive Green Shirt","mStriped Shirt","mWhite Shirt","mChecked Shirt","mGray Checked Shirt","mGreen Khaki Shirt","mB&W Shirt"]
    mshirtsprices=[1195,835,999,799,859,1390,1399,799,1090,999]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    mshirtsbg=PhotoImage(file=f"images\\mshirts.png")
    background = canvas.create_image(500.0, 300.0,image=mshirtsbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mshirtscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(mshirtscodes[i],mshirtsproducts[i],clicked[i],mshirtsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mshirtscodes[i],clicked[i],string))
        mydb.commit()

        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = mencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def mjeansscreen():
    global mjeansbg,cartbtn,wbackbtn
    mjeanscodes=[1021,1022,1023,1024,1025,1026,1027,1028,1029,1030]
    mjeansproducts=["mFaded Jeans","mBlack Jeans","mRipped Jeans","mBlack Jeans - 2","mGrey Jeans","mLight Blue Jeans","mRipped Jeans - 2","mDark Blue Jeans","mRipped Loose Fit","mSkinny Jeans"]
    mjeansprices=[1995,1635,2599,1799,1999,990,1575,1135,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    mjeansbg=PhotoImage(file=f"images\\mjeans.png")
    background = canvas.create_image(500.0, 300.0,image=mjeansbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mjeanscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(mjeanscodes[i],mjeansproducts[i],clicked[i],mjeansprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mjeanscodes[i],clicked[i],string))
        mydb.commit()
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = mencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def mpants():
    global mpantsbg,cartbtn,wbackbtn
    mpantscodes=[1031,1032,1033,1034,1035,1036,1037,1038,1039,1040]
    mpantsproducts=["mBrown Pants","mBlack Pants","mGray Pants","mWhite Pants","mBlue Trousers","mBlack Trouser","mOlive Pants","mOff-White Pants","mBlue Pants","mBlack Trouser 2"]
    mpantsprices=[2295,1180,1999,2699,1859,1390,1575,1835,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    mpantsbg=PhotoImage(file=f"images\\mpants.png")
    background = canvas.create_image(500.0, 300.0,image=mpantsbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mpantscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(mpantscodes[i],mpantsproducts[i],clicked[i],mpantsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mpantscodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = mencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def mtraditionalwear():
    global mtraditionalwearbg,cartbtn,wbackbtn
    mtraditionalwearcodes=[1041,1042,1043,1044,1045,1046,1047,1048,1049,1050]
    mtraditionalwearproducts=["mRed Kurta Set","mWhite Kurta Set","mMaroon Kurta Set","mTeal Kurta Set","mStriped Kurta Set","mBlue Kurta Set","mPink Kurta Set","mRed Kurta Set 2","mGreen Kurta Set","mWhite Kurta"]
    mtraditionalwearprices=[1295,835,999,699,859,1390,1575,835,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    mtraditionalwearbg=PhotoImage(file=f"images\\mtraditionalwear.png")
    background = canvas.create_image(500.0, 300.0,image=mtraditionalwearbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mtraditionalwearcodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(mtraditionalwearcodes[i],mtraditionalwearproducts[i],clicked[i],mtraditionalwearprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mtraditionalwearcodes[i],clicked[i],string))
        mydb.commit()
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = mencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def mshoesscreen():
    global mshoesbg,cartbtn,wbackbtn
    mshoescodes=[1051,1052,1053,1054,1055,1056,1057,1058,1059,1060]
    mshoesproducts=["mGreen Shoes","mBlack Nike","mWhite Shoes","mBlack Shoes","mB&W Shoes","mStriped Shoes","mBlue Shoes","mGray Shoes","mRed Shoes","mMaroon Shoes"]
    mshoesprices=[2199,1660,1999,1950,1859,1390,2499,1835,1799,1555]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    mshoesbg=PhotoImage(file=f"images\\mshoes.png")
    background = canvas.create_image(500.0, 300.0,image=mshoesbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mshoescodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(mshoescodes[i],mshoesproducts[i],clicked[i],mshoesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(mshoescodes[i],clicked[i],string))
        mydb.commit()
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = mencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def maccessoriesscreen():
    global maccessoriesbg,cartbtn,wbackbtn
    maccessoriescodes=[1061,1062,1063,1064,1065,1066,1067,1068,1069,1070]
    maccessoriesproducts=["mSilver Chain","mBelt&Wallet Set","mRed Tie Set","mBlack Shades","mSmart Watch","mGold Chain","mSilver Chain 2","mBlue Watch","mGold Rim Shades","mWhite Watch"]
    maccessoriesprices=[1295,835,999,699,859,1390,835,1575,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    maccessoriesbg=PhotoImage(file=f"images\\maccessories.png")
    background = canvas.create_image(500.0, 300.0,image=maccessoriesbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn2.png")
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(maccessoriescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(maccessoriescodes[i],maccessoriesproducts[i],maccessoriesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(maccessoriescodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 73, y = 266,width =136,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 254, y = 265,width =136,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 431, y = 265,width =136,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 608, y = 265,width =136,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 786, y = 265,width =136,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 73, y = 556,width =136,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 254, y = 556,width =136,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 431, y = 556,width =136,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 608, y = 556,width =136,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 786, y = 556,width =136,height = 16)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = mencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

#########################################WOMEN'S SECTION###########################################  
def womencategoryscreen():
    global switchbtn,womenscreen,dressesandjumpsuitsbtn,topsandteesbtn,traditionalsbtn,trouserbtn,shoesbtn,heelsandflatsbtn,sleepwearbtn,wbackbtn,background
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    womenscreen=PhotoImage(file=f"images\\womenscreen.png")
    background = canvas.create_image(500.0, 300.0,image=womenscreen)

    dressesandjumpsuitsbtn = PhotoImage(file = f"images\\dressesandjumpsuitsbtn.png")
    dressesandjumpsuits = Button(image = dressesandjumpsuitsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[wdresses(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    dressesandjumpsuits.place(x = 23, y = 380,width = 115,height = 169)

    topsandteesbtn = PhotoImage(file = f"images\\topsandteesbtn.png")
    topsandtees = Button(image = topsandteesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[wtops(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    topsandtees.place(x = 162, y = 380,width = 115,height = 169)

    traditionalsbtn = PhotoImage(file = f"images\\traditionalsbtn.png")
    traditionals = Button(image = traditionalsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[wtraditionals(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    traditionals.place(x = 302, y = 380,width = 115,height = 169)

    trouserbtn = PhotoImage(file = f"images\\trouserbtn.png")
    trouser = Button(image = trouserbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[wbottomwear(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    trouser.place(x =440, y = 380,width = 118,height = 170)

    shoesbtn = PhotoImage(file = f"images\\shoesbtn.png")
    shoes = Button(image = shoesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[wshoes(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    shoes.place(x =581, y = 380,width = 115,height = 169)

    heelsandflatsbtn = PhotoImage(file = f"images\\heelsandflatsbtn.png")
    heelsandflats = Button(image = heelsandflatsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[wheelsandflats(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    heelsandflats.place(x =720, y = 378,width = 116,height = 170)

    sleepwearbtn = PhotoImage(file = f"images\\sleepwearbtn.png")
    sleepwear = Button(image = sleepwearbtn,borderwidth = 0,highlightthickness = 0,command =lambda:[wsleepwear(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    sleepwear.place(x =861, y = 380,width = 115,height = 170)

    wbackbtn = PhotoImage(file = f"images\\wbackbtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[searchscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wback.place(x =17, y = 26,width = 54,height = 62)

    banner1 = ImageTk.PhotoImage(Image.open("images\\womenscreenbanner1.png"))
    banner2 = ImageTk.PhotoImage(Image.open("images\\womenscreenbanner2.png"))
    banner3 = ImageTk.PhotoImage(Image.open("images\\womenscreenbanner3.png"))
    banner4 = ImageTk.PhotoImage(Image.open("images\\womenscreenbanner4.png"))
    banner5 = ImageTk.PhotoImage(Image.open("images\\womenscreenbanner5.png"))

    l=Label()
    l.place(x=20,y=103,height=227,width=960)
    banners=[banner1,banner2,banner3,banner4,banner5]
    def change_image(nextindex,value):
        global change
        if value=="continue":
            l.configure(image=banners[nextindex])
            change=window.after(2000, lambda: change_image((nextindex+1) % len(banners),"continue"))
        else:
            window.after_cancel(change)
        
    change_image(0,"continue")

def wdresses():
    global wdressbg,cartbtn,wbackbtn
    wdresscodes=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
    wdressesproducts=["wBlack Dress","wFloral Dress","wBlazer Dress","wShirt Dress","wMaxi Dress","wGreen Dress","wWhite Dress","wPink Dress","wBlue Dress","wRed Dress"]
    wdressesprices=[1691,835,999,699,859,1390,1575,835,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    wdressbg=PhotoImage(file=f"images\\wdresses.png")
    background = canvas.create_image(500.0, 300.0,image=wdressbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wdresscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(wdresscodes[i],wdressesproducts[i],clicked[i],wdressesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wdresscodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = womencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)


def wtops():
    global wtopsbg,cartbtn,wbackbtn
    wtopscodes=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
    wtopsproducts=["wTie Dye Top","wOlive Top","wKnitted Top","wRed Top","wPlaid Shirt","wGrey Crop Top","wRed Dress","wWhite Top","wBlack Crop Top","wBlue Satin Top"]
    wtopsprices=[799,877,767,550,879,635,835,890,618,687]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    wtopsbg=PhotoImage(file=f"images\\wtops.png")
    background = canvas.create_image(500.0, 300.0,image=wtopsbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wtopscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(wtopscodes[i],wtopsproducts[i],clicked[i],wtopsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wtopscodes[i],clicked[i],string))
        mydb.commit()
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = womencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def wtraditionals():
    global wtraditionalsbg,cartbtn,wbackbtn
    wtraditionalscodes=[2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]
    wtraditionalsproducts=["wFloral Anarkali","wBlue Kurta Set","wGreen Kurta Set","wYellow Kurta Set","wRed Kurta Set","wGrey Anarkali","wBlue Lehenga","wYellow Kurta Set 2","wGreen Kurta Set 2","wWhite Anarkali"]
    wtraditionalsprices=[4355,1198,3249,4799,1079,3599,3875,2585,2859,4999]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    wtraditionalsbg=PhotoImage(file=f"images\\wtraditionals.png")
    background = canvas.create_image(500.0, 300.0,image=wtraditionalsbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wtraditionalscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(wtraditionalscodes[i],wtraditionalsproducts[i],clicked[i],wtraditionalsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wtraditionalscodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = womencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def wbottomwear():
    global wbottomwearbg,cartbtn,wbackbtn
    wbottomwearcodes=[2031,2032,2033,2034,2035,2036,2037,2038,2039,2040]
    wbottomwearproducts=["wRipped, Slimfit","wWide, Ripped","wWide, Black","wWide, Dark Blue","wStraight, Brown","wSlimfit, Dark","wWide, Dark Gray","wStraight, White","wWide, Purple","wStraight, Blue"]
    wbottomwearprices=[1023,1189,1259,1123,1323,1390,1192,1463,1192,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    wbottomwearbg=PhotoImage(file=f"images\\wbottomwear.png")
    background = canvas.create_image(500.0, 300.0,image=wbottomwearbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wbottomwearcodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(wbottomwearcodes[i],wbottomwearproducts[i],clicked[i],wbottomwearprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wbottomwearcodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = womencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def wshoes():
    global wshoesbg,cartbtn,wbackbtn
    wshoescodes=[2041,2042,2043,2044,2045,2046,2047,2048,2049,2050]
    wshoesproducts=["wPink Sneakers","wWhite Shoes","wBlue Shoes","wPink Shoes","wBlue Shoes 2","wBrown Shoes","wB&W Shoes","wWhite Shoes 2","wBlack Shoes","wGray Shoes"]
    wshoesprices=[1295,899,999,859,759,1390,1575,835,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    wshoesbg=PhotoImage(file=f"images\\wshoes.png")
    background = canvas.create_image(500.0, 300.0,image=wshoesbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wshoescodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(wshoescodes[i],wshoesproducts[i],clicked[i],wshoesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wshoescodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = womencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def wheelsandflats():
    global wheelsandflatsbg,cartbtn,wbackbtn
    wheelsandflatscodes=[2051,2052,2053,2054,2055,2056,2057,2058,2059,2060]
    wheelsandflatsproducts=["wFloral Flats","wBlack Boots","wBeige Heels","wPurple Sandals","wPink Heels","wBrown Sandals","wFloral Sandals","wStrappy Heels","wBlack Heels","wBlack Flats"]
    wheelsandflatsprices=[1295,1835,999,999,859,1390,1290,1305,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    wheelsandflatsbg=PhotoImage(file=f"images\\wheelsandflats.png")
    background = canvas.create_image(500.0, 300.0,image=wheelsandflatsbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wheelsandflatscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(wheelsandflatscodes[i],wheelsandflatsproducts[i],clicked[i],wheelsandflatsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wheelsandflatscodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = womencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def wsleepwear():
    global wsleepwearbg,cartbtn,wbackbtn
    wsleepwearcodes=[2061,2062,2063,2064,2065,2066,2067,2068,2069,2070]
    wsleepwearproducts=["wLeaves Suit Set","wMilkshakes Suit","wFloral Suits Set","wBallerinas Set","wPups Suit Set","wCastle Suit Set","wRed Suit Set","wGiraffe Suit Set","wBerries Suit Set","wYellow Suit Set"]
    wsleepwearprices=[1295,1835,999,699,859,1390,1575,835,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    wsleepwearbg=PhotoImage(file=f"images\\wsleepwear.png")
    background = canvas.create_image(500.0, 300.0,image=wsleepwearbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wsleepwearcodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(wsleepwearcodes[i],wsleepwearproducts[i],clicked[i],wsleepwearprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(wsleepwearcodes[i],clicked[i],string))
        mydb.commit()
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = womencategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)
    
#######################################KIDS SECTION#############################################
def kidscategoryscreen():
    global switchbtn, kidsscreen,tshirtsbtn,bottomwearbtn,traditionalwearbtn,preteensbtn,newbornbtn,footwearbtn,babycarebtn,wbackbtn,switchbtn,background
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    kidsscreen=PhotoImage(file=f"images\\kidsscreen.png")
    background = canvas.create_image(500.0, 300.0,image=kidsscreen)

    tshirtsbtn = PhotoImage(file = f"images\\ktshirtsbtn.png")
    tshirts = Button(image = tshirtsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[ktshirts(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    tshirts.place(x = 27, y = 379,width = 115,height = 169)

    bottomwearbtn = PhotoImage(file = f"images\\kbottomwearbtn.png")
    bottomwear = Button(image = bottomwearbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[kbottomwear(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    bottomwear.place(x = 163, y = 379,width = 115,height = 169)

    traditionalwearbtn = PhotoImage(file = f"images\\ktraditionalwearbtn.png")
    traditionalwear = Button(image = traditionalwearbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[ktraditionalwear(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    traditionalwear.place(x = 298, y = 378,width = 118,height = 170)

    preteensbtn = PhotoImage(file = f"images\\preteensbtn.png")
    preteens = Button(image = preteensbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[kpreteens(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    preteens.place(x =440, y = 378,width = 115,height = 169)

    newbornbtn = PhotoImage(file = f"images\\knewbornbtn.png")
    newborn = Button(image = newbornbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[knewborn(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    newborn.place(x =580, y = 379,width = 116,height = 171)

    footwearbtn = PhotoImage(file = f"images\\kfootwearbtn.png")
    footwear = Button(image = footwearbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[kfootwear(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    footwear.place(x =719, y = 379,width = 115,height = 169)

    babycarebtn = PhotoImage(file = f"images\\babycarebtn.png")
    babycare = Button(image = babycarebtn,borderwidth = 0,highlightthickness = 0,command = lambda:[kbabycare(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    babycare.place(x =856, y = 379,width = 115,height = 169)

    wbackbtn = PhotoImage(file = f"images\\wbackbtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[searchscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wback.place(x =17, y = 26,width = 54,height = 62)


    banner1 = ImageTk.PhotoImage(Image.open("images\\kidsscreenbanner1.png"))
    banner2 = ImageTk.PhotoImage(Image.open("images\\kidsscreenbanner2.png"))
    banner3 = ImageTk.PhotoImage(Image.open("images\\kidsscreenbanner3.png"))
    banner4 = ImageTk.PhotoImage(Image.open("images\\kidsscreenbanner4.png"))
    banner5 = ImageTk.PhotoImage(Image.open("images\\kidsscreenbanner5.png"))

    l=Label()
    l.place(x=20,y=103,height=227,width=960)
    banners=[banner1,banner2,banner3,banner4,banner5]
    def change_image(nextindex,value):
        global change
        if value=="continue":
            l.configure(image=banners[nextindex])
            change=window.after(2000, lambda: change_image((nextindex+1) % len(banners),"continue"))
        else:
            window.after_cancel(change)
        
    change_image(0,"continue")


def ktshirts():
    global ktshirtsbg,cartbtn,wbackbtn
    ktshirtscodes=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010]
    ktshirtsproducts=["kWhite Tee","kGray Tee","kBlack Tee","kPurple Tee","kFrilled Tee","kBlue Tee","kBrown Tee","kTeddy Sweatshirt","kPrinted Tee","kCropped Tee"]
    ktshirtsprices=[799,835,699,699,859,690,855,999,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    ktshirtsbg=PhotoImage(file=f"images\\ktshirts.png")
    background = canvas.create_image(500.0, 300.0,image=ktshirtsbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(ktshirtscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(ktshirtscodes[i],ktshirtsproducts[i],clicked[i],ktshirtsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(ktshirtscodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = kidscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def kbottomwear():
    global kbottomwearbg,cartbtn,wbackbtn
    kbottomwearcodes=[3011,3012,3013,3014,3015,3016,3017,3018,3019,3020]
    kbottomwearproducts=["kBrown Pants","kBrown Pants 2","kDenim Pants","kWide Jeans","kStriped Lowers","kBlack Pants","kGreen Pants","kChecked Bottoms","kPink Trousers","kDenim Bottoms"]
    kbottomwearprices=[799,835,949,699,859,1390,675,715,890,1099]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    kbottomwearbg=PhotoImage(file=f"images\\kbottomwear.png")
    background = canvas.create_image(500.0, 300.0,image=kbottomwearbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(kbottomwearcodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(kbottomwearcodes[i],kbottomwearproducts[i],clicked[i],kbottomwearprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(kbottomwearcodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = kidscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def ktraditionalwear():
    global ktraditionalwearbg,cartbtn,wbackbtn
    ktraditionalwearcodes=[3021,3022,3023,3024,3025,3026,3027,3028,3029,3030]
    ktraditionalwearproducts=["kDhoti Kurta","kRed Kurta Set","kPeach Kurti","kMint Kurta Set","kFloral Kurta Set","kYellow Kurta Set","kGrey Kurta Set","kBlue Kurta Set","kPatterns Set","kPink Dhoti Kurta"]
    ktraditionalwearprices=[1295,835,999,859,859,890,1575,835,1516,935]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    ktraditionalwearbg=PhotoImage(file=f"images\\ktraditionalwear.png")
    background = canvas.create_image(500.0, 300.0,image=ktraditionalwearbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(ktraditionalwearcodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(ktraditionalwearcodes[i],ktraditionalwearproducts[i],clicked[i],ktraditionalwearprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(ktraditionalwearcodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = kidscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def kpreteens():
    global kpreteensbg,cartbtn,wbackbtn
    kpreteenscodes=[3031,3032,3033,3034,3035,3036,3037,3038,3039,3040]
    kpreteensproducts=["kWhite Outfit","kLight Grey Outfit","kBlue Outfit","kGirls Denim Outfit","kOrange Outfit","kBoys Denim Outfit","kBrown Outfit","kGrey Outfit","kPink Outfit","kGreen Dress"]
    kpreteensprices=[1295,835,999,699,859,990,1575,835,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    kpreteensbg=PhotoImage(file=f"images\\kpreteens.png")
    background = canvas.create_image(500.0, 300.0,image=kpreteensbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(kpreteenscodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(kpreteenscodes[i],kpreteensproducts[i],clicked[i],kpreteensprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(kpreteenscodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = kidscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def knewborn():
    global knewbornbg,cartbtn,wbackbtn
    knewborncodes=[3041,3042,3043,3044,3045,3046,3047,3048,3049,3050]
    knewbornproducts=["kBlack Outfit","kDino Onesie","kWhite Dress","kPink Onesie","kGreen Onesie","kGrey Tunic Outfit","kGrey Outfit","kDenim Onesie","kPrinted Onesie","kFloral Outfit"]
    knewbornprices=[1295,835,999,699,859,1390,1575,835,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    knewbornbg=PhotoImage(file=f"images\\knewborn.png")
    background = canvas.create_image(500.0, 300.0,image=knewbornbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(knewborncodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(knewborncodes[i],knewbornproducts[i],clicked[i],knewbornprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(knewborncodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = kidscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def kfootwear():
    global kfootwearbg,cartbtn,wbackbtn
    kfootwearcodes=[3051,3052,3053,3054,3055,3056,3057,3058,3059,3060]
    kfootwearproducts=["kGreen Nikes","kBlue Shoes","kFloral Shoes","kBrown Sandals","kUnicorn Slippers","kBrown Shoes","kWhite Shoes","kBlack Shoes","kWhite Boots","kBlue Flats"]
    kfootwearprices=[1295,835,999,699,859,1390,1575,835,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    kfootwearbg=PhotoImage(file=f"images\\kfootwear.png")
    background = canvas.create_image(500.0, 300.0,image=kfootwearbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn1.png")
    def size(i):
        global clicked
        clicked=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get(),clicked5.get(),clicked6.get(),clicked7.get(),clicked8.get(),clicked9.get(),clicked10.get()]
    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(kfootwearcodes[i],clicked[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}','{}',1,{},'{}')".format(kfootwearcodes[i],kfootwearproducts[i],clicked[i],kfootwearprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND SIZE='{}' AND CUSTMAIL='{}'".format(kfootwearcodes[i],clicked[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    options=["XS", "S","M","L","XL"]
    clicked1=StringVar()
    clicked1.set("M")
    drop1= OptionMenu(canvas,clicked1,*options,command=size)
    drop1.configure(anchor='w')
    drop1.place(x=103,y=265,width = 40,height = 17)
    drop1.config(bg="WHITE", fg="BLACK")
    drop1["menu"].config(bg="white")
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 265,width =71,height = 16)

    clicked2=StringVar()
    clicked2.set("M")
    drop2= OptionMenu(canvas,clicked2,*options,command=size)
    drop2.configure(anchor='w')
    drop2.place(x=284,y=265,width = 40,height = 17)
    drop2.config(bg="WHITE", fg="BLACK")
    drop2["menu"].config(bg="white")
    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    clicked3=StringVar()
    clicked3.set("M")
    drop3= OptionMenu(canvas,clicked3,*options,command=size)
    drop3.configure(anchor='w')
    drop3.place(x=461,y=265,width = 40,height = 17)
    drop3.config(bg="WHITE", fg="BLACK")
    drop3["menu"].config(bg="white")
    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 265,width =71,height = 16)

    clicked4=StringVar()
    clicked4.set("M")
    drop4= OptionMenu(canvas,clicked4,*options,command=size)
    drop4.configure(anchor='w')
    drop4.place(x=638,y=265,width = 40,height = 17)
    drop4.config(bg="WHITE", fg="BLACK")
    drop4["menu"].config(bg="white")
    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 265,width =71,height = 16)

    clicked5=StringVar()
    clicked5.set("M")
    drop5= OptionMenu(canvas,clicked5,*options,command=size)
    drop5.configure(anchor='w')
    drop5.place(x=815,y=265,width = 40,height = 17)
    drop5.config(bg="WHITE", fg="BLACK")
    drop5["menu"].config(bg="white")
    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 856, y = 265,width =71,height = 16)
    
    clicked6=StringVar()
    clicked6.set("M")
    drop6= OptionMenu(canvas,clicked6,*options,command=size)
    drop6.configure(anchor='w')
    drop6.place(x=103,y=555,width = 40,height = 17)
    drop6.config(bg="WHITE", fg="BLACK")
    drop6["menu"].config(bg="white")
    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 555,width =71,height = 16)

    clicked7=StringVar()
    clicked7.set("M")
    drop7= OptionMenu(canvas,clicked7,*options,command=size)
    drop7.configure(anchor='w')
    drop7.place(x=284,y=555,width = 40,height = 17)
    drop7.config(bg="WHITE", fg="BLACK")
    drop7["menu"].config(bg="white")
    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 555,width =71,height = 16)

    clicked8=StringVar()
    clicked8.set("M")
    drop8= OptionMenu(canvas,clicked8,*options,command=size)
    drop8.configure(anchor='w')
    drop8.place(x=461,y=555,width = 40,height = 17)
    drop8.config(bg="WHITE", fg="BLACK")
    drop8["menu"].config(bg="white")
    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 555,width =71,height = 16)

    clicked9=StringVar()
    clicked9.set("M")
    drop9= OptionMenu(canvas,clicked9,*options,command=size)
    drop9.configure(anchor='w')
    drop9.place(x=638,y=555,width = 40,height = 17)
    drop9.config(bg="WHITE", fg="BLACK")
    drop9["menu"].config(bg="white")
    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 555,width =71,height = 16)

    clicked10=StringVar()
    clicked10.set("M")
    drop10= OptionMenu(canvas,clicked10,*options,command=size)
    drop10.configure(anchor='w')
    drop10.place(x=815,y=555,width = 40,height = 17)
    drop10.config(bg="WHITE", fg="BLACK")
    drop10["menu"].config(bg="white")
    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 856, y = 555,width =71,height = 16)

    size(1)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = kidscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def kbabycare():
    global kbabycarebg,cartbtn,wbackbtn
    kbabycarecodes=[3061,3062,3063,3064,3065,3066,3067,3068,3069,3070]
    kbabycareproducts=["kShampoo Set","kBaby Blanket","kCrib Set","kBowl&Spoon Set","kCar Seat","kCream Set","kBabycare Set","kBlue Diaper Bag","kPink Diaper Bag","kBlack Bag"]
    kbabycareprices=[1295,835,999,699,859,1390,1575,835,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    kbabycarebg=PhotoImage(file=f"images\\kbabycare.png")
    background = canvas.create_image(500.0, 300.0,image=kbabycarebg)
    cartbtn=PhotoImage(file=f"images\\cartbtn2.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(kbabycarecodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(kbabycarecodes[i],kbabycareproducts[i],kbabycareprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(kbabycarecodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 73, y = 266,width =136,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 254, y = 265,width =136,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 431, y = 265,width =136,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 608, y = 265,width =136,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 786, y = 265,width =136,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 73, y = 556,width =136,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 254, y = 556,width =136,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 431, y = 556,width =136,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 608, y = 556,width =136,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 786, y = 556,width =136,height = 16)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = kidscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

#######################################ACCESSORIES SECTION######################################
def acccategoryscreen():
    global switchbtn, accscreen,earringsbtn,jewelrybtn,bagsbtn,watchesbtn,beltsbtn,hairaccbtn,sunglassesbtn,wbackbtn,switchbtn,background
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    accscreen=PhotoImage(file=f"images\\accscreen.png")
    background = canvas.create_image(500.0, 300.0,image=accscreen)


    earringsbtn = PhotoImage(file = f"images\\earringsbtn.png")
    earrings = Button(image = earringsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[aearrings(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    earrings.place(x = 28, y = 379,width = 115,height = 169)

    jewelrybtn = PhotoImage(file = f"images\\jewelrybtn.png")
    jewelry = Button(image = jewelrybtn,borderwidth = 0,highlightthickness = 0,command = lambda:[ajewelery(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    jewelry.place(x = 165, y = 379,width = 115,height = 169)

    bagsbtn = PhotoImage(file = f"images\\bagsbtn.png")
    bags = Button(image = bagsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[abags(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    bags.place(x = 303, y = 379,width = 115,height = 169)

    watchesbtn = PhotoImage(file = f"images\\watchesbtn.png")
    watches = Button(image = watchesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[awatches(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    watches.place(x =440, y = 378,width = 118,height = 170)

    beltsbtn = PhotoImage(file = f"images\\beltsbtn.png")
    belts = Button(image = beltsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[abelts(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    belts.place(x =580, y = 379,width = 115,height = 169)

    hairaccbtn = PhotoImage(file = f"images\\hairaccbtn.png")
    hairacc = Button(image = hairaccbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[ahairacc(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    hairacc.place(x =718, y = 377,width = 116,height = 171)

    sunglassesbtn = PhotoImage(file = f"images\\sunglassesbtn.png")
    sunglasses = Button(image = sunglassesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[asunglasses(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    sunglasses.place(x =857, y = 379,width = 115,height = 169)

    wbackbtn = PhotoImage(file = f"images\\wbackbtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[searchscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wback.place(x =17, y = 26,width = 54,height = 62)


    banner1 = ImageTk.PhotoImage(Image.open("images\\accscreenbanner1.png"))
    banner2 = ImageTk.PhotoImage(Image.open("images\\accscreenbanner2.png"))
    banner3 = ImageTk.PhotoImage(Image.open("images\\accscreenbanner3.png"))
    banner4 = ImageTk.PhotoImage(Image.open("images\\accscreenbanner4.png"))
    banner5 = ImageTk.PhotoImage(Image.open("images\\accscreenbanner5.png"))

    l=Label()
    l.place(x=20,y=103,height=227,width=960)
    banners=[banner1,banner2,banner3,banner4,banner5]
    def change_image(nextindex,value):
        global change
        if value=="continue":
            l.configure(image=banners[nextindex])
            change=window.after(2000, lambda: change_image((nextindex+1) % len(banners),"continue"))
        else:
            window.after_cancel(change)
        
    change_image(0,"continue")

def aearrings():
    global aearringsbg,cartbtn,wbackbtn
    aearringscodes=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010]
    aearringsproducts=["aGold Drop Earrings","aSilver Feather Earrings","aRain Earrings","aNight & Day Earrings","aButterfly Earrings","aSnowflake Earrings","aBee Earrings","aStarry Shower Earrings","aPearl Drops Earrings","aQuirky Eye Earrings"]
    aearringsprices=[799,835,699,699,859,690,855,999,616,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    aearringsbg=PhotoImage(file=f"images\\aearrings.png")
    background = canvas.create_image(500.0, 300.0,image=aearringsbg)
    cartbtn=PhotoImage(file=f"images\\mcartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(aearringscodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(aearringscodes[i],aearringsproducts[i],aearringsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(aearringscodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 112, y = 266,width =105,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 293, y = 265,width =105,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 470, y = 266,width =105,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 647, y = 266,width =105,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 825, y = 265,width =105,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 112, y = 556,width =105,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 293, y = 556,width =105,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 470, y = 556,width =105,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 647, y = 556,width =105,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 825, y = 556,width =105,height = 16)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = acccategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def ajewelery():
    global ajewelerybg,cartbtn,wbackbtn
    ajewelerycodes=[4011,4012,4013,4014,4015,4016,4017,4018,4019,4020]
    ajeweleryproducts=["aSilver Camera Pendant","aGold V Necklace","aQuirky Rainbow Rings","aGold Toned Bracelets","aBracelets Set of 4","a Layered Necklace","aButterfly Layers","aVivid Blooms Chain","aRing Set of 4","aRings Set"]
    ajeweleryprices=[799,835,999,2099,859,690,855,599,716,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    ajewelerybg=PhotoImage(file=f"images\\ajewelery.png")
    background = canvas.create_image(500.0, 300.0,image=ajewelerybg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(ajewelerycodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(ajewelerycodes[i],ajeweleryproducts[i],ajeweleryprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(ajewelerycodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 825, y = 556,width =105,height = 16)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = acccategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def abags():
    global abagsbg,cartbtn,wbackbtn
    abagscodes=[4021,4022,4023,4024,4025,4026,4027,4028,4029,4030]
    abagsproducts=["aBlack Formal Sling","aWhite Floral Sling","aPastel Bag Set","aPink Chained Sling","aBaby Blue Bagpack","aBeige Handbag","aSee Through Bagpack","aBlack Belted Bagpack","aDaisy Tote Bag","aTote Bag Set of 3"]
    abagsprices=[2799,2835,4099,1519,959,1690,1125,999,816,2035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    abagsbg=PhotoImage(file=f"images\\abags.png")
    background = canvas.create_image(500.0, 300.0,image=abagsbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(abagscodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(abagscodes[i],abagsproducts[i],abagsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(abagscodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 825, y = 556,width =105,height = 16)
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = acccategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)
    
def awatches():
    global awatchesbg,cartbtn,wbackbtn
    awatchescodes=[4031,4032,4033,4034,4035,4036,4037,4038,4039,4040]
    awatchesproducts=["aGreen Watch","aBaby Pink Watch","aRed Watch","aWorld Map Watch","aRose Gold Watch","aWhite Watch","aGrey Watch","aGold Watch","aBlack Dial Watch","aCrystal Dial Watch"]
    awatchesprices=[3999,1199,2999,7100,3859,2790,3550,2999,1516,1110]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    awatchesbg=PhotoImage(file=f"images\\awatches.png")
    background = canvas.create_image(500.0, 300.0,image=awatchesbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn2.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(awatchescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(awatchescodes[i],awatchesproducts[i],awatchesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(awatchescodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 73, y = 266,width =136,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 254, y = 265,width =136,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 431, y = 265,width =136,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 608, y = 265,width =136,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 786, y = 265,width =136,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 73, y = 556,width =136,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 254, y = 556,width =136,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 431, y = 556,width =136,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 608, y = 556,width =136,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 786, y = 556,width =136,height = 16)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = acccategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def abelts():
    global abeltsbg,cartbtn,wbackbtn,mcartbtn
    abeltscodes=[4041,4042,4043,4044,4045,4046,4047,4048,4049,4050]
    abeltsproducts=["aWhite Belt","aSkinny Knot Belt","aCircle&Bar Toggle Belt","aSkinny Knot Belt 2","aThin Brown Belt","aCorset Belt","aCream Belt","aPink Belt","aBlack Belt","aPearls Belt"]
    abeltsprices=[1099,565,899,699,859,1599,765,999,1260,762]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    abeltsbg=PhotoImage(file=f"images\\abelts.png")
    background = canvas.create_image(500.0, 300.0,image=abeltsbg)
    cartbtn=PhotoImage(file=f"images\\cartbtn2.png")
    mcartbtn=PhotoImage(file=f"images\\mcartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(abeltscodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(abeltscodes[i],abeltsproducts[i],abeltsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(abeltscodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 73, y = 266,width =136,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 254, y = 265,width =136,height = 16)

    wd3 = Button(image = mcartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 470, y = 266,width =105,height = 16)

    wd4 = Button(image = mcartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 647, y = 266,width =105,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 786, y = 265,width =136,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 73, y = 556,width =136,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 254, y = 556,width =136,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 431, y = 556,width =136,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 608, y = 556,width =136,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 786, y = 556,width =136,height = 16)

    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = acccategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def ahairacc():
    global ahairaccbg,cartbtn,wbackbtn
    ahairacccodes=[4051,4052,4053,4054,4055,4056,4057,4058,4059,4060]
    ahairaccproducts=["aBlue Scrunchy Set of 2","aHair Ties Set of 4","aClaw Clips Set of 3","aHair Clips Set of 8","aScrunchy Set of 2","aScrunchy Set of 3","aButterfly Claw Clip","aPink Claw Clip","aClaw Clip Set of 4","aHair Clips Set of 4"]
    ahairaccprices=[40,50,120,80,40,60,60,75,250,50]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    ahairaccbg=PhotoImage(file=f"images\\ahairacc.png")
    background = canvas.create_image(500.0, 300.0,image=ahairaccbg)
    cartbtn=PhotoImage(file=f"images\\mcartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(ahairacccodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(ahairacccodes[i],ahairaccproducts[i],ahairaccprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(ahairacccodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 112, y = 266,width =105,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 293, y = 265,width =105,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 470, y = 266,width =105,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 647, y = 266,width =105,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 825, y = 265,width =105,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 112, y = 556,width =105,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 293, y = 556,width =105,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 470, y = 556,width =105,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 647, y = 556,width =105,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 825, y = 556,width =105,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = acccategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def asunglasses():
    global asunglassesbg,cartbtn,wbackbtn,mcartbtn
    asunglassescodes=[4061,4062,4063,4064,4065,4066,4067,4068,4069,4070]
    asunglassesproducts=["aPink Shades","aDark Brown Shades","aBlack Shades","aPink Panto Shades","aAnimal Print Shades","aBlack Gold Rim Shades","aRed Shades","aGreen Shades","aBlack Wayfarer Shades","aDark Grey Shades"]
    asunglassesprices=[2010,1935,2699,1549,1369,2190,1855,1599,1516,1035]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    asunglassesbg=PhotoImage(file=f"images\\asunglasses.png")
    background = canvas.create_image(500.0, 300.0,image=asunglassesbg)
    cartbtn=PhotoImage(file=f"images\\mcartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(asunglassescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(asunglassescodes[i],asunglassesproducts[i],asunglassesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(asunglassescodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 112, y = 266,width =105,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 293, y = 265,width =105,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 470, y = 266,width =105,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 647, y = 266,width =105,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 825, y = 265,width =105,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 112, y = 556,width =105,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 293, y = 556,width =105,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 470, y = 556,width =105,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 647, y = 556,width =105,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 825, y = 556,width =105,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = acccategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)


#################################ELECTRONICS SECTION#################################################
def electronicscategoryscreen():
    global switchbtn, electronicsscreen,phonesbtn,tabletsbtn,laptopsbtn,tvbtn,headphonesbtn,speakersbtn,accessoriesbtn,wbackbtn,switchbtn,background
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    electronicsscreen=PhotoImage(file=f"images\\electronicsscreen.png")
    background = canvas.create_image(500.0, 300.0,image=electronicsscreen)

    phonesbtn = PhotoImage(file = f"images\\phonesbtn.png")
    phones = Button(image = phonesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[ephones(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    phones.place(x = 28, y = 379,width = 115,height = 169)

    tabletsbtn = PhotoImage(file = f"images\\tabletsbtn.png")
    tablets = Button(image = tabletsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[etablets(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    tablets.place(x = 165, y = 379,width = 115,height = 169)

    laptopsbtn = PhotoImage(file = f"images\\laptopsbtn.png")
    laptops = Button(image = laptopsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[elaptops(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    laptops.place(x = 303, y = 379,width = 115,height = 169)

    tvbtn = PhotoImage(file = f"images\\tvbtn.png")
    tv = Button(image = tvbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[etv(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    tv.place(x =440, y = 378,width = 118,height = 170)

    headphonesbtn = PhotoImage(file = f"images\\headphonesbtn.png")
    headphones = Button(image = headphonesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[eheadphones(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    headphones.place(x =580, y = 379,width = 115,height = 169)

    speakersbtn = PhotoImage(file = f"images\\speakersbtn.png")
    speakers = Button(image = speakersbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[espeakers(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    speakers.place(x =718, y = 377,width = 116,height = 171)

    accessoriesbtn = PhotoImage(file = f"images\\accessoriesbtn.png")
    accessories= Button(image = accessoriesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[eaccessories(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    accessories.place(x =857, y = 379,width = 115,height = 169)

    wbackbtn = PhotoImage(file = f"images\\wbackbtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[searchscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wback.place(x =17, y = 26,width = 54,height = 62)

    banner1 = ImageTk.PhotoImage(Image.open("images\\electronicsscreenbanner1.png"))
    banner2 = ImageTk.PhotoImage(Image.open("images\\electronicsscreenbanner2.png"))
    banner3 = ImageTk.PhotoImage(Image.open("images\\electronicsscreenbanner3.png"))
    banner4 = ImageTk.PhotoImage(Image.open("images\\electronicsscreenbanner4.png"))
    banner5 = ImageTk.PhotoImage(Image.open("images\\electronicsscreenbanner5.png"))

    l=Label()
    l.place(x=20,y=103,height=227,width=960)
    banners=[banner1,banner2,banner3,banner4,banner5]
    def change_image(nextindex,value):
        global change
        if value=="continue":
            l.configure(image=banners[nextindex])
            change=window.after(2000, lambda: change_image((nextindex+1) % len(banners),"continue"))
        else:
            window.after_cancel(change)
        
    change_image(0,"continue")

def ephones():
    global ephonesbg,cartbtn,wbackbtn,mcartbtn
    ephonescodes=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010]
    ephonesproducts=["eGalaxy S22 Ultra 5G","eGalaxy Z Flip 4","eiPhone 14 Pro","eiPhone 14","eiPhone 14 Plus - Red","eVivo T1 Pro 5G","eRealme Narzo 50i","eMi 12 Pro 5G","eiPhone 14 Pro Max","eiPhone 14 Plus - Blue"]
    ephonesprices=[108999,101999,129300,79990,89990,24999,9990,54999,139900,89990]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    ephonesbg=PhotoImage(file=f"images\\ephones.png")
    background = canvas.create_image(500.0, 300.0,image=ephonesbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(ephonescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(ephonescodes[i],ephonesproducts[i],ephonesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(ephonescodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = electronicscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def etablets():
    global etabletsbg,cartbtn,wbackbtn,mcartbtn
    etabletscodes=[5011,5012,5013,5014,5015,5016,5017,5018,5019,5020]
    etabletsproducts=["eGalaxy Tab A8 Black","eApple iPad 9th Gen","eGalaxy Tab S6 Lite","eGalaxy Tab A8 Pink","eSamsung Galaxy Tab S8+","eOppo Pad Air Grey","eGalaxy Tab A7 Black","eGalaxy Tab A7 White","eNokia T20","eRealme Pad Mini"]
    etabletsprices=[14999,29900,25999,14900,11990,16999,12990,37999,18499,10990]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    etabletsbg=PhotoImage(file=f"images\\etablets.png")
    background = canvas.create_image(500.0, 300.0,image=etabletsbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(etabletscodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(etabletscodes[i],etabletsproducts[i],etabletsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(etabletscodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = electronicscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def elaptops():
    global elaptopsbg,cartbtn,wbackbtn,mcartbtn
    elaptopscodes=[5021,5022,5023,5024,5025,5026,5027,5028,5029,5030]
    elaptopsproducts=["eEnvy 13 Convertible","eGalaxy Book 2 Pro 360","ePavilion x360 Convertible","eDell Inspiron 16","eLenevo Legion 5 Pro","eLenevo Ideapad 3","eLenevo Thinkpad L13","eLenevo Yoga Slim","eHP Pavilion","eASUS VivoBook Flip 14"]
    elaptopsprices=[83499,125000,85999,85999,140690,29999,83690,75990,139900,32990]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    elaptopsbg=PhotoImage(file=f"images\\elaptops.png")
    background = canvas.create_image(500.0, 300.0,image=elaptopsbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(elaptopscodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(elaptopscodes[i],elaptopsproducts[i],elaptopsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(elaptopscodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = electronicscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def etv():
    global etvbg,cartbtn,wbackbtn,mcartbtn
    etvcodes=[5031,5032,5033,5034,5035,5036,5037,5038,5039,5040]
    etvproducts=["eSamsung Neo QLED","eMi Qled UHD Smart Tv","eSony Bravia UHD TV","eRedmi Smart TV","eXiaomi Smart TV","eSamsung Series 7","eSony X80K Series TV","eSamsung The Frame Qled","eRealme Smart TV","eLG HD Ready Smart TV"]
    etvprices=[98499,59999,380000,59999,13999,47990,85490,75990,39900,15990]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    etvbg=PhotoImage(file=f"images\\etv.png")
    background = canvas.create_image(500.0, 300.0,image=etvbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(etvcodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(etvcodes[i],etvproducts[i],etvprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(etvcodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = electronicscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def eheadphones():
    global eheadphonesbg,cartbtn,wbackbtn,mcartbtn
    eheadphonescodes=[5041,5042,5043,5044,5045,5046,5047,5048,5049,5050]
    eheadphonesproducts=["eboAt Rockerz 650 Teal","eboAt Nirvanaa 751 ANC","eboAt Rockerz 450 Pro","eboAt Superior Rockerz ","eboAt Rockerz 650 Red","eboAt Rockerz 550","eApple AirPods Max","eboAt Rockerz 370","eboAt Immortal","eboAt Rockerz 450"]
    eheadphonesprices=[1799,3999,1800,1299,1799,1999,59900,1999,2642,3990]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    eheadphonesbg=PhotoImage(file=f"images\\eheadphones.png")
    background = canvas.create_image(500.0, 300.0,image=eheadphonesbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(eheadphonescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(eheadphonescodes[i],eheadphonesproducts[i],eheadphonesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(eheadphonescodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = electronicscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def espeakers():
    global espeakersbg,cartbtn,wbackbtn,mcartbtn
    espeakerscodes=[5051,5052,5053,5054,5055,5056,5057,5058,5059,5060]
    espeakersproducts=["eboAt Stone 350 T","eboAt Stone SpinX 2.0","eboAt Stone 1500","eJBL Flip Essential ","eboAt stone 1350","eboAt Stone 350 T","eJBL Go 3","eMarshall Willen Wireless","eJBL Flip 5","eboAt Stone 1010"]
    espeakersprices=[1699,3999,6990,5299,4799,1999,3699,9999,6538,2690]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    espeakersbg=PhotoImage(file=f"images\\espeakers.png")
    background = canvas.create_image(500.0, 300.0,image=espeakersbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(espeakerscodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(espeakerscodes[i],espeakersproducts[i],espeakersprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(espeakerscodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = electronicscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)


def eaccessories():
    global eaccessoriesbg,cartbtn,wbackbtn,mcartbtn
    eaccessoriescodes=[5061,5062,5063,5064,5065,5066,5067,5068,5069,5070]
    eaccessoriesproducts=["eMiniso Type-C Cable","eMiniso Power Bank","eLogitech POP Mouse ","eHP 32 GB Flash drive ","eMi LED Light Blue","eMiniso Type-C Cable 2","eOnePlus Power Bank","eLogitech POP Keyboard","eHP Wireless Mouse","eHDMI Cable 10 M"]
    eaccessoriesprices=[800,1099,2499,329,99,999,1030,9785,899,525]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    eaccessoriesbg=PhotoImage(file=f"images\\eaccessories.png")
    background = canvas.create_image(500.0, 300.0,image=eaccessoriesbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(eaccessoriescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(eaccessoriescodes[i],eaccessoriesproducts[i],eaccessoriesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(eaccessoriescodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = electronicscategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

######################################BEAUTY SECTION#########################################
def beautycategoryscreen():
    global switchbtn, beautyscreen,makeupbtn,skincarebtn,perfumesbtn,haircarebtn,appliancesbtn,babbtn,wbackbtn,switchbtn,background
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    beautyscreen=PhotoImage(file=f"images\\beautyscreen.png")
    background = canvas.create_image(500.0, 300.0,image=beautyscreen)

    makeupbtn = PhotoImage(file = f"images\\makeupbtn.png")
    makeup = Button(image = makeupbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[bmakeup(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    makeup.place(x = 50, y = 379,width = 115,height = 169)

    skincarebtn = PhotoImage(file = f"images\\skincarebtn.png")
    skincare = Button(image = skincarebtn,borderwidth = 0,highlightthickness = 0,command = lambda:[bskincare(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    skincare.place(x = 207, y = 379,width = 115,height = 169)

    perfumesbtn = PhotoImage(file = f"images\\perfumesbtn.png")
    perfumes = Button(image = perfumesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[bperfumes(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    perfumes.place(x = 362, y = 379,width = 115,height = 169)

    haircarebtn = PhotoImage(file = f"images\\haircarebtn.png")
    haircare = Button(image = haircarebtn,borderwidth = 0,highlightthickness = 0,command = lambda:[bhaircare(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    haircare.place(x =520, y = 379,width = 115,height = 169)

    appliancesbtn = PhotoImage(file = f"images\\appliancesbtn.png")
    appliances = Button(image = appliancesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[bappliances(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    appliances.place(x =674, y = 379,width = 118,height = 170)

    babbtn = PhotoImage(file = f"images\\babbtn.png")
    bab = Button(image = babbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[bbathandbody(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    bab.place(x =834, y = 377,width = 116,height = 171)

    wbackbtn = PhotoImage(file = f"images\\wbackbtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[searchscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wback.place(x =17, y = 26,width = 54,height = 62)


    banner1 = ImageTk.PhotoImage(Image.open("images\\beautyscreenbanner1.png"))
    banner2 = ImageTk.PhotoImage(Image.open("images\\beautyscreenbanner2.png"))
    banner3 = ImageTk.PhotoImage(Image.open("images\\beautyscreenbanner3.png"))
    banner4 = ImageTk.PhotoImage(Image.open("images\\beautyscreenbanner4.png"))
    banner5 = ImageTk.PhotoImage(Image.open("images\\beautyscreenbanner5.png"))

    l=Label()
    l.place(x=20,y=103,height=227,width=960)
    banners=[banner1,banner2,banner3,banner4,banner5]
    def change_image(nextindex,value):
        global change
        if value=="continue":
            l.configure(image=banners[nextindex])
            change=window.after(2000, lambda: change_image((nextindex+1) % len(banners),"continue"))
        else:
            window.after_cancel(change)
        
    change_image(0,"continue")

def bmakeup():
    global bmakeupbg,cartbtn,wbackbtn,mcartbtn
    bmakeupcodes=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010]
    bmakeupproducts=["bPink Liquid Lipstick","bMousse Foundation","bLiquid Eyeliner","bMARS Blush+ Palette","bMatte Compact","bIconic Red Lipstick","bFit Me Foundation","bWaterproof Eyeliner","bMaybelline Mascara","bEyeshadow Palatte"]
    bmakeupprices=[578,136,187,299,299,428,224,299,295,660]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    bmakeupbg=PhotoImage(file=f"images\\bmakeup.png")
    background = canvas.create_image(500.0, 300.0,image=bmakeupbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(bmakeupcodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(bmakeupcodes[i],bmakeupproducts[i],bmakeupprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(bmakeupcodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = beautycategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def bskincare():
    global bskincarebg,cartbtn,wbackbtn,mcartbtn
    bskincarecodes=[6011,6012,6013,6014,6015,6016,6017,6018,6019,6020]
    bskincareproducts=["bNiacinamide 10% Serum","bRetinol Serum","bFace Roller&Gua Sha(RQ)","bPlum Moisturizer","bMicellar Cleansing Water","bPlum Vitamin C Serum","bHyaluronic Acid Serum","bJade Face Roller ","bPlum Night Gel","bLakme Cleansing Milk"]
    bskincareprices=[800,388,1049,355,4799,711,363,1999,188,290]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    bskincarebg=PhotoImage(file=f"images\\bskincare.png")
    background = canvas.create_image(500.0, 300.0,image=bskincarebg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(bskincarecodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(bskincarecodes[i],bskincareproducts[i],bskincareprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(bskincarecodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = beautycategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def bperfumes():
    global bperfumesbg,cartbtn,wbackbtn,mcartbtn
    bperfumescodes=[6021,6022,6023,6024,6025,6026,6027,6028,6029,6030]
    bperfumesproducts=["bRose Perfume","bScent Tulip","bFresh Perfume","bBloom Perfume","bFreeland Perfume","bGlam Perfume","bPerfume Set","bWhite Perfume ","bRose Gold Perfume","bHoney Perfume"]
    bperfumesprices=[580,499,580,499,799,580,3699,580,6538,580]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    bperfumesbg=PhotoImage(file=f"images\\bperfumes.png")
    background = canvas.create_image(500.0, 300.0,image=bperfumesbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(bperfumescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(bperfumescodes[i],bperfumesproducts[i],bperfumesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(bperfumescodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = beautycategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)


def bhaircare():
    global bhaircarebg,cartbtn,wbackbtn,mcartbtn
    bhaircarecodes=[6031,6032,6033,6034,6035,6036,6037,6038,6039,6040]
    bhaircareproducts=["bOnion Hair Oil","bmCaffeine Hair Mask","bL’oreal Hair Serum","bVega Round Brush","bVega Paddle Brush","bCastor Oil for Hair","bTRESemme Hair Mask","bMatrix Hair Serum ","bVega Cushion Brush","bVega Hair Comb"]
    bhaircareprices=[347,509,413,299,499,215,595,500,358,240]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    bhaircarebg=PhotoImage(file=f"images\\bhaircare.png")
    background = canvas.create_image(500.0, 300.0,image=bhaircarebg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(bhaircarecodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(bhaircarecodes[i],bhaircareproducts[i],bhaircareprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(bhaircarecodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = beautycategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def bappliances():
    global bappliancesbg,cartbtn,wbackbtn,mcartbtn
    bappliancescodes=[6041,6042,6043,6044,6045,6046,6047,6048,6049,6050]
    bappliancesproducts=["bDyson Hair Dryer","bPhillips Straigthener","bDyson Corrale","bVega Hair Styling Kit","bDyson Straightener","bPhillips Hair Dryer","bPhils Straightening Comb","bVega 3 in 1 Hair Styler","bPhillips Advanced","bVega Wet&Dry Styler"]
    bappliancesprices=[34900,2699,32900,5299,24799,2542,3699,1299,1438,2690]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    bappliancesbg=PhotoImage(file=f"images\\bappliances.png")
    background = canvas.create_image(500.0, 300.0,image=bappliancesbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(bappliancescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(bappliancescodes[i],bappliancesproducts[i],bappliancesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(bappliancescodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = beautycategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)


def bbathandbody():
    global bbathandbodybg,cartbtn,wbackbtn,mcartbtn
    bbathandbodycodes=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060]
    bbathandbodyproducts=["bSea Salt Shower Gel","bBritish Rose Shower Gel","bHyalurone Shampoo","bWOW Vit-C Face Wash","bmCaffeine Body Scrub","bLavender Conditioner","bTRESemme Shampoo","bL’OREAL Shampoo","bNivea Milk Face Wash","bFace & Body Scrub"]
    bbathandbodyprices=[300,309,299,299,499,260,150,699,120,269]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    bbathandbodybg=PhotoImage(file=f"images\\bbathandbody.png")
    background = canvas.create_image(500.0, 300.0,image=bbathandbodybg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(bbathandbodycodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(bbathandbodycodes[i],bbathandbodyproducts[i],bbathandbodyprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(bbathandbodycodes[i],string))
        mydb.commit() 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = beautycategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

######################################HOME AND LIVING SECTION#########################################
def hnlcategoryscreen():
    global switchbtn, hnlscreen,bedbtn,homedecorbtn,lampsbtn,flooringbtn,kitchenbtn,bathbtn,cushionsbtn,wbackbtn,switchbtn,background
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    hnlscreen=PhotoImage(file=f"images\\hnlscreen.png")
    background = canvas.create_image(500.0, 300.0,image=hnlscreen)
    
    bedbtn = PhotoImage(file = f"images\\bedbtn.png")
    bed = Button(image = bedbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[hbedlinenandfurnishing(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    bed.place(x = 28, y = 379,width = 115,height = 169)

    homedecorbtn = PhotoImage(file = f"images\\homedecorbtn.png")
    homedecor = Button(image = homedecorbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[hhomedecor(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    homedecor.place(x = 165, y = 379,width = 115,height = 169)

    lampsbtn = PhotoImage(file = f"images\\lampsbtn.png")
    lamps = Button(image = lampsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[hlampsandlighting(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    lamps.place(x = 303, y = 379,width = 115,height = 169)

    flooringbtn = PhotoImage(file = f"images\\flooringbtn.png")
    flooring = Button(image = flooringbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[hflooring(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    flooring.place(x =440, y = 378,width = 118,height = 170)

    kitchenbtn = PhotoImage(file = f"images\\kitchenbtn.png")
    kitchen = Button(image = kitchenbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[hkitchenandtable(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    kitchen.place(x =580, y = 379,width = 115,height = 169)

    bathbtn = PhotoImage(file = f"images\\bathbtn.png")
    bath = Button(image = bathbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[hbath(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    bath.place(x =718, y = 377,width = 116,height = 171)

    cushionsbtn = PhotoImage(file = f"images\\cushionsbtn.png")
    cushions = Button(image = cushionsbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[hcushionsandcurtains(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    cushions.place(x =857, y = 379,width = 115,height = 171)

    wbackbtn = PhotoImage(file = f"images\\wbackbtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[searchscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wback.place(x =17, y = 26,width = 54,height = 62)

    banner1 = ImageTk.PhotoImage(Image.open("images\\hnlscreenbanner1.png"))
    banner2 = ImageTk.PhotoImage(Image.open("images\\hnlscreenbanner2.png"))
    banner3 = ImageTk.PhotoImage(Image.open("images\\hnlscreenbanner3.png"))
    banner4 = ImageTk.PhotoImage(Image.open("images\\hnlscreenbanner4.png"))
    banner5 = ImageTk.PhotoImage(Image.open("images\\hnlscreenbanner5.png"))

    l=Label()
    l.place(x=20,y=103,height=227,width=960)
    banners=[banner1,banner2,banner3,banner4,banner5]
    def change_image(nextindex,value):
        global change
        if value=="continue":
            l.configure(image=banners[nextindex])
            change=window.after(2000, lambda: change_image((nextindex+1) % len(banners),"continue"))
        else:
            window.after_cancel(change)
        
    change_image(0,"continue")

def hbedlinenandfurnishing():
    global hbedlinenandfurnishingbg,cartbtn,wbackbtn,mcartbtn
    hbedlinenandfurnishingcodes=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010]
    hbedlinenandfurnishingproducts=["hSquares Sheet Set","hGradient Sheet Set","hPink Sheet Set","hDual Color Comforter","hLeaves Sheet Set","hWhite Bedding Set","hReversible Bed Cover","hSpace Sheet Set","hCotton Woven Cover","hBlue Bed Linen"]
    hbedlinenandfurnishingprices=[2231,1099,1990,2999,1799,3600,1277,9999,1990,1299]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    hbedlinenandfurnishingbg=PhotoImage(file=f"images\\hbedlinenandfurnishing.png")
    background = canvas.create_image(500.0, 300.0,image=hbedlinenandfurnishingbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(hbedlinenandfurnishingcodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(hbedlinenandfurnishingcodes[i],hbedlinenandfurnishingproducts[i],hbedlinenandfurnishingprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(hbedlinenandfurnishingcodes[i],string))
        
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = hnlcategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def hhomedecor():
    global hhomedecorbg,cartbtn,wbackbtn,mcartbtn
    hhomedecorcodes=[7011,7012,7013,7014,7015,7016,7017,7018,7019,7020]
    hhomedecorproducts=[ "hDeer Showpieces","hDecorative Tree","hPineapple Decor","hReindeer Clock","hPeacock Wall Art","hWall Frame Set","hMetal Art","hTree of Life","hTabletop Bell","hPeach Globe"]
    hhomedecorprices=[199,360,299,1879,7499,499,6000,11700,3650,1499]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    hhomedecorbg=PhotoImage(file=f"images\\hhomedecor.png")
    background = canvas.create_image(500.0, 300.0,image=hhomedecorbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(hhomedecorcodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(hhomedecorcodes[i],hhomedecorproducts[i],hhomedecorprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(hhomedecorcodes[i],string))
         
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = hnlcategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def hlampsandlighting():
    global hlampsandlightingbg,cartbtn,wbackbtn,mcartbtn
    hlampsandlightingcodes=[7021,7022,7023,7024,7025,7026,7027,7028,7029,7030]
    hlampsandlightingproducts=["hWorld Map Lights","hBrass Study Lamp","hShelf Floor Lamp","hCeramic Table Lamp","hTripod Floor Lamp","hPhotoclip LED String Light","hLantern String Lights","hBamboo Fairy Lights","hFlower Fairy Lights","hDreamy Fairy Lights"]
    hlampsandlightingprices=[4999,2221,3667,699,4118,399,499,2800,169,800]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    hlampsandlightingbg=PhotoImage(file=f"images\\hlampsandlighting.png")
    background = canvas.create_image(500.0, 300.0,image=hlampsandlightingbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(hlampsandlightingcodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(hlampsandlightingcodes[i],hlampsandlightingproducts[i],hlampsandlightingprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(hlampsandlightingcodes[i],string))
 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = hnlcategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def hflooring():
    global hflooringbg,cartbtn,wbackbtn,mcartbtn
    hflooringcodes=[7031,7032,7033,7034,7035,7036,7037,7038,7039,7040]
    hflooringproducts=["hMarble Flooring","hFloor Decking","hTimber Flooring","hNatural Wooden Flooring","hLaminate Flooring","hRio Wood Tiles","hMoroccan Ceramic Tiles","hJute Fibre Flooring","hCarpet Tiles","hFloor Carpet"]
    hflooringprices=[2968,2450,347,1780,1894,1271,1199,2010,1500,4399]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    hflooringbg=PhotoImage(file=f"images\\hflooring.png")
    background = canvas.create_image(500.0, 300.0,image=hflooringbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(hflooringcodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(hflooringcodes[i],hflooringproducts[i],hflooringprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(hflooringcodes[i],string))
 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = hnlcategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)


def hkitchenandtable():
    global hkitchenandtablebg,cartbtn,wbackbtn,mcartbtn
    hkitchenandtablecodes=[7041,7042,7043,7044,7045,7046,7047,7048,7049,7050]
    hkitchenandtableproducts=["hWooden Study Table","hBrown Coffee Table","hWalnut Coffee Table","hCenter Table","hConference Table","hCrockery Rack","hChimney Hood","hInduction Cooktop","hKitchen Blenders","hDining Table Set"]
    hkitchenandtableprices=[5719,1199,5426,3000,69550,14831,17900,2010,12571,69699]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    hkitchenandtablebg=PhotoImage(file=f"images\\hkitchenandtable.png")
    background = canvas.create_image(500.0, 300.0,image=hkitchenandtablebg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(hkitchenandtablecodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(hkitchenandtablecodes[i],hkitchenandtableproducts[i],hkitchenandtableprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(hkitchenandtablecodes[i],string))
        
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = hnlcategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def hbath():
    global hbathbg,cartbtn,wbackbtn,mcartbtn
    hbathcodes=[7051,7052,7053,7054,7055,7056,7057,7058,7059,7060]
    hbathproducts=["hBlue Towels Set of 4","hBlack Designer Bath Set","hFrench Scented Candles","hHandmade Soaps","hBathroom Plant","hBrown Striped Towel","hSoap Dispenser Set of 4","hScented Candles Set","hLeaf Soap Stand","hSucculents Set of 4"]
    hbathprices=[2659,4450,990,899,799,799,2699,1299,538,2690]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    hbathbg=PhotoImage(file=f"images\\hbath.png")
    background = canvas.create_image(500.0, 300.0,image=hbathbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(hbathcodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(hbathcodes[i],hbathproducts[i],hbathprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(hbathcodes[i],string))
     
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = hnlcategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def hcushionsandcurtains():
    global hcushionsandcurtainsbg,cartbtn,wbackbtn,mcartbtn
    hcushionsandcurtainscodes=[7061,7062,7063,7064,7065,7066,7067,7068,7069,7070]
    hcushionsandcurtainsproducts=["hHandwoven Cushions","hRed Cushion Set (5)","hBlue Cushion Set(4)","hSheer Curtains Set","hBlue Gradient Curtains","hGreen Cushion Set (5)","hThrow & Cushion Set","hPatterned Cushion Set(5)","hGrey Curtain","hVelvet White Curtains"]
    hcushionsandcurtainsprices=[2715,1099,3990,899,1299,1999,3699,1999,999,1090]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    hcushionsandcurtainsbg=PhotoImage(file=f"images\\hcushionsandcurtains.png")
    background = canvas.create_image(500.0, 300.0,image=hcushionsandcurtainsbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(hcushionsandcurtainscodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(hcushionsandcurtainscodes[i],hcushionsandcurtainsproducts[i],hcushionsandcurtainsprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(hcushionsandcurtainscodes[i],string))
        
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = hnlcategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

############################################LUXE SECTION################################################
def luxecategoryscreen():
    global switchbtn, luxescreen,wclothesbtn,waccbtn,mclothesbtn,maccbtn,wbackbtn,switchbtn,background
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    luxescreen=PhotoImage(file=f"images\\luxescreen.png")
    background = canvas.create_image(500.0, 300.0,image=luxescreen)

    wclothesbtn = PhotoImage(file = f"images\\wclothesbtn.png")
    wclothes = Button(image = wclothesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[lwclothes(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wclothes.place(x = 39, y = 420,width =215,height = 147)

    waccbtn = PhotoImage(file = f"images\\waccbtn.png")
    wacc = Button(image = waccbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[lwaccessories(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wacc.place(x = 256, y = 420,width = 215,height = 147)

    mclothesbtn = PhotoImage(file = f"images\\mclothesbtn.png")
    mclothes = Button(image = mclothesbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[lmclothes(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    mclothes.place(x = 529, y = 420,width = 215,height = 147)

    maccbtn = PhotoImage(file = f"images\\maccbtn.png")
    macc= Button(image = maccbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[lmaccessories(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    macc.place(x =746, y = 420,width = 215,height = 147)

    wbackbtn = PhotoImage(file = f"images\\wbackbtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = lambda:[searchscreen(),change_image(0,"stop")],relief = "flat",cursor="hand2")
    wback.place(x =17, y = 26,width = 54,height = 62)


    banner1 = ImageTk.PhotoImage(Image.open("images\\luxescreenbanner1.png"))
    banner2 = ImageTk.PhotoImage(Image.open("images\\luxescreenbanner2.png"))
    banner3 = ImageTk.PhotoImage(Image.open("images\\luxescreenbanner3.png"))


    l=Label()
    l.place(x=20,y=103,height=227,width=960)
    banners=[banner1,banner2,banner3]
    def change_image(nextindex,value):
        global change
        if value=="continue":
            l.configure(image=banners[nextindex])
            change=window.after(2000, lambda: change_image((nextindex+1) % len(banners),"continue"))
        else:
            window.after_cancel(change)
        
    change_image(0,"continue")

def lwclothes():
    global lwclothesbg,cartbtn,wbackbtn,mcartbtn
    lwclothescodes=[8001,8002,8003,8004,8005,8006,8007,8008,8009,8010]
    lwclothesproducts=["lFloral Print Skater Dress","lWool Wrap Coat","lEllaine Dress","lCopper Dress","lBelong Womens Top","lJonas Luxury Dress","lFifth Ave Feathers Dress","lSea Breeze Shirt","lA.L.C. Alexis Dress","lHandkerchief Dress "]
    lwclothesprices=[24500,30099,14800,15299,7799,10999,27699,6999,64238,7750]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    lwclothesbg=PhotoImage(file=f"images\\lwclothes.png")
    background = canvas.create_image(500.0, 300.0,image=lwclothesbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(lwclothescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(lwclothescodes[i],lwclothesproducts[i],lwclothesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(lwclothescodes[i],string))

        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = luxecategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def lwaccessories():
    global lwaccessoriesbg,cartbtn,wbackbtn,mcartbtn
    lwaccessoriescodes=[8011,8012,8013,8014,8015,8016,8017,8018,8019,8020]
    lwaccessoriesproducts=["lVanilla Jet Set Pouch","lCream Casual Belt","lFossil Ceramic Watch","lVersace, V-Motif Series","lReversible Leather Belt","lFrench Crossbody Bag","lMK Shoulder Bag","lMK Jodie","lCarlie Rose Gold","lGancini Leather Belt"]
    lwaccessoriesprices=[13500,8099,16990,91099,14799,27299,52000,12999,26538,35000]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    lwaccessoriesbg=PhotoImage(file=f"images\\lwaccessories.png")
    background = canvas.create_image(500.0, 300.0,image=lwaccessoriesbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(lwaccessoriescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(lwaccessoriescodes[i],lwaccessoriesproducts[i],lwaccessoriesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(lwaccessoriescodes[i],string))
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = luxecategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def lmclothes():
    global lmclothesbg,cartbtn,wbackbtn,mcartbtn
    lmclothescodes=[8021,8022,8023,8024,8025,8026,8027,8028,8029,8030]
    lmclothesproducts=["lBlue Slimfit Shirt","lLO-FI Regular Fit","lMid-Wash Denim Shirt","lSpotter Slim Fit Shirt","lFloral Bowling Shirt","lHotaka Slim Fit Jacket","lClifton Trucker Jacket","lBlack Shirt","lDunes Oversized Hoodie","lTropical Print Shirt"]
    lmclothesprices=[8054,6099,22990,12299,32799,16999,18699,10800,18938,9690]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    lmclothesbg=PhotoImage(file=f"images\\lmclothes.png")
    background = canvas.create_image(500.0, 300.0,image=lmclothesbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(lmclothescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(lmclothescodes[i],lmclothesproducts[i],lmclothesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(lmclothescodes[i],string)) 
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = luxecategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)

def lmaccessories():
    global lmaccessoriesbg,cartbtn,wbackbtn,mcartbtn
    lmaccessoriescodes=[8031,8032,8033,8034,8035,8036,8037,8038,8039,8040]
    lmaccessoriesproducts=["lReversible Gancini Belt","lRectangular Buckle Belt","lBrown Leather Watch","lChronograph Watch","lAutomatic Watch","lLeather Belt","lLeather Bi-Fold Wallet","lMK Bi-Fold Wallet","lBonnet Leather Wallet","lTriangular Belt"]
    lmaccessoriesprices=[32750,17099,11990,13499,16799,12999,19699,13999,22000,45000]
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#ffffff")
    lmaccessoriesbg=PhotoImage(file=f"images\\lmaccessories.png")
    background = canvas.create_image(500.0, 300.0,image=lmaccessoriesbg)
    cartbtn=PhotoImage(file=f"images\\scartbtn.png")

    def addtocart(i):
        global cart
        mycursor.execute("SELECT * FROM customercart where PCODE={} AND CUSTMAIL='{}'".format(lmaccessoriescodes[i],string))
        prods=mycursor.fetchall()
        if len(prods)==0:
            mycursor.execute("INSERT INTO customercart VALUES({},'{}',NULL,1,{},'{}')".format(lmaccessoriescodes[i],lmaccessoriesproducts[i],lmaccessoriesprices[i],string))
        else:
            mycursor.execute("UPDATE customercart set QUANTITY=QUANTITY+1 where PCODE={} AND CUSTMAIL='{}'".format(lmaccessoriescodes[i],string))
        try:
            cart.destroy()
        except Exception:
            pass
        cart = Tk()
        cart.title('Confirm')
        cart.geometry("250x100")
        cart.resizable(False, False)
        e=Label(cart,text='Add product to cart?',anchor='w',fg="black")
        e.place(x=78,y=23)
        yes = Button(cart,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.commit(),cart.destroy()],cursor="hand2")
        yes.place(x = 50, y = 56,width = 55,height =21)
        no = Button(cart,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:[mydb.rollback(),cart.destroy()],cursor="hand2")
        no.place(x = 144, y = 56,width = 55,height =21)
        
    wd1 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(0), relief = "flat",cursor="hand2")
    wd1.place(x = 144, y = 266,width =71,height = 16)

    wd2 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(1), relief = "flat",cursor="hand2")
    wd2.place(x = 325, y = 265,width =71,height = 16)

    wd3 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(2), relief = "flat",cursor="hand2")
    wd3.place(x = 502, y = 266,width =71,height = 16)

    wd4 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(3), relief = "flat",cursor="hand2")
    wd4.place(x = 679, y = 266,width =71,height = 16)

    wd5 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(4), relief = "flat",cursor="hand2")
    wd5.place(x = 857, y = 265,width =71,height = 16)

    wd6 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(5), relief = "flat",cursor="hand2")
    wd6.place(x = 144, y = 556,width =71,height = 16)

    wd7 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(6), relief = "flat",cursor="hand2")
    wd7.place(x = 325, y = 556,width =71,height = 16)

    wd8 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(7), relief = "flat",cursor="hand2")
    wd8.place(x = 502, y = 556,width =71,height = 16)

    wd9 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(8), relief = "flat",cursor="hand2")
    wd9.place(x = 679, y = 556,width =71,height = 16)

    wd10 = Button(image = cartbtn,borderwidth = 0,highlightthickness = 0,command = lambda:addtocart(9), relief = "flat",cursor="hand2")
    wd10.place(x = 857, y = 556,width =71,height = 16)
    
    wbackbtn = PhotoImage(file = f"images\\backwhitebtn.png")
    wback = Button(image =wbackbtn,borderwidth = 0,highlightthickness = 0,command = luxecategoryscreen,relief = "flat",cursor="hand2")
    wback.place(x =5, y = 5,width = 54,height = 62)





def profilescreen():
    global profilebg,psignoutbtn,pdeleteaccbtn,peditprofilebtn,pchangepwdbtn,pchangeaddressbtn,phomebtn
    clear_frame()
    closewindows()
    canvasdefinition()
    canvas.configure(bg="#d8dff9")
    profilebg=PhotoImage(file=f"images\\profilebg.png")
    background = canvas.create_image(500.0, 300.0,image=profilebg)

    mycursor.execute("select NAME,DOB,ADDRESS from customers where EMAILID='{}'".format(accmail))
    data=mycursor.fetchall()
    accname=data[0][0]
    accdob=data[0][1]
    accaddr=data[0][2]

    namelabel=Label(text=accname,anchor='w',bg="#F7F9FE",fg="black")
    namelabel.config(font=('Helvetica bold', 26))
    namelabel.place(x=202,y=80)

    maillabel=Label(text=accmail,anchor='w',bg="#F7F9FE",fg="black")
    maillabel.config(font=('Helvetica bold', 12))
    maillabel.place(x=202,y=125)

    doblabel=Label(text=accdob,anchor='w',bg="#F7F9FE",fg="black")
    doblabel.config(font=('Helvetica bold', 12))
    doblabel.place(x=202,y=150)

    addrlabel=Label(text=accaddr,anchor='w',bg="#F7F9FE",fg="black")
    addrlabel.config(font=('Helvetica bold', 12))
    addrlabel.place(x=202,y=175)


    pchangepwdbtn = PhotoImage(file = f"images\\pchangepwdbtn.png")
    pchangepwd = Button(image = pchangepwdbtn,borderwidth = 0,highlightthickness = 0,command = changepassword,relief = "flat",cursor="hand2")
    pchangepwd.place(x = 50, y = 250,width = 899,height = 37)

    pchangeaddressbtn = PhotoImage(file = f"images\\pchangeaddressbtn.png")
    pchangeaddress = Button(image = pchangeaddressbtn,borderwidth = 0,highlightthickness = 0,command = changeaddress,relief = "flat",cursor="hand2")
    pchangeaddress.place(x = 50, y = 300,width = 899,height = 37)

    peditprofilebtn = PhotoImage(file = f"images\\peditprofilebtn.png")
    peditprofile = Button(image = peditprofilebtn,borderwidth = 0,highlightthickness = 0,command = editprofile,relief = "flat",cursor="hand2")
    peditprofile.place(x = 50, y = 350,width = 899,height = 37)

    psignoutbtn = PhotoImage(file = f"images\\psignoutbtn.png")
    psignout = Button(image = psignoutbtn,borderwidth = 0,highlightthickness = 0,command = signoutconfirm,relief = "flat",cursor="hand2")
    psignout.place(x = 50, y = 400,width = 899,height = 37)

    pdeleteaccbtn = PhotoImage(file = f"images\\pdeleteacc.png")
    pdeleteacc = Button(image = pdeleteaccbtn,borderwidth = 0,highlightthickness = 0,command = deleteaccconfirm,relief = "flat",cursor="hand2")
    pdeleteacc.place(x = 50, y = 450,width = 899,height = 37)

    phomebtn = PhotoImage(file = f"images\\phomebtn.png")
    phome = Button(image = phomebtn,borderwidth = 0,highlightthickness = 0,command = homepage,relief = "flat",cursor="hand2")
    phome.place(x = 764, y = 95,width = 178,height = 88)

def editprofile():
    global editprofilescreenimg,backbtn,updateprofilebtn,oldemailid
    clear_frame()
    closewindows()
    canvasdefinition()
    editprofilescreenimg = PhotoImage(file = f"images\\editprofilescreen.png")
    background = canvas.create_image(494.0, 300.0,image=editprofilescreenimg)
    mycursor.execute("SELECT NAME,DOB,GENDER,EMAILID from customers where emailid='{}'".format(string))
    oldprofile=mycursor.fetchall()
    
    oldname=oldprofile[0][0]
    olddob=str(oldprofile[0][1])
    dobnumbers=olddob.split("-")
    g=oldprofile[0][2]
    if g=="F":
        oldgender="Female"
    elif g=="M":
        oldgender="Male"
    else:
        oldgender="Rather Not Disclose"
    oldemailid=oldprofile[0][3]
    editprofilenameentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    editprofilenameentry.place(x = 445, y = 204,width = 372,height = 38)
    editprofilenameentry.insert(0, oldname)
    cal=DateEntry(selectmode='day',year=int(dobnumbers[0]),month= int(dobnumbers[1]),day=int(dobnumbers[2]))
    cal.place(
        x = 445, y = 315,
        width = 372,
        height = 38)
    def my_upd(*args): # triggered when value of string variable changes
        d=cal.get_date()
        return d.strftime("%Y-%m-%d")
    def shortform(choice):
        choice=clicked.get()
        if choice=="Female":
            g="F"
        elif choice=="Male":
            g="M"
        else:
            g="N"
        return g
    options=["Female", "Male","Rather Not Disclose"]
    clicked=StringVar()
    clicked.set(oldgender)
    drop= OptionMenu(canvas,clicked,*options,command=shortform)
    drop.configure(anchor='w')
    drop.place(x=445,y=259,width = 372,height = 38)
    drop.config(bg="WHITE", fg="BLACK")
    drop["menu"].config(bg="white")
    editprofilemailentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    editprofilemailentry.place(x = 445, y = 369,width = 372,height = 38)
    editprofilemailentry.insert(0, oldemailid)
    updateprofilebtn= PhotoImage(file = f"images\\updateprofilebtn.png")
    updateprofile = Button(image = updateprofilebtn,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command =lambda:editprofileprocess(editprofilenameentry.get().upper(),my_upd(),shortform(""),editprofilemailentry.get().upper()),
                    relief = "flat",cursor="hand2")
    updateprofile.place(x = 355, y = 471,width = 289,height = 59)
    backbtn= PhotoImage(file = f"images\\pbackbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command = profilescreen,relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 58,height = 66)

def editprofileprocess(name,dob,gender,mail):
    global string,accmail
    mycursor.execute("Select emailid from customers")
    emails=mycursor.fetchall()
    specialchar=["\"","[","!","#","$","%","^","&","*","(",")","<",">","?","/","|","}","{","~",":","]"]
    EMAIL=True
    for i in specialchar:
        if i in mail:
            EMAIL=False
    NAME=True
    for i in specialchar:
        if i in name:
            NAME=False
    B=False
    for i in emails:
        if i[0]==mail:
            if i[0]!=oldemailid:
                B=True
    if name=="" or dob=="" or gender=="" or mail=="":
        errorscreens("Fill all fields.")
    elif "@" not in mail or "." not in mail or EMAIL==False:
        errorscreens("Enter valid Email ID.")
    elif NAME==False or "@" in name or "." in name:
        errorscreens("Enter valid name")
    elif B==True:
        errorscreens("Email already registered")
    
    else:
        mycursor.execute("UPDATE customers set name='{}',dob='{}',gender='{}',emailid='{}' where emailid='{}'".format(name.upper(),dob,gender,mail.upper(),string))
        mycursor.execute("UPDATE customercart set custmail='{}' where custmail='{}'".format(mail.upper(),string))
        mycursor.execute("UPDATE customerorders set custmail='{}' where custmail='{}'".format(mail.upper(),string))
        mydb.commit()
        string=mail
        accmail=mail
        profilescreen()

def changeaddress():
    global changeaddressscreenimg,backbtn,updateaddressbtn
    clear_frame()
    closewindows()
    canvasdefinition()
    changeaddressscreenimg = PhotoImage(file = f"images\\changeaddressscreen.png")
    background = canvas.create_image(494.0, 300.0,image=changeaddressscreenimg)
    changeaddressentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    changeaddressentry.place(x = 217, y = 319,width = 568,height = 38) 
    updateaddressbtn= PhotoImage(file = f"images\\updateaddressbtn.png")
    updateaddress = Button(image = updateaddressbtn,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command =lambda:changeaddressprocess(changeaddressentry.get().upper()),
                    relief = "flat",cursor="hand2")
    updateaddress.place(x = 355, y = 471,width = 289,height = 59)
    backbtn= PhotoImage(file = f"images\\pbackbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command = profilescreen,relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 58,height = 66)

def changeaddressprocess(address):
    global string,changeaddress
    if address=="":
        errorscreens("Please enter the address.")
    else:
        mycursor.execute("UPDATE customers set address='{}' where emailid='{}'".format(address.upper(),string))
        mydb.commit()
        profilescreen()
        try:
            changeaddress.destroy()
        except Exception:
            pass
        changeaddress = Tk()
        changeaddress.title('Woohoo!')
        changeaddress.geometry("250x100")
        changeaddress.resizable(False, False)
        e=Label(changeaddress,text='Your address has been changed.',anchor='w',fg="black")
        e.place(x=44,y=23)
        oplaced = Button(changeaddress,text="OKAY THANKS!",borderwidth = 2,highlightthickness = 0,command = lambda:changeaddress.destroy(),cursor="hand2")
        oplaced.place(x = 75, y = 56,width = 100,height =21)

def changepassword():
    global changepasswordscreenimg,backbtn,updatepasswordbtn,hidepwbtn1,showpwbtn1,hidepwbtn2,showpwbtn2,hidepwbtn3,showpwbtn3
    clear_frame()
    closewindows()
    canvasdefinition()
    changepasswordscreenimg = PhotoImage(file = f"images\\changepasswordscreen.png")
    background = canvas.create_image(500.0, 300.0,image=changepasswordscreenimg)
    currentpasswordentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    currentpasswordentry['show']="●"
    currentpasswordentry.place(x = 499, y = 228,width = 293,height = 38) 
    currentpasswordentry.bind('<Control-x>', lambda e: 'break') #disable cut
    currentpasswordentry.bind('<Control-c>', lambda e: 'break') #disable copy
    currentpasswordentry.bind('<Control-v>', lambda e: 'break') #disable paste
    currentpasswordentry.bind('<Button-3>', lambda e: 'break')  #disable right-click
    def showpassword1():
        global hidepwbtn1,hidepw1 
        currentpasswordentry['show']=""
        showpw1.place_forget()
        hidepwbtn1= PhotoImage(file = f"images\\hidepwsmall1.png")
        hidepw1= Button(image = hidepwbtn1,borderwidth=0,highlightthickness = 0,command = hidepassword1,relief = "flat",cursor="hand2")
        hidepw1.place(x = 763, y = 237,width = 18,height = 18)
    def hidepassword1():
        currentpasswordentry['show']="●"
        hidepw1.place_forget()
        showpw1.place(x = 763, y = 237,width = 18,height = 18)
    #button to show password
    showpwbtn1= PhotoImage(file = f"images\\showpwsmall1.png")
    showpw1 = Button(image = showpwbtn1,borderwidth=0,highlightthickness = 0,command = showpassword1,relief = "flat",cursor="hand2")
    showpw1.place(x = 763, y = 237,width = 18,height = 18)

    #PASSWORD FIELD 2
    changepasswordentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    changepasswordentry.place(x = 499, y = 281,width = 293,height = 38)
    changepasswordentry['show']="●"

    changepasswordentry.bind('<Control-x>', lambda e: 'break') #disable cut
    changepasswordentry.bind('<Control-c>', lambda e: 'break') #disable copy
    changepasswordentry.bind('<Control-v>', lambda e: 'break') #disable paste
    changepasswordentry.bind('<Button-3>', lambda e: 'break')  #disable right-click
    def showpassword2():
        global hidepwbtn2
        global hidepw2
        changepasswordentry['show']=""
        showpw2.place_forget()
        hidepwbtn2= PhotoImage(file = f"images\\hidepwsmall.png")
        hidepw2= Button(image = hidepwbtn2,borderwidth=0,highlightthickness = 0,command = hidepassword2,relief = "flat",cursor="hand2")
        hidepw2.place(x = 763, y = 290,width = 18,height = 18)

    def hidepassword2():
        changepasswordentry['show']="●"
        hidepw2.place_forget()
        showpw2.place(x = 763, y = 290,width = 18,height = 18)

    #button to show password
    showpwbtn2= PhotoImage(file = f"images\\showpwsmall.png")
    showpw2 = Button(window,image = showpwbtn2,borderwidth=0,highlightthickness = 0,
                     command = showpassword2,
                     relief = "flat",cursor="hand2")
    showpw2.place(x = 763, y = 290,width = 18,height = 18)
    confirmchangepasswordentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    confirmchangepasswordentry.place(x = 499, y = 334,width = 293,height = 38)
    confirmchangepasswordentry['show']="●"

    confirmchangepasswordentry.bind('<Control-x>', lambda e: 'break') #disable cut
    confirmchangepasswordentry.bind('<Control-c>', lambda e: 'break') #disable copy
    confirmchangepasswordentry.bind('<Control-v>', lambda e: 'break') #disable paste
    confirmchangepasswordentry.bind('<Button-3>', lambda e: 'break')  #disable right-click
    def showpassword3():
        global hidepwbtn3
        global hidepw3
        confirmchangepasswordentry['show']=""
        showpw3.place_forget()
        hidepwbtn3= PhotoImage(file = f"images\\hidepwsmall.png")
        hidepw3= Button(image = hidepwbtn3,borderwidth=0,highlightthickness = 0,command = hidepassword3,relief = "flat",cursor="hand2")
        hidepw3.place(x = 763, y = 343,width = 18,height = 18)

    def hidepassword3():
        confirmchangepasswordentry['show']="●"
        hidepw3.place_forget()
        showpw3.place(x = 763, y = 343,width = 18,height = 18)

    #button to show password
    showpwbtn3= PhotoImage(file = f"images\\showpwsmall.png")
    showpw3 = Button(window,image = showpwbtn3,borderwidth=0,highlightthickness = 0,
                     command = showpassword3,
                     relief = "flat",cursor="hand2")
    showpw3.place(x = 763, y = 343,width = 18,height = 18)
    updatepasswordbtn= PhotoImage(file = f"images\\updatepasswordbtn.png")
    updatepassword = Button(image = updatepasswordbtn,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command =lambda:changepasswordprocess(currentpasswordentry.get(),changepasswordentry.get(),confirmchangepasswordentry.get()),
                    relief = "flat",cursor="hand2")
    updatepassword.place(x = 355, y = 471,width = 289,height = 59)
    backbtn= PhotoImage(file = f"images\\pbackbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command = profilescreen,relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 58,height = 66)

def changepasswordprocess(currentpw,pw,confirmpw):
    global string,pwchanged
    mycursor.execute("SELECT PASSWORD FROM CUSTOMERS WHERE EMAILID='{}'".format(string))
    x=mycursor.fetchall()
    if currentpw=="" or pw=="" or confirmpw=="":
        errorscreens("Fill all fields")
    elif bcrypt.checkpw(currentpw.encode('utf-8'),x[0][0].encode('utf-8'))==False:
        errorscreens("Current password incorrect.")
    elif pw!=confirmpw:
        errorscreens("Passwords do not match.")
    elif bcrypt.checkpw(currentpw.encode('utf-8'),x[0][0].encode('utf-8')) and pw==confirmpw:
        bytePwd=pw.encode('utf-8')
        hashed = bcrypt.hashpw(bytePwd, mySalt)
        mycursor.execute("UPDATE customers set password='{}' where emailid='{}'".format(hashed.decode(),string))
        mydb.commit()
        profilescreen()
        try:
            pwchanged.destroy()
        except Exception:
            pass
        pwchanged = Tk()
        pwchanged.title('Success!')
        pwchanged.geometry("250x100")
        pwchanged.resizable(False, False)
        e=Label(pwchanged,text='Your password has been changed.',anchor='w',fg="black")
        e.place(x=42,y=23)
        oplaced = Button(pwchanged,text="OKAY THANKS!",borderwidth = 2,highlightthickness = 0,command = lambda:pwchanged.destroy(),cursor="hand2")
        oplaced.place(x = 75, y = 56,width = 100,height =21)

def deleteaccconfirm():
    global delacc
    try:
        delacc.destroy()
    except Exception:
        pass
    delacc = Tk()
    delacc.title('Confirm')
    delacc.geometry("250x100")
    delacc.resizable(False, False)
    e=Label(delacc,text='Delete Account?',anchor='w',fg="black")
    e.place(x=77,y=23)
    yes = Button(delacc,text="YES",borderwidth = 2,highlightthickness = 0,command = lambda:[delacc.destroy(),deleteacc()],cursor="hand2")
    yes.place(x = 50, y = 56,width = 55,height =21)
    no = Button(delacc,text="NO",borderwidth = 2,highlightthickness = 0,command = lambda:delacc.destroy(),cursor="hand2")
    no.place(x = 144, y = 56,width = 55,height =21)

def deleteacc():
    mycursor.execute("delete from customers where EMAILID='{}'".format(accmail))
    mycursor.execute("delete from customercart where custmail='{}'".format(string))
    mycursor.execute("delete from customerorders where custmail='{}'".format(string))
    mydb.commit()
    welcomescreen()
    
###########################CREATING ADMIN PART OF THE APP#######################################
def adminloginscreen(B):
    global loginscreenimg,loginbtn,backbtn,showpwbtn
    
    clear_frame()
    closewindows()
    canvasdefinition()
    if B==0:
        loginscreenimg = PhotoImage(file = f"images\\adminloginscreenerror.png")
    else:
        loginscreenimg = PhotoImage(file = f"images\\adminloginscreen.png")
    background = canvas.create_image(494.0, 300.0,image=loginscreenimg)
    
    loginmailentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    loginmailentry.place(x = 668, y = 227,width = 247,height = 44)
    
    loginpwentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    loginpwentry.default_show_val=loginpwentry['show']
    loginpwentry['show']="●"
    loginpwentry.place(x = 668, y = 300,width = 247,height = 44)

    loginbtn = PhotoImage(file = f"images\\loginbtn.png")
    login = Button(image = loginbtn,borderwidth = 0,highlightthickness = 0,command = lambda:adminloginprocess(loginmailentry.get(),loginpwentry.get()),relief = "flat",cursor="hand2")
    login.place(x = 678, y = 367,width = 88,height = 39)

    backbtn= PhotoImage(file = f"images\\backbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command = welcomescreen,relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 54,height = 62)

    def showpassword():
        global hidepwbtn,hidepw
        loginpwentry['show']=""
        showpw.place_forget()
        hidepwbtn= PhotoImage(file = f"images\\hidepwbtn.png")
        hidepw = Button(image = hidepwbtn,borderwidth=0,highlightthickness = 0,command = hidepassword,relief = "flat",cursor="hand2")
        hidepw.place(x = 872, y = 305,width = 33,height = 33)

    def hidepassword():
        loginpwentry['show']="●"
        hidepw.place_forget()
        showpw.place(x = 872, y = 305,width = 33,height = 33)
        
    showpwbtn= PhotoImage(file = f"images\\showpwbtn.png")
    showpw = Button(image = showpwbtn,borderwidth=0,highlightthickness = 0,command = showpassword,relief = "flat",cursor="hand2")
    showpw.place(x = 872, y = 305,width = 33,height = 33)

def adminoptionsscreen():
    global options,seecustbtn,searchcustbtn,seeprodbtn,searchprodbtn,addprodbtn,editprodbtn,delprodbtn,backbtn
    clear_frame()
    closewindows()
    canvasdefinition()
    options = PhotoImage(file = f"images\\optionsscreen.png")
    background = canvas.create_image(494.0, 300.0,image=options)

    backbtn= PhotoImage(file = f"images\\backbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command = lambda:adminloginscreen(20),relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 54,height = 62)

    seecustbtn = PhotoImage(file = f"images\\seecustbtn.png")
    seecust = Button(image = seecustbtn,borderwidth = 0,highlightthickness = 0,command = customerrecordsdisplay,relief = "flat",cursor="hand2")
    seecust.place(x = 579, y = 195,width = 298,height = 33)

    searchcustbtn = PhotoImage(file = f"images\\searchcustbtn.png")
    searchcust = Button(image = searchcustbtn,borderwidth = 0,highlightthickness = 0,command = searchcustomerrecordsscreen,relief = "flat",cursor="hand2")
    searchcust.place(x = 579, y = 258,width = 298,height = 33)

    seeprodbtn = PhotoImage(file = f"images\\seeprodbtn.png")
    seeprod = Button(image = seeprodbtn,borderwidth = 0,highlightthickness = 0,command = productrecordsdisplay,relief = "flat",cursor="hand2")
    seeprod.place(x = 579, y = 320,width = 298,height = 33)

    searchprodbtn = PhotoImage(file = f"images\\searchprodbtn.png")
    searchprod = Button(image = searchprodbtn,borderwidth = 0,highlightthickness = 0,command = searchproductrecordsscreen,relief = "flat",cursor="hand2")
    searchprod.place(x = 579, y = 383,width = 298,height = 33)

def customerrecordsdisplay():
    global customerrecords,backbtn
    try:
        customerrecords.destroy()
    except Exception:
        pass
    customerrecords = Tk()
    customerrecords.title('Customer Records')
    customerrecords.geometry("1000x600")
    customerrecords.configure(bg = "#c0cafb")
    canvas = Canvas(customerrecords,bg = "#c0cafb",bd = 0,highlightthickness = 0,relief = "ridge")
    frame = Frame(canvas)
    mycursor.execute("SELECT NAME, DOB, GENDER, EMAILID,ADDRESS FROM customers")
    rec=mycursor.fetchall()
    if len(rec)==0:
        errorscreens("No registered customer.")
    else:
        e=Label(frame,height=3,width=26,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=0)
        e=Label(frame,height=3,width=26,text='Date of Birth',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=1)
        e=Label(frame,height=3,width=26,text='Gender',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=2)
        e=Label(frame,height=3,width=26,text='E-mail ID',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=3)
        e=Label(frame,height=3,width=26,text='Address',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
        e.grid(row=1,column=4)
        i=2
        for record in rec: 
            for j in range(len(record)):
                e = Label(frame,height=2,width=26, text=record[j],
            borderwidth=2,relief='ridge', anchor="w",bg='#ffffff') 
                e.grid(row=i, column=j) 
            i=i+1
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        scrollbar = Scrollbar(customerrecords, orient='vertical', command=canvas.yview)
        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
        canvas.pack(fill='both', expand=True, side='left')
        scrollbar.pack(fill='y', side='right')
        customerrecords.resizable(False,False)
        customerrecords.mainloop()

def searchcustomerrecordsscreen():
    global searchcustrecbg,searchcustrecbtn,backbtn
    clear_frame()
    closewindows()
    canvasdefinition()
    searchcustrecbg = PhotoImage(file = f"images\\searchcustrecscreen.png")
    background = canvas.create_image(494.0, 300.0,image=searchcustrecbg)

    backbtn= PhotoImage(file = f"images\\backbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command =adminoptionsscreen,relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 54,height = 62)

    searchentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    searchentry.place(x =554, y = 367,width = 354,height = 45)

    searchcustrecbtn = PhotoImage(file = f"images\\searchcustrecbtn.png")
    searchcustrec = Button(image = searchcustrecbtn,borderwidth = 0,highlightthickness = 0,command = lambda:searchcustrecprocess(searchentry.get().upper()),relief = "flat",cursor="hand2")
    searchcustrec.place(x = 677, y = 435,width = 106,height = 31)
    
def searchcustrecprocess(text):
    global searchcustomer
    if text=="":
        errorscreens("Enter something to search.")
    else:
        closewindows()
        mycursor.execute("SELECT NAME, DOB, GENDER, EMAILID,ADDRESS FROM CUSTOMERS")
        x=mycursor.fetchall()
        records=[]
        for i in x:
            if text in i[0].upper() or text in i[3].upper():
                records.append(i)
                

        try:
            searchcustomer.destroy()
        except Exception:
            pass
        if len(records)==0:
            errorscreens("No such customer.")
        else:
            searchcustomer = Tk()
            searchcustomer.title('Search Results')
            searchcustomer.geometry("1000x600")
            searchcustomer.configure(bg = "#c0cafb")
            canvas = Canvas(searchcustomer,bg = "#c0cafb",bd = 0,highlightthickness = 0,relief = "ridge")
            frame = Frame(canvas)
            e=Label(frame,height=3,width=26,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
            e.grid(row=1,column=0)
            e=Label(frame,height=3,width=26,text='Date of Birth',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
            e.grid(row=1,column=1)
            e=Label(frame,height=3,width=26,text='Gender',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
            e.grid(row=1,column=2)
            e=Label(frame,height=3,width=26,text='E-mail ID',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
            e.grid(row=1,column=3)
            e=Label(frame,height=3,width=26,text='Address',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
            e.grid(row=1,column=4)

            buttonlist=[]
            rowno=2
            for u in range(len(records)):
                    b = Button(frame,height=2,width=26, text=records[u][0],borderwidth=2, anchor="w",bg='#ffffff',command=partial(seeorders,records[u][3]),relief='ridge',cursor="hand2")
                    buttonlist.append(b)
                    b.grid(row=rowno, column=0)
                    rowno+=1
            i=2
            for r in records:
                for j in range(1,len(r)):
                    e = Label(frame,height=2,width=26, text=r[j],
                borderwidth=2,relief='ridge', anchor="w",bg='#ffffff') 
                    e.grid(row=i, column=j) 
                i=i+1
            canvas.create_window(0, 0, anchor='nw', window=frame)
            canvas.update_idletasks()
            scrollbar = Scrollbar(searchcustomer, orient='vertical', command=canvas.yview)
            canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
            canvas.pack(fill='both', expand=True, side='left')
            scrollbar.pack(fill='y', side='right')
            searchcustomer.resizable(False,False)
            searchcustomer.mainloop()

def productrecordsdisplay():
    global productrecords,backbtn
    try:
        productrecords.destroy()
    except Exception:
        pass
    productrecords = Tk()
    productrecords.title('Product Records')
    productrecords.geometry("1000x600")
    productrecords.configure(bg = "#c0cafb")
    canvas = Canvas(productrecords,bg = "#c0cafb",bd = 0,highlightthickness = 0,relief = "ridge")
    frame = Frame(canvas)
    mycursor.execute("SELECT PCODE,PNAME,PCOST FROM products")
    records=mycursor.fetchall()
    e=Label(frame,height=3,width=26,text='Product Code',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
    e.grid(row=1,column=0)
    e=Label(frame,height=3,width=26,text='Product Name',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
    e.grid(row=1,column=1)
    e=Label(frame,height=3,width=26,text='Product Cost',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
    e.grid(row=1,column=2)
    
    buttonlist=[]
    rowno=2
    for u in range(len(records)):
            b = Button(frame,height=2,width=26, text=records[u][0],borderwidth=2, anchor="w",bg='#ffffff',command=partial(prodinfo,records[u][0]),relief='ridge',cursor="hand2")
            buttonlist.append(b)
            b.grid(row=rowno, column=0)
            rowno+=1
    i=2
    for r in records:
        for j in range(1,len(r)):
            e = Label(frame,height=2,width=26, text=r[j],
	borderwidth=2,relief='ridge', anchor="w",bg='#ffffff') 
            e.grid(row=i, column=j) 
        i=i+1
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()
    scrollbar = Scrollbar(productrecords, orient='vertical', command=canvas.yview)
    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
    canvas.pack(fill='both', expand=True, side='left')
    scrollbar.pack(fill='y', side='right')
    productrecords.resizable(False,False)
    productrecords.mainloop()
def searchproductrecordsscreen():
    global searchprodrecbg,searchprodrecbtn,backbtn
    clear_frame()
    closewindows()
    canvasdefinition()
    searchprodrecbg = PhotoImage(file = f"images\\searchprodrecscreen.png")
    background = canvas.create_image(494.0, 300.0,image=searchprodrecbg)

    backbtn= PhotoImage(file = f"images\\backbtn.png")
    back = Button(image = backbtn,borderwidth=0,highlightthickness = 0,command =adminoptionsscreen,relief = "flat",cursor="hand2")
    back.place(x = 10, y = 10,width = 54,height = 62)

    searchentry = Entry(bd = 0,bg = "#ffffff",highlightthickness = 0)
    searchentry.place(x =554, y = 367,width = 354,height = 45)

    searchprodrecbtn = PhotoImage(file = f"images\\searchcustrecbtn.png")
    searchprodrec = Button(image = searchprodrecbtn,borderwidth = 0,highlightthickness = 0,command = lambda:searchprodrecprocess(searchentry.get().upper()),relief = "flat",cursor="hand2")
    searchprodrec.place(x = 677, y = 435,width = 106,height = 31)
    
def searchprodrecprocess(text):
    global searchproducts
    mycursor.execute("SELECT PCODE,PNAME,PCOST,PCATEGORY FROM PRODUCTS")
    x=mycursor.fetchall()
    if text=="":
        errorscreens("Enter something to search.")
    else:
        closewindows()
        records=[]
        for i in x:
            if text in str(i[0]) or text in i[1].upper() or text in i[3].upper():
                records.append(i)

        try:
            searchproducts.destroy()

        except Exception:
            pass
        if len(records)==0:
            errorscreens("No such product exists.")
        else:
            searchproducts = Tk()
            searchproducts.title('Search Results')
            searchproducts.geometry("1000x600")
            searchproducts.configure(bg = "#c0cafb")
            canvas = Canvas(searchproducts,bg = "#c0cafb",bd = 0,highlightthickness = 0,relief = "ridge")
            frame = Frame(canvas)
            e=Label(frame,height=3,width=26,text='Product Code',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
            e.grid(row=1,column=0)
            e=Label(frame,height=3,width=26,text='Product Name',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
            e.grid(row=1,column=1)
            e=Label(frame,height=3,width=26,text='Product Cost',borderwidth=2, relief='ridge',anchor='w',bg='#151435',fg="white")
            e.grid(row=1,column=2)
            
            buttonlist=[]
            rowno=2
            for u in range(len(records)):
                    b = Button(frame,height=2,width=26, text=records[u][0],borderwidth=2, anchor="w",bg='#ffffff',command=partial(prodinfo,records[u][0]),relief='ridge',cursor="hand2")
                    buttonlist.append(b)
                    b.grid(row=rowno, column=0)
                    rowno+=1
            i=2
            for r in records:
                for j in range(1,len(r)-1):
                    e = Label(frame,height=2,width=26, text=r[j],
                borderwidth=2,relief='ridge', anchor="w",bg='#ffffff') 
                    e.grid(row=i, column=j) 
                i=i+1
            canvas.create_window(0, 0, anchor='nw', window=frame)
            canvas.update_idletasks()
            scrollbar = Scrollbar(searchproducts, orient='vertical', command=canvas.yview)
            canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
            canvas.pack(fill='both', expand=True, side='left')
            scrollbar.pack(fill='y', side='right')
            searchproducts.resizable(False,False)
            searchproducts.mainloop()

def prodinfo(i):
    global productinfo,img
    try:
        productinfo.destroy()

    except Exception:
        pass
    productinfo = Toplevel()
    productinfo.geometry("174x270")
    productinfo.configure(bg = "#ffffff")
    productinfo.title("{}".format(i))
    img = ImageTk.PhotoImage(Image.open("images\\products\\{}".format(str(i)+".png")))
    prod = Label(productinfo, image = img)
    prod.pack(side = "bottom", fill = "both", expand = "yes")

def errorscreens(errorname):
    global error
    try:
        error.destroy()
    except Exception:
        pass

    error = Tk()
    error.title('Try again')
    error.geometry("250x100")
    error.resizable(False, False)
    e=Label(error,text=errorname,anchor='w',fg="black")
    e.pack(side = "top",expand="yes")
    okay = Button(error,text="Okay.",borderwidth = 2,highlightthickness = 0,command = lambda:error.destroy(),cursor="hand2")
    okay.pack(side = "bottom",expand="yes")
        
welcomescreen()
window.resizable(True, True)
window.mainloop()
