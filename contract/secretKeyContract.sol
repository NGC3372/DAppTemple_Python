// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.8.0;


contract secretKeyContract{
    address public deployer;
    address public caller;

    struct DHKey{
        string managerKey;
        mapping(address => string) userKey;
    }

    mapping(string => DHKey) private dataDHList;

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

    function createData_DHKey(string memory dataName ,string memory _manageKey) public onlyCaller{
        DHKey storage temp = dataDHList[dataName];
        temp.managerKey = _manageKey;
    }

    function addUser_DHKey(string  memory dataName,string memory _userKey) public {
        dataDHList[dataName].userKey[msg.sender] = _userKey;
    }

    function getUser_DHKey(address user , string memory dataName ) public view returns(string memory user_key){
        DHKey storage temp = dataDHList[dataName];
        user_key = temp.userKey[user];
    }

    function getManage_DHKey(string memory dataName)public view returns(string memory manage_key){
        DHKey storage temp = dataDHList[dataName];
        manage_key = temp.managerKey;
    }

}
