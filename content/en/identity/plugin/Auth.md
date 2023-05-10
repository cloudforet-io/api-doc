---
title: "Auth"
linkTitle: "Auth"
weight: 3
bookFlatSection: true
---
# [Auth](#Auth)



>  **Package : spaceone.api.identity.plugin**

<br>
<br>

## Auth





**Auth Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./Auth#init) | [InitRequest](Auth#initrequest) | [PluginInfo](./Auth#plugininfo) |
| [**verify**](./Auth#verify) | [VerifyRequest](Auth#verifyrequest) | [Empty](./Auth#empty) |
| [**find**](./Auth#find) | [FindRequest](Auth#findrequest) | [UsersInfo](./Auth#usersinfo) |
| [**login**](./Auth#login) | [LoginRequest](Auth#loginrequest) | [UserInfo](./Auth#userinfo) |



    
<br>

### init










    
<br>

### verify










    
<br>

### find










    
<br>

### login










    


<br>
<br>

## Message



### AuthVerifyInfo
* **options** (Struct)  `Required` 

    <br>

### FindRequest
* **options** (Struct)  `Required` 

    
* **secret_data** (Struct)  `Required` 

    
* **user_id** (string) 

    
* **keyword** (string) 

    
* **schema** (string) 

    <br>

### InitRequest
* **options** (Struct)  `Required` 

    <br>

### LoginRequest
* **options** (Struct)  `Required` 

    
* **secret_data** (Struct)  `Required` 

    
* **user_credentials** (Struct)  `Required` 

    
* **schema** (string) 

    <br>

### PluginInfo
* **metadata** (Struct)  `Required` 

    <br>

### UserInfo
* **user_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **email** (string)  `Required` 

    
* **mobile** (string)  `Required` 

    
* **group** (string)  `Required` 

    
* **state** (State)  `Required` 

    <br>

### UsersInfo
* **results** (UserInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

  *will be depricated*

    
* **more** (bool)  `Required` 

    <br>

### VerifyRequest
* **options** (Struct)  `Required` 

    
* **secret_data** (Struct)  `Required` 

    
* **schema** (string) 

    <br>
