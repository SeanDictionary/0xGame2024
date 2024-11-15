// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "./flash.sol";

contract Setup {
    Pool public TARGET;
    constructor() payable {
        TARGET = new Pool();
        TARGET.deposit{value: msg.value}();
    }

    function isSolved() external view returns (bool) {
        return (TARGET.totalSupply() == 1000 ether &&
            address(TARGET).balance < 10 ether);
    }
}
