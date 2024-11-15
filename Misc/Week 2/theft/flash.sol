// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

interface FlashLoanReceiver {
    function execute() external payable;
}

contract Pool {
    mapping(address => uint256) private balances;
    uint public totalSupply;
    uint public maxloanamount = 100 ether;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
        totalSupply += msg.value;
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender];
        balances[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
        totalSupply -= amount;
    }

    function balanceOf(address user) external view returns (uint256) {
        return balances[user];
    }

    function flashLoan(uint256 amount) external {
        require(amount <= maxloanamount, "Amount too high");
        uint256 balanceBefore = address(this).balance;
        require(balanceBefore >= amount, "No enough balance here");

        FlashLoanReceiver(msg.sender).execute{value: amount}();

        require(address(this).balance >= balanceBefore, "no money back");
    }
}
