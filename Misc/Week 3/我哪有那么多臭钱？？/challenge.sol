// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

contract Challenge {
    mapping(address => uint256) public balance;
    bool public solve;
    constructor() {}

    function Get() public {
        balance[msg.sender] = 50;
    }

    function Transfer(address to, uint256 amount) public {
        require(amount > 0, "Man!");
        require(balance[msg.sender] > 0, "What can I say");
        require(balance[msg.sender] - amount > 0, "Mamba out!");
        require(uint160(msg.sender) % (16*16) == 239, "Sometimes I ask myself, who am i?");
        balance[msg.sender] -= amount;
        balance[to] += amount;
    }

    function check() public {
        require(balance[msg.sender] == 114514);
        solve=true;
    }

    function isSolved() public view returns (bool) {
        return solve;
    }
}
