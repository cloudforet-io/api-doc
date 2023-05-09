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

desc: Creates a new Secret. When creating the resource, external `data` is encrypted, and a `secret_id` is issued for data access by other microservices.
request_example: >-
{
"name": "aws-dev",
"data": "********",
"secret_type": "CREDENTIALS",
"schema": "aws_access_key",
"service_account_id": "sa-123456789012",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"secret_id": "secret-123456789012",
"name": "aws-dev",
"secret_type": "CREDENTIALS",
"tags": {},
"schema": "aws_access_key",
"provider": "aws",
"service_account_id": "sa-123456789012",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:10:14.851Z"
}



> **POST** /secret/v1/secret/create
>






    
<br>

### update

desc: Updates a specific Secret. You can make changes in Secret settings, including `name` and`tags`.
request_example: >-
{
"secret_id": "secret-123456789012",
"name": "aws-dev2",
"tags": { "a": "b"},
"project_id": "project-123456789012",
"release_project": true,
"domain_id": "domain-123456789012"
}
response_example: >-
{
"secret_id": "secret-123456789012",
"name": "aws-dev2",
"secret_type": "CREDENTIALS",
"tags": { "a": "b"},
"schema": "aws_access_key",
"provider": "aws",
"service_account_id": "sa-123456789012",
"project_id": "",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:10:14.851Z"
}



> **POST** /secret/v1/secret/update
>






    
<br>

### delete

desc: Deletes a specific Secret. You must specify the `secret_id` of the Secret to delete.
request_example: >-
{
"secret_id": "secret-123456789012",
"domain_id": "domain-123456789012"
}



> **POST** /secret/v1/secret/delete
>






    
<br>

### update_data

desc: Updates encrypted data of a specific Secret resource. For example, to change the parameter `data`, external data to encrypt, you can use `update_data` to create new encrypted data based on the changed `data` and store it in the Secret resource.
request_example: >-
{
"secret_id": "secret-123456789012",
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



> **POST** /secret/v1/secret/update-data
>






    
<br>

### get_data

desc: Gets a specific Secret. Prints detailed information about the Secret, including  `name`, `tags`, `schema`, and `provider`.
request_example: >-
{
"secret_id": "secret-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"data": {
"encrypted_data": "xxxxxxxxxxxxxxxxxx"
},
"encrypted": true,
"encrypt_options": {
"encrypt_algorithm": "SPACEONE_DEFAULT",
"encrypted_data_key": "xxxxxx"
}
}



> **POST** /secret/v1/secret/get-data
>






    
<br>

### get

desc: Gets a specific Post. You must specify the `post_id` of the Post to get, and the `board_id` of the Board where the child Post to get belongs. Prints detailed information about the Post.
request_example: >-
{
"secret_id": "secret-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"secret_id": "secret-123456789012",
"name": "aws-dev",
"secret_type": "CREDENTIALS",
"tags": {},
"schema": "aws_access_key",
"provider": "aws",
"service_account_id": "sa-123456789012",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:10:14.851Z"
}



> **POST** /secret/v1/secret/get
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
"secret_id": "secret-123456789012",
"name": "aws-dev",
"secret_type": "CREDENTIALS",
"tags": {},
"schema": "aws_access_key",
"provider": "aws",
"service_account_id": "sa-123456789012",
"project_id": "project-123456789012",
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T06:10:14.851Z"
},
{
"secret_id": "secret-987654321098",
"name": "plugin-credentials",
"secret_type": "CREDENTIALS",
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T02:31:01.709Z"
}
],
"total_count": 2
}



> **POST** /secret/v1/secret/list
>






    
<br>

### stat





> **POST** /secret/v1/secret/stat
>






    


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
