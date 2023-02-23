// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Auction {
    address payable public beneficiary;
    uint public auctionEndTime;
    bool ended;

    address public highestBidder;
    uint public highestBid;

    // track bidders who decide to withdraw their bids at a later point
    mapping (address => uint) pendingReturns;

    event highestBidIncreased(address bidder, uint amount);
    event auctionEnded(address winner, uint winnerBet);

    error auctionAlreadyEnded();
    error bidNotHigh(uint amount);
    error auctionNotEnded(uint timeRemaining);
    error auctionEndAlreadyCalled();

    constructor(uint auctionTime, address payable beneficiaryAdd){
        beneficiary = beneficiaryAdd;
        auctionEndTime = block.timestamp + auctionTime;
    }

    function bid() external payable {

        if (block.timestamp > auctionEndTime) {
            revert auctionAlreadyEnded();
        }

        if (msg.value <= highestBid) {
            revert bidNotHigh(highestBid);
        }

        if (highestBid != 0) {
            pendingReturns[highestBidder] += highestBid;
        }

        highestBidder = msg.sender;
        highestBid = msg.value;
        emit highestBidIncreased(highestBidder, highestBid);
    }

    function withdraw() external payable returns (bool) {
        uint bidAmount = pendingReturns[msg.sender];

        if (bidAmount > 0) {
            pendingReturns[msg.sender] = 0;

            if (!payable(msg.sender).send(bidAmount)) {
                pendingReturns[msg.sender] = bidAmount;
                return false;
            }
        }
        return true;
    }


    function end() external {
        if (block.timestamp < auctionEndTime) {
            revert auctionNotEnded(auctionEndTime - block.timestamp);
        }

        if (ended) {
            revert auctionEndAlreadyCalled();
        }

        ended = true;
        emit auctionEnded(highestBidder, highestBid);

        beneficiary.transfer(highestBid);
    }


    function hello() public pure returns (string memory) {
        return "Hello";
    }
}
