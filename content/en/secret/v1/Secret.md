---
title: "Secret"
linkTitle: "Secret"
weight: 3
bookFlatSection: true
---
# [Secret](#Secret)
desc: A Secret is an external data, encrypted by CloudForet.


>  **Package : spaceone.api.secret.v1**

<br>
<br>

## Secret


**Secret Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Secret#create) | [CreateSecretRequest](Secret#createsecretrequest) | [SecretInfo](./Secret#secretinfo) |
| [**update**](./Secret#update) | [UpdateSecretRequest](Secret#updatesecretrequest) | [SecretInfo](./Secret#secretinfo) |
| [**delete**](./Secret#delete) | [SecretRequest](Secret#secretrequest) | [Empty](./Secret#empty) |
| [**update_data**](./Secret#update_data) | [UpdateSecretDataRequest](Secret#updatesecretdatarequest) | [Empty](./Secret#empty) |
| [**get_data**](./Secret#get_data) | [SecretRequest](Secret#secretrequest) | [SecretDataInfo](./Secret#secretdatainfo) |
| [**get**](./Secret#get) | [GetSecretRequest](Secret#getsecretrequest) | [SecretInfo](./Secret#secretinfo) |
| [**list**](./Secret#list) | [SecretQuery](Secret#secretquery) | [SecretsInfo](./Secret#secretsinfo) |
| [**stat**](./Secret#stat) | [SecretStatQuery](Secret#secretstatquery) | [Struct](./Secret#struct) |



    
<br>

### create

> **POST** /secret/v1/secret/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /secret/v1/secret/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /secret/v1/secret/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### update_data

> **POST** /secret/v1/secret/update-data
>




 {{< tabs " update_data " >}}




{{< /tabs >}}

    
<br>

### get_data

> **POST** /secret/v1/secret/get-data
>




 {{< tabs " get_data " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /secret/v1/secret/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /secret/v1/secret/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /secret/v1/secret/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateSecretRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    
* **secret_type** (SecretType)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **service_account_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **trusted_secret_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetSecretRequest
* **secret_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### SecretDataInfo
* **data** (Struct)  `Required` 

    
* **encrypted** (bool)  `Required` 

    
* **encrypt_options** (Struct)  `Required` 

    <br>

### SecretInfo
* **secret_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **secret_type** (SecretType)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **schema** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **service_account_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **trusted_secret_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### SecretQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **secret_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **secret_type** (SecretType)  `Required` 

  *is_required: false*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **service_account_id** (string)  `Required` 

  *is_required: false*

    
* **trusted_secret_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SecretRequest
* **secret_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SecretStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SecretsInfo
* **results** (SecretInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateSecretDataRequest
* **secret_id** (string)  `Required` 

  *is_required: true*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **schema** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateSecretRequest
* **secret_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **release_project** (bool)  `Required` 

  *is_required: false*

    <br>
