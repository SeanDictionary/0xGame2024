// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Signin {
    bytes32 signin;

    constructor () {}

    function sign(bytes32 _signin) public {
        signin = _signin;
    }

    function isSolved() public view returns (bool) {
        string memory expected = "Hello0xBlockchain";
        return keccak256(abi.encodePacked(expected)) == signin;
    }
}