---
description:  
---
# Repository

>  **Package : spaceone.api.repository.v1**

## Repository

{% hint style="info" %}
**Repository Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**register**](repository.md#register)|   [CreateRepositoryRequest](repository.md#createrepositoryrequest) |   [RepositoryInfo](repository.md#repositoryinfo) |  |
| [**update**](repository.md#update)|   [UpdateRepositoryRequest](repository.md#updaterepositoryrequest) |   [RepositoryInfo](repository.md#repositoryinfo) |  |
| [**deregister**](repository.md#deregister)|   [RepositoryRequest](repository.md#repositoryrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](repository.md#get)|   [GetRepositoryRequest](repository.md#getrepositoryrequest) |   [RepositoryInfo](repository.md#repositoryinfo) |  |
| [**list**](repository.md#list)|   [RepositoryQuery](repository.md#repositoryquery) |   [RepositoriesInfo](repository.md#repositoriesinfo) |  |
| [**stat**](repository.md#stat)|   [RepositoryStatQuery](repository.md#repositorystatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**register**](repository.md#register) </div> | <div style="width:200px; text-align:center;">    [CreateRepositoryRequest](repository.md#createrepositoryrequest)  </div> | <div style="width:200px; text-align:center;">   [RepositoryInfo](repository.md#repositoryinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](repository.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateRepositoryRequest](repository.md#updaterepositoryrequest)  </div> | <div style="width:200px; text-align:center;">   [RepositoryInfo](repository.md#repositoryinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**deregister**](repository.md#deregister) </div> | <div style="width:200px; text-align:center;">    [RepositoryRequest](repository.md#repositoryrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](repository.md#get) </div> | <div style="width:200px; text-align:center;">    [GetRepositoryRequest](repository.md#getrepositoryrequest)  </div> | <div style="width:200px; text-align:center;">   [RepositoryInfo](repository.md#repositoryinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](repository.md#list) </div> | <div style="width:200px; text-align:center;">    [RepositoryQuery](repository.md#repositoryquery)  </div> | <div style="width:200px; text-align:center;">   [RepositoriesInfo](repository.md#repositoriesinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](repository.md#stat) </div> | <div style="width:200px; text-align:center;">    [RepositoryStatQuery](repository.md#repositorystatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### register
> **POST** /repository/v1/repositories
>


| Type | Message |
| :--- | :--- |
| Request | [CreateRepositoryRequest](repository.md#createrepositoryrequest) |
| Response |  [RepositoryInfo](repository.md#repositoryinfo)  |
 
 

 
### update
> **PUT** /repository/v1/repository/{repository_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateRepositoryRequest](repository.md#updaterepositoryrequest) |
| Response |  [RepositoryInfo](repository.md#repositoryinfo)  |
 
 

 
### deregister
> **DELETE** /repository/v1/repository/{repository_id}
>


| Type | Message |
| :--- | :--- |
| Request | [RepositoryRequest](repository.md#repositoryrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /repository/v1/repositories/{repository_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetRepositoryRequest](repository.md#getrepositoryrequest) |
| Response |  [RepositoryInfo](repository.md#repositoryinfo)  |
 
 

 
### list
> **GET** /repository/v1/repositories
>
> **POST** /repository/v1/repositories/search



| Type | Message |
| :--- | :--- |
| Request | [RepositoryQuery](repository.md#repositoryquery) |
| Response |  [RepositoriesInfo](repository.md#repositoriesinfo)  |
 
 

 
### stat
> **POST** /repository/v1/repositories/stat
>


| Type | Message |
| :--- | :--- |
| Request | [RepositoryStatQuery](repository.md#repositorystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateRepositoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| repository_type |string|✅| |
| endpoint |string|❌| |
| version |string|❌| |
| secret_id |string|❌| |
| domain_id |string|✅| |

### GetRepositoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| repository_id |string|✅| |
| only |list of string|❌| |
| domain_id |string|✅| |

### RepositoriesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of RepositoryInfo](repository.md#repositoryinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RepositoryInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| repository_id |string | |
| name |string | |
| repository_type |string | |
| endpoint |string | |
| version |string | |
| secret_id |string | |
| created_at |string | |

### RepositoryQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| repository_id |string|❌| |
| name |string|❌| |
| repository_type |string|❌| |
| domain_id |string|✅| |

### RepositoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| repository_id |string|✅| |
| domain_id |string|✅| |

### RepositoryStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### UpdateRepositoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| repository_id |string|✅| |
| name |string|❌| |
| domain_id |string|✅| |
