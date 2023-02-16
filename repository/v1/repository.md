---
description: A Repository is a repository storing data of deployable plugins.
---
# Repository

>  **Package : spaceone.api.repository.v1**

## Repository

{% hint style="info" %}
**Repository Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](repository.md#register)|   [CreateRepositoryRequest](repository.md#createrepositoryrequest) |   [RepositoryInfo](repository.md#repositoryinfo) |
| [**update**](repository.md#update)|   [UpdateRepositoryRequest](repository.md#updaterepositoryrequest) |   [RepositoryInfo](repository.md#repositoryinfo) |
| [**deregister**](repository.md#deregister)|   [RepositoryRequest](repository.md#repositoryrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](repository.md#get)|   [GetRepositoryRequest](repository.md#getrepositoryrequest) |   [RepositoryInfo](repository.md#repositoryinfo) |
| [**list**](repository.md#list)|   [RepositoryQuery](repository.md#repositoryquery) |   [RepositoriesInfo](repository.md#repositoriesinfo) |
| [**stat**](repository.md#stat)|   [RepositoryStatQuery](repository.md#repositorystatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### register
> **POST** /repository/v1/repository/register
>

> Registers a Repository. The parameter `name` can only include alphabets, numbers, and hyphens(-). The parameter `repository_type` can be either `local` or `remote`. The parameter `endpoint` is needed if the `repository_type` is `remote`.

| Type | Message |
| :--- | :--- |
| Request | [CreateRepositoryRequest](repository.md#createrepositoryrequest) |
| Response |  [RepositoryInfo](repository.md#repositoryinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "Local",
    "repository_type": "local",
    "endpoint": "grpc+ssl://local-url:443"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "repository_id": "repo-123456789012",
    "name": "Local",
    "repository_type": "local",
    "endpoint": "grpc+ssl://local-url:443",
    "created_at": "2022-01-01T02:27:02.924Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /repository/v1/repository/update
>

> Updates a specific Repository registered. You must specify the `repository_id` of the Repository to update. You can make changes in Repository settings, including `name`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateRepositoryRequest](repository.md#updaterepositoryrequest) |
| Response |  [RepositoryInfo](repository.md#repositoryinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "repository_id": "repo-123456789012",
    "name": "Local-repo"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "repository_id": "repo-123456789012",
    "name": "Local-repo",
    "repository_type": "local",
    "endpoint": "grpc+ssl://local-url:443",
    "created_at": "2022-01-01T02:27:02.924Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### deregister
> **POST** /repository/v1/repository/deregister
>

> Deregisters and deletes a specific Repository. You must specify the `repository_id` of the Repository to deregister.

| Type | Message |
| :--- | :--- |
| Request | [RepositoryRequest](repository.md#repositoryrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "repository_id": "repo-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /repository/v1/repository/get
>

> Gets a specific Repository. Prints detailed information about the Repository, including  `name`, `repository_type`, and `endpoint`.

| Type | Message |
| :--- | :--- |
| Request | [GetRepositoryRequest](repository.md#getrepositoryrequest) |
| Response |  [RepositoryInfo](repository.md#repositoryinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "repository_id": "repo-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "repository_id": "repo-123456789012",
    "name": "Local-repo",
    "repository_type": "local",
    "endpoint": "grpc+ssl://local-url:443",
    "created_at": "2022-01-01T02:26:29.081Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /repository/v1/repository/list
>

> Gets a list of all Repositories regardless of `domain`. You can use a query to get a filtered list of Repositories.

| Type | Message |
| :--- | :--- |
| Request | [RepositoryQuery](repository.md#repositoryquery) |
| Response |  [RepositoriesInfo](repository.md#repositoriesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "repository_id": "repo-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /repository/v1/repository/stat
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
| name |string|✔| |
| repository_type |string|✔| |
| endpoint |string|✘| |
| version |string|✘| |
| secret_id |string|✘| |
| domain_id |string|✔| |

### GetRepositoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| repository_id |string|✔| |
| only |list of string|✘| |
| domain_id |string|✔| |

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
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| repository_id |string|✘| |
| name |string|✘| |
| repository_type |string|✘| |
| domain_id |string|✔| |

### RepositoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| repository_id |string|✔| |
| domain_id |string|✔| |

### RepositoryStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### UpdateRepositoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| repository_id |string|✔| |
| name |string|✘| |
| domain_id |string|✔| |
