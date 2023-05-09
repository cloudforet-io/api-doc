---
title: "Repository"
linkTitle: "Repository"
weight: 3
bookFlatSection: true
---
# [Repository](#Repository)
desc: A Repository is a repository storing data of deployable plugins.


>  **Package : spaceone.api.repository.v1**

<br>
<br>

## Repository





**Repository Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](./Repository#register) | [CreateRepositoryRequest](Repository#createrepositoryrequest) | [RepositoryInfo](./Repository#repositoryinfo) |
| [**update**](./Repository#update) | [UpdateRepositoryRequest](Repository#updaterepositoryrequest) | [RepositoryInfo](./Repository#repositoryinfo) |
| [**deregister**](./Repository#deregister) | [RepositoryRequest](Repository#repositoryrequest) | [Empty](./Repository#empty) |
| [**get**](./Repository#get) | [GetRepositoryRequest](Repository#getrepositoryrequest) | [RepositoryInfo](./Repository#repositoryinfo) |
| [**list**](./Repository#list) | [RepositoryQuery](Repository#repositoryquery) | [RepositoriesInfo](./Repository#repositoriesinfo) |
| [**stat**](./Repository#stat) | [RepositoryStatQuery](Repository#repositorystatquery) | [Struct](./Repository#struct) |



    
<br>

### register

desc: Registers a Repository. The parameter `name` can only include alphabets, numbers, and hyphens(-). The parameter `repository_type` can be either `local` or `remote`. The parameter `endpoint` is needed if the `repository_type` is `remote`.
request_example: >-
{
"name": "Local",
"repository_type": "local",
"endpoint": "grpc+ssl://local-url:443"
}
response_example: >-
{
"repository_id": "repo-123456789012",
"name": "Local",
"repository_type": "local",
"endpoint": "grpc+ssl://local-url:443",
"created_at": "2022-01-01T02:27:02.924Z"
}



> **POST** /repository/v1/repository/register
>






    
<br>

### update

desc: Updates a specific Repository registered. You must specify the `repository_id` of the Repository to update. You can make changes in Repository settings, including `name`.
request_example: >-
{
"repository_id": "repo-123456789012",
"name": "Local-repo"
}
response_example: >-
{
"repository_id": "repo-123456789012",
"name": "Local-repo",
"repository_type": "local",
"endpoint": "grpc+ssl://local-url:443",
"created_at": "2022-01-01T02:27:02.924Z"
}



> **POST** /repository/v1/repository/update
>






    
<br>

### deregister

desc: Deregisters and deletes a specific Repository. You must specify the `repository_id` of the Repository to deregister.
request_example: >-
{
"repository_id": "repo-123456789012"
}



> **POST** /repository/v1/repository/deregister
>






    
<br>

### get

desc: Gets a specific Repository. Prints detailed information about the Repository, including  `name`, `repository_type`, and `endpoint`.
request_example: >-
{
"repository_id": "repo-123456789012"
}
response_example: >-
{
"repository_id": "repo-123456789012",
"name": "Local-repo",
"repository_type": "local",
"endpoint": "grpc+ssl://local-url:443",
"created_at": "2022-01-01T02:26:29.081Z"
}



> **POST** /repository/v1/repository/get
>






    
<br>

### list

desc: Gets a list of all Repositories regardless of `domain`. You can use a query to get a filtered list of Repositories.
request_example: >-
{
"query": {},
"repository_id": "repo-123456789012"
}
response_example: >-
{
"results": [
{
"repository_id": "repo-123456789012",
"name": "Local-repo",
"repository_type": "local",
"endpoint": "grpc+ssl://local-url:443",
"created_at": "2022-01-01T02:26:29.081Z"
}
],
"total_count": 1
}



> **POST** /repository/v1/repository/list
>






    
<br>

### stat





> **POST** /repository/v1/repository/stat
>






    


<br>
<br>

## Message



### CreateRepositoryRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **repository_type** (string)  `Required` 

  *is_required: true*

    
* **endpoint** (string)  `Required` 

  *is_required: false*

    
* **version** (string)  `Required` 

  *is_required: false*

    
* **secret_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetRepositoryRequest
* **repository_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RepositoriesInfo
* **results** (RepositoryInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### RepositoryInfo
* **repository_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **repository_type** (string)  `Required` 

    
* **endpoint** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **secret_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### RepositoryQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **repository_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **repository_type** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RepositoryRequest
* **repository_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RepositoryStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateRepositoryRequest
* **repository_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
