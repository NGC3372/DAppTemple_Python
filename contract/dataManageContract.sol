// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.8.0;
import "./dataStorageContract.sol";
import "./tableContract.sol";

contract dataManageContract{
    address public deployer;
    address public caller;
    address public tableContractAddress;

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

    function setTableContractAddress(address _address) public onlyCaller{
        tableContractAddress = _address;
    }

    function setPublicData(string memory dataName, string memory content) public onlyCaller{
        address dataStorageContractAddress = tableContract(tableContractAddress).dataStorageContractAddress();
        //some conditions.....
        dataStorageContract(dataStorageContractAddress).setPublicData(dataName,content);
    }

    function setUserData(string memory dataName , string memory content) public {
        address dataStorageContractAddress = tableContract(tableContractAddress).dataStorageContractAddress();
        //some conditions.....
        address addrUser  = msg.sender;
        dataStorageContract(dataStorageContractAddress).setUserData(addrUser,dataName,content);
    }

}
