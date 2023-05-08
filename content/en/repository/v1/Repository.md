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

> **POST** /repository/v1/repository/register
>




 {{< tabs " register " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /repository/v1/repository/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### deregister

> **POST** /repository/v1/repository/deregister
>




 {{< tabs " deregister " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /repository/v1/repository/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /repository/v1/repository/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /repository/v1/repository/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


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
