var Auction = artifacts.require("./Auction.sol");

module.exports = function(deployer) {
    var beneficiary_address = "0xfc4582133129374C4345fDD046C13143FB7480B7";
    deployer.deploy(Auction, 300, beneficiary_address);

    
}