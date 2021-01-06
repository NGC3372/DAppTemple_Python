// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.8.0;

contract tableContract{
    address public deployer;
    address public caller;

    address public dataStorageContractAddress;
    address public dataManageContractAddress;
    address public scecrtKeyContractAddress;

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

    function setCaller(address addr) public onlyDeployer{
        caller = addr;
    }

    function setDataStorageContractAddress(address addr) public onlyCaller{
        dataStorageContractAddress = addr;
    }

    function setDataManageContractAddress(address addr) public onlyCaller{
        dataManageContractAddress = addr;
    }

    function setScecrtKeyContractAddress(address addr) public onlyCaller{
        scecrtKeyContractAddress = addr;
    }

}
