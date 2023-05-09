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

desc: Creates a new Trusted Secret. When creating the resource, external `data` is encrypted, and a `trusted_secret_id` is issued for data access by other microservices.
request_example: >-
{
"name": "aws-dev",
"data": "********",
"schema": "aws_access_key",
"service_account_id": "sa-123456789012",
"tags": {},
"domain_id": "domain-123456789012"
}
response_example: >-
{
"trusted_secret_id": "trusted-secret-123456789012",
"name": "aws-dev",
"tags": {},
"schema": "aws_access_key",
"provider": "aws",
"service_account_id": "sa-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:10:14.851Z"
}



> **POST** /secret/v1/trusted-secret/create
>






    
<br>

### update

desc: Updates a specific Secret. You can make changes in Secret settings, including `name` and`tags`.
request_example: >-
{
"trusted_secret_id": "trusted-secret-123456789012",
"name": "aws-dev2",
"tags": { "a": "b"},
"domain_id": "domain-123456789012"
}
response_example: >-
{
"trusted_secret_id": "trusted-secret-123456789012",
"name": "aws-dev2",
"tags": { "a": "b"},
"schema": "aws_access_key",
"provider": "aws",
"service_account_id": "sa-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:10:14.851Z"
}



> **POST** /secret/v1/trusted-secret/update
>






    
<br>

### delete

desc: Deletes a specific Secret. You must specify the `secret_id` of the Secret to delete.
request_example: >-
{
"trusted_secret_id": "trusted-secret-123456789012",
"domain_id": "domain-123456789012"
}



> **POST** /secret/v1/trusted-secret/delete
>






    
<br>

### update_data

desc: Updates encrypted data of a specific Secret resource. For example, to change the parameter `data`, external data to encrypt, you can use `update_data` to create new encrypted data based on the changed `data` and store it in the Secret resource.
request_example: >-
{
"trusted_secret_id": "trusted-secret-123456789012",
"data": "********",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"data": {
"encrypted_data": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
},
"encrypted": true,
"encrypt_options": {
"encrypted_data_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"encrypt_algorithm": "CloudForet_DEFAULT"
}
}



> **POST** /secret/v1/trusted-secret/update-data
>






    
<br>

### get

desc: Gets a specific Post. You must specify the `post_id` of the Post to get, and the `board_id` of the Board where the child Post to get belongs. Prints detailed information about the Post.
request_example: >-
{
"trusted_secret_id": "trusted-secret-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"trusted_secret_id": "trusted-secret-123456789012",
"name": "aws-dev",
"tags": {},
"schema": "aws_access_key",
"provider": "aws",
"service_account_id": "sa-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:10:14.851Z"
}



> **POST** /secret/v1/trusted-secret/get
>






    
<br>

### list

desc: Gets a list of all Posts. You can use a query to get a filtered list of Posts.
request_example: >-
{
"query": {},
"domain_id": "domain-123456789012"
}
response_example: >-
{
"results": [
{
"trusted_secret_id": "trusted-secret-123456789012",
"name": "aws-dev",
"tags": {},
"schema": "aws_access_key",
"provider": "aws",
"service_account_id": "sa-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:10:14.851Z"
},
{
"trusted_secret_id": "trusted-secret-987654321098",
"name": "plugin-credentials",
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T02:31:01.709Z"
}
],
"total_count": 2
}



> **POST** /secret/v1/trusted-secret/list
>






    
<br>

### stat





> **POST** /secret/v1/trusted-secret/stat
>






    


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
