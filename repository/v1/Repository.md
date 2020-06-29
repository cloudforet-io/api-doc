---
description:  
---
# Repository

>  **Package : spaceone.api.repository.v1**

## Repository

{% hint style="info" %}
**Repository Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [register](Repository.md#register)| [CreateRepositoryRequest](Repository.md#createrepositoryrequest) | [RepositoryInfo](Repository.md#repositoryinfo) |  |
| 2 | [update](Repository.md#update)| [UpdateRepositoryRequest](Repository.md#updaterepositoryrequest) | [RepositoryInfo](Repository.md#repositoryinfo) |  |
| 3 | [deregister](Repository.md#deregister)| [RepositoryRequest](Repository.md#repositoryrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Repository.md#get)| [GetRepositoryRequest](Repository.md#getrepositoryrequest) | [RepositoryInfo](Repository.md#repositoryinfo) |  |
| 5 | [list](Repository.md#list)| [RepositoryQuery](Repository.md#repositoryquery) | [RepositoriesInfo](Repository.md#repositoriesinfo) |  |
| 6 | [stat](Repository.md#stat)| [RepositoryStatQuery](Repository.md#repositorystatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### register
> **POST** /repository/v1/repositories
>



| Type | Message |
| :--- | :--- |
| Request | [CreateRepositoryRequest](Repository.md#createrepositoryrequest) |
| Response |  [RepositoryInfo](Repository.md#repositoryinfo)  |



### update
> **PUT** /repository/v1/repository/{repository_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateRepositoryRequest](Repository.md#updaterepositoryrequest) |
| Response |  [RepositoryInfo](Repository.md#repositoryinfo)  |



### deregister
> **DELETE** /repository/v1/repository/{repository_id}
>



| Type | Message |
| :--- | :--- |
| Request | [RepositoryRequest](Repository.md#repositoryrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /repository/v1/repositories/{repository_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetRepositoryRequest](Repository.md#getrepositoryrequest) |
| Response |  [RepositoryInfo](Repository.md#repositoryinfo)  |



### list
> **GET** /repository/v1/repositories
>
> **POST** /repository/v1/repositories/search




| Type | Message |
| :--- | :--- |
| Request | [RepositoryQuery](Repository.md#repositoryquery) |
| Response |  [RepositoriesInfo](Repository.md#repositoriesinfo)  |



### stat
> **POST** /repository/v1/repositories/stat
>



| Type | Message |
| :--- | :--- |
| Request | [RepositoryStatQuery](Repository.md#repositorystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateRepositoryRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | repository_type |string |✅ ||
| 3 | endpoint |string |❌ ||
| 4 | version |string |❌ ||
| 5 | secret_id |string |❌ ||
| 6 | domain_id |string |❌ ||

### GetRepositoryRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | repository_id |string |✅ ||
| 2 | only |string |❌ ||
| 3 | domain_id |string |❌ ||

### RepositoriesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[RepositoryInfo](Repository.md#repositoryinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### RepositoryInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | repository_id |string | ||
| 2 | name |string | ||
| 3 | repository_type |string | ||
| 4 | endpoint |string | ||
| 5 | version |string | ||
| 6 | secret_id |string | ||
| 7 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### RepositoryQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | repository_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | repository_type |string |❌ ||
| 5 | domain_id |string |❌ ||

### RepositoryRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | repository_id |string |✅ ||
| 2 | domain_id |string |❌ ||

### RepositoryStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### UpdateRepositoryRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | repository_id |string |✅ ||
| 2 | name |string |✅ ||
| 3 | domain_id |string |❌ ||
