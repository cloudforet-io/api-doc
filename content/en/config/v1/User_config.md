---
title: "User_config"
linkTitle: "User_config"
weight: 3
bookFlatSection: true
---
# [User_config](#User_config)
desc: UserConfig API which configure environments for user


>  **Package : spaceone.api.config.v1**

<br>
<br>

## User_config





**UserConfig Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./UserConfig#create) | [SetUserConfigRequest](UserConfig#setuserconfigrequest) | [UserConfigInfo](./UserConfig#userconfiginfo) |
| [**update**](./UserConfig#update) | [SetUserConfigRequest](UserConfig#setuserconfigrequest) | [UserConfigInfo](./UserConfig#userconfiginfo) |
| [**set**](./UserConfig#set) | [SetUserConfigRequest](UserConfig#setuserconfigrequest) | [UserConfigInfo](./UserConfig#userconfiginfo) |
| [**delete**](./UserConfig#delete) | [UserConfigRequest](UserConfig#userconfigrequest) | [Empty](./UserConfig#empty) |
| [**get**](./UserConfig#get) | [GetUserConfigRequest](UserConfig#getuserconfigrequest) | [UserConfigInfo](./UserConfig#userconfiginfo) |
| [**list**](./UserConfig#list) | [UserConfigQuery](UserConfig#userconfigquery) | [UserConfigsInfo](./UserConfig#userconfigsinfo) |
| [**stat**](./UserConfig#stat) | [UserConfigStatQuery](UserConfig#userconfigstatquery) | [Struct](./UserConfig#struct) |



    
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
* **name** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### SetUserConfigRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UserConfigInfo
* **name** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### UserConfigQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UserConfigRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UserConfigStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UserConfigsInfo
* **results** (UserConfigInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
