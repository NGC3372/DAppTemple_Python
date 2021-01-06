// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.8.0;

contract dataStorageContract{
    address public deployer;
    address public caller;

    mapping(string => string) private publicData;

    mapping(address => mapping(string => string)) private userData;

    modifier onlyDeployer() {
        require(msg.sender == deployer, "Caller is not deployer");
        _;
    }

    modifier onlyCaller() {
        require(msg.sender == caller, "Caller is not right");
        _;
    }

    constructor(){
        deployer = msg.sender;
    }

    function setCaller(address _caller) public onlyDeployer{
        caller = _caller;
    }

    function setPublicData(string  memory dataName , string memory content ) public onlyCaller{
        publicData[dataName] = content;
    }

    function setUserData(address addrUser , string memory dataName , string memory content) public onlyCaller{
        userData[addrUser][dataName] = content;
    }

    function getPublicData(string memory dataName )public view returns(string memory CONTENT){
        CONTENT = publicData[dataName];
    }

    function getUserData(address addr , string memory dataName)public view returns(string memory CONTENT){
        CONTENT = userData[addr][dataName];
    }

}
