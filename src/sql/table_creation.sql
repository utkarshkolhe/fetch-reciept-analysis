CREATE TABLE UserRoles(
    _id INT PRIMARY KEY,
    role VARCHAR(100)
);

CREATE TABLE Users (
    _id VARCHAR(100) PRIMARY KEY,
    state VARCHAR(100),
    createdDate TIMESTAMP,
    lastLogin TIMESTAMP,
    roleid INT, --REFERENCES UserRoles(_id),
    active BOOLEAN,
    signUpSource VARCHAR(100)
);

CREATE TABLE BrandCategories(
    _id INT PRIMARY KEY,
    categoryCode VARCHAR(100),
    category VARCHAR(100)
);

CREATE TABLE Brands(
  _id VARCHAR(100) PRIMARY KEY,
  barcode VARCHAR(100),
  brandCode VARCHAR(100),
  catid INT,  --REFERENCES BrandCategories(_id),
  cpgid VARCHAR(100),
  cpgref VARCHAR(100),
  topBrand boolean,
  name VARCHAR(100)
);

CREATE TABLE Receipts(
  _id VARCHAR(100) PRIMARY KEY,
  bonusPointsEarned FLOAT,
  bonusPointsEarnedReason VARCHAR(100),
  createDate TIMESTAMP,
  dateScanned TIMESTAMP,
  finishedDate TIMESTAMP,
  modifyDate TIMESTAMP,
  pointsAwardedDate TIMESTAMP,
  pointsEarned FLOAT,
  purchaseDate TIMESTAMP,
  purchasedItemCount INT,
  rewardsReceiptStatus VARCHAR(100),
  totalSpent FLOAT,
  userId VARCHAR(100) --REFERENCES Users(_id)
);


CREATE TABLE ReceiptItems(
  _id VARCHAR(100) PRIMARY KEY,
  recieptID VARCHAR(100), --REFERENCES Receipts(_id),
  brandID VARCHAR(100), --REFERENCES Brands(_id),
  barcode VARCHAR(100),
  description TEXT,
  finalPrice FLOAT,
  itemPrice FLOAT,
  needsFetchReview BOOLEAN,
  partnerItemId VARCHAR(100),
  preventTargetGapPoints BOOLEAN,
  quantityPurchased INT,
  userFlaggedBarcode VARCHAR(100),
  userFlaggedNewItem BOOLEAN,
  userFlaggedPrice FLOAT,
  userFlaggedQuantity BOOLEAN,
  needsFetchReviewReason VARCHAR(100),
  pointsNotAwardedReason VARCHAR(100),
  pointsPayerId VARCHAR(100),
  rewardsGroup VARCHAR(100),
  rewardsProductPartnerId VARCHAR(100),
  userFlaggedDescription VARCHAR(100),
  originalMetaBriteBarcode VARCHAR(100),
  originalMetaBriteDescription VARCHAR(100),
  brandCode VARCHAR(100),
  competitorRewardsGroup VARCHAR(100),
  discountedItemPrice FLOAT,
  originalReceiptItemText TEXT,
  itemNumber VARCHAR(100),
  originalMetaBriteQuantityPurchased INT,
  pointsEarned FLOAT,
  targetPrice FLOAT,
  competitiveProduct VARCHAR(100),
  originalFinalPrice FLOAT,
  originalMetaBriteItemPrice FLOAT,
  deleted BOOLEAN,
  priceAfterCoupon FLOAT,
  metabriteCampaignId VARCHAR(100)
);
