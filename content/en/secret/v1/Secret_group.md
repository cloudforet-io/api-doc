---
title: "Secret_group"
linkTitle: "Secret_group"
weight: 3
bookFlatSection: true
---
# [Secret_group](#Secret_group)



>  **Package : spaceone.api.secret.v1**

<br>
<br>

## Secret_group





**SecretGroup Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./SecretGroup#create) | [CreateSecretGroupRequest](SecretGroup#createsecretgrouprequest) | [SecretGroupInfo](./SecretGroup#secretgroupinfo) |
| [**update**](./SecretGroup#update) | [UpdateSecretGroupRequest](SecretGroup#updatesecretgrouprequest) | [SecretGroupInfo](./SecretGroup#secretgroupinfo) |
| [**add_secret**](./SecretGroup#add_secret) | [SecretGroupSecretRequest](SecretGroup#secretgroupsecretrequest) | [SecretGroupSecretInfo](./SecretGroup#secretgroupsecretinfo) |
| [**remove_secret**](./SecretGroup#remove_secret) | [SecretGroupSecretRequest](SecretGroup#secretgroupsecretrequest) | [Empty](./SecretGroup#empty) |
| [**delete**](./SecretGroup#delete) | [SecretGroupRequest](SecretGroup#secretgrouprequest) | [Empty](./SecretGroup#empty) |
| [**get**](./SecretGroup#get) | [GetSecretGroupRequest](SecretGroup#getsecretgrouprequest) | [SecretGroupInfo](./SecretGroup#secretgroupinfo) |
| [**list**](./SecretGroup#list) | [SecretGroupQuery](SecretGroup#secretgroupquery) | [SecretGroupsInfo](./SecretGroup#secretgroupsinfo) |
| [**stat**](./SecretGroup#stat) | [SecretGroupStatQuery](SecretGroup#secretgroupstatquery) | [Struct](./SecretGroup#struct) |



    
<br>

### create





> **POST** /secret/v1/secret-group/create
>






    
<br>

### update





> **POST** /secret/v1/secret-group/update
>






    
<br>

### add_secret





> **POST** /secret/v1/secret-group/add-secret
>






    
<br>

### remove_secret





> **POST** /secret/v1/secret-group/remove-secret
>






    
<br>

### delete





> **POST** /secret/v1/secret-group/delete
>






    
<br>

### get





> **POST** /secret/v1/secret-group/get
>






    
<br>

### list





> **POST** /secret/v1/secret-group/list
>






    
<br>

### stat





> **POST** /secret/v1/secret-group/stat
>






    


<br>
<br>

## Message



### CreateSecretGroupRequest
* **name** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **tags** (Struct) 

    <br>

### GetSecretGroupRequest
* **secret_group_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### SecretGroupInfo
* **secret_group_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### SecretGroupQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **secret_group_id** (string) 

    
* **name** (string) 

    
* **secret_id** (string) 

    <br>

### SecretGroupRequest
* **secret_group_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### SecretGroupSecretInfo
* **secret_group_info** (SecretGroupInfo)  `Required` 

    
* **secret_info** (SecretInfo)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### SecretGroupSecretRequest
* **secret_group_id** (string)  `Required` 

    
* **secret_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### SecretGroupStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### SecretGroupsInfo
* **results** (SecretGroupInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateSecretGroupRequest
* **secret_group_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **tags** (Struct) 

    <br>
