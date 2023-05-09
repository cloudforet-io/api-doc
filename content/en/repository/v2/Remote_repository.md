---
title: "Remote_repository"
linkTitle: "Remote_repository"
weight: 3
bookFlatSection: true
---
# [Remote_repository](#Remote_repository)



>  **Package : spaceone.api.repository.v2**

<br>
<br>

## Remote_repository





**RemoteRepository Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get**](./RemoteRepository#get) | [GetRemoteRepository](RemoteRepository#getremoterepository) | [RemoteRepositoryInfo](./RemoteRepository#remoterepositoryinfo) |
| [**list**](./RemoteRepository#list) | [RemoteRepositoryQuery](RemoteRepository#remoterepositoryquery) | [RemoteRepositoriesInfo](./RemoteRepository#remoterepositoriesinfo) |



    
<br>

### get





> **POST** /repository/v2/remote-repository/get
>






    
<br>

### list





> **POST** /repository/v2/remote-repository/list
>






    


<br>
<br>

## Message



### GetRemoteRepository
* **name** (string)  `Required` 

  *is_required: true*

    <br>

### RemoteRepositoriesInfo
* **results** (RemoteRepositoryInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### RemoteRepositoryInfo
* **name** (string)  `Required` 

    
* **description** (string)  `Required` 

    
* **endpoint** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### RemoteRepositoryQuery
* **name** (string)  `Required` 

  *is_required: false*

    
* **version** (string)  `Required` 

  *is_required: false*

    <br>
