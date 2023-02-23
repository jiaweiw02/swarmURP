var Auction = artifacts.require("./Auction.sol");

module.exports = function(deployer) {
    var beneficiary_address = "0x038dA5b422a6CCbfcEc60A6C2d1A782883F8354d";
    deployer.deploy(Auction, 300, beneficiary_address);
}