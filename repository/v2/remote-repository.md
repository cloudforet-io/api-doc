---
description:  
---
# Remote repository

>  **Package : spaceone.api.repository.v2**

## RemoteRepository

{% hint style="info" %}
**RemoteRepository Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get**](remote-repository.md#get)|   [GetRemoteRepository](remote-repository.md#getremoterepository) |   [RemoteRepositoryInfo](remote-repository.md#remoterepositoryinfo) |
| [**list**](remote-repository.md#list)|   [RemoteRepositoryQuery](remote-repository.md#remoterepositoryquery) |   [RemoteRepositoriesInfo](remote-repository.md#remoterepositoriesinfo) | 
 

 
### get
> **POST** /repository/v2/remote-repository/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetRemoteRepository](remote-repository.md#getremoterepository) |
| Response |  [RemoteRepositoryInfo](remote-repository.md#remoterepositoryinfo)  |
 
 

 
### list
> **POST** /repository/v2/remote-repository/list
>


| Type | Message |
| :--- | :--- |
| Request | [RemoteRepositoryQuery](remote-repository.md#remoterepositoryquery) |
| Response |  [RemoteRepositoriesInfo](remote-repository.md#remoterepositoriesinfo)  |


## 

## Message

### GetRemoteRepository
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |

### RemoteRepositoriesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of RemoteRepositoryInfo](remote-repository.md#remoterepositoryinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RemoteRepositoryInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| name |string | |
| description |string | |
| endpoint |string | |
| version |string | |

### RemoteRepositoryQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✘| |
| version |string|✘| |
