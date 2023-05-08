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




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /secret/v1/secret-group/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### add_secret

> **POST** /secret/v1/secret-group/add-secret
>




 {{< tabs " add_secret " >}}




{{< /tabs >}}

    
<br>

### remove_secret

> **POST** /secret/v1/secret-group/remove-secret
>




 {{< tabs " remove_secret " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /secret/v1/secret-group/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /secret/v1/secret-group/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /secret/v1/secret-group/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /secret/v1/secret-group/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateSecretGroupRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetSecretGroupRequest
* **secret_group_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### SecretGroupInfo
* **secret_group_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### SecretGroupQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **secret_group_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **secret_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SecretGroupRequest
* **secret_group_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SecretGroupSecretInfo
* **secret_group_info** (SecretGroupInfo)  `Required` 

    
* **secret_info** (SecretInfo)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### SecretGroupSecretRequest
* **secret_group_id** (string)  `Required` 

  *is_required: true*

    
* **secret_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SecretGroupStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SecretGroupsInfo
* **results** (SecretGroupInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateSecretGroupRequest
* **secret_group_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
