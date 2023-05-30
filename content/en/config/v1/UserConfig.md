---
title: "UserConfig"
linkTitle: "UserConfig"
weight: 3
bookFlatSection: true
---
# [UserConfig](#UserConfig)
UserConfig API which configure environments for user


>  **Package : spaceone.api.config.v1**

<br>
<br>

## UserConfig





**UserConfig Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./UserConfig#create) | [SetUserConfigRequest](UserConfig#setuserconfigrequest) | [UserConfigInfo](UserConfig#userconfiginfo) |
| [**update**](./UserConfig#update) | [SetUserConfigRequest](UserConfig#setuserconfigrequest) | [UserConfigInfo](UserConfig#userconfiginfo) |
| [**set**](./UserConfig#set) | [SetUserConfigRequest](UserConfig#setuserconfigrequest) | [UserConfigInfo](UserConfig#userconfiginfo) |
| [**delete**](./UserConfig#delete) | [UserConfigRequest](UserConfig#userconfigrequest) | [Empty](UserConfig#empty) |
| [**get**](./UserConfig#get) | [GetUserConfigRequest](UserConfig#getuserconfigrequest) | [UserConfigInfo](UserConfig#userconfiginfo) |
| [**list**](./UserConfig#list) | [UserConfigQuery](UserConfig#userconfigquery) | [UserConfigsInfo](UserConfig#userconfigsinfo) |
| [**stat**](./UserConfig#stat) | [UserConfigStatQuery](UserConfig#userconfigstatquery) | [Struct](UserConfig#struct) |



    
<br>

### create





> **POST** /config/v1/user-config/create
>






    
<br>

### update





> **POST** /config/v1/user-config/update
>






    
<br>

### set





> **POST** /config/v1/user-config/set
>






    
<br>

### delete





> **POST** /config/v1/user-config/delete
>






    
<br>

### get





> **POST** /config/v1/user-config/get
>






    
<br>

### list





> **POST** /config/v1/user-config/list
>






    
<br>

### stat





> **POST** /config/v1/user-config/stat
>






    


<br>
<br>

## Message



### GetUserConfigRequest
* **name** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### SetUserConfigRequest
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### UserConfigInfo
* **name** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### UserConfigQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **name** (string)  

    
* **user_id** (string)  

    <br>

### UserConfigRequest
* **name** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UserConfigStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UserConfigsInfo
* **results** (UserConfigInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
