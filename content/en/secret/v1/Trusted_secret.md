---
title: "Trusted_secret"
linkTitle: "Trusted_secret"
weight: 3
bookFlatSection: true
---
# [Trusted_secret](#Trusted_secret)
desc: A Trusted Secret is an external data, encrypted by CloudForet.


>  **Package : spaceone.api.secret.v1**

<br>
<br>

## Trusted_secret


**TrustedSecret Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./TrustedSecret#create) | [CreateTrustedSecretRequest](TrustedSecret#createtrustedsecretrequest) | [TrustedSecretInfo](./TrustedSecret#trustedsecretinfo) |
| [**update**](./TrustedSecret#update) | [UpdateTrustedSecretRequest](TrustedSecret#updatetrustedsecretrequest) | [TrustedSecretInfo](./TrustedSecret#trustedsecretinfo) |
| [**delete**](./TrustedSecret#delete) | [TrustedSecretRequest](TrustedSecret#trustedsecretrequest) | [Empty](./TrustedSecret#empty) |
| [**update_data**](./TrustedSecret#update_data) | [UpdateTrustedSecretDataRequest](TrustedSecret#updatetrustedsecretdatarequest) | [Empty](./TrustedSecret#empty) |
| [**get**](./TrustedSecret#get) | [GetTrustedSecretRequest](TrustedSecret#gettrustedsecretrequest) | [TrustedSecretInfo](./TrustedSecret#trustedsecretinfo) |
| [**list**](./TrustedSecret#list) | [TrustedSecretQuery](TrustedSecret#trustedsecretquery) | [TrustedSecretsInfo](./TrustedSecret#trustedsecretsinfo) |
| [**stat**](./TrustedSecret#stat) | [TrustedSecretStatQuery](TrustedSecret#trustedsecretstatquery) | [Struct](./TrustedSecret#struct) |



    
<br>

### create

> **POST** /secret/v1/trusted-secret/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /secret/v1/trusted-secret/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /secret/v1/trusted-secret/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### update_data

> **POST** /secret/v1/trusted-secret/update-data
>




 {{< tabs " update_data " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /secret/v1/trusted-secret/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /secret/v1/trusted-secret/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /secret/v1/trusted-secret/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateTrustedSecretRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **service_account_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetTrustedSecretRequest
* **trusted_secret_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### TrustedSecretInfo
* **trusted_secret_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **schema** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **service_account_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### TrustedSecretQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **trusted_secret_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **service_account_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### TrustedSecretRequest
* **trusted_secret_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### TrustedSecretStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### TrustedSecretsInfo
* **results** (TrustedSecretInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateTrustedSecretDataRequest
* **trusted_secret_id** (string)  `Required` 

  *is_required: true*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    
* **schema** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateTrustedSecretRequest
* **trusted_secret_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
